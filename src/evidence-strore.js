const fs = require("fs");
const path = require("path");
const crypto = require("crypto");

const root =
  process.env.SSAI_DATA_DIR ||
  path.join(__dirname, "..", ".data");

const evidenceDir = path.join(root, "evidence");
const latestFile = path.join(root, "latest.json");

function ensureReady() {
  fs.mkdirSync(evidenceDir, { recursive: true });
}

function sha256(text) {
  return crypto
    .createHash("sha256")
    .update(text)
    .digest("hex");
}

function write(record) {
  ensureReady();

  const id = record.request_id || crypto.randomUUID();

  const stored = {
    ...record,
    request_id: id
  };

  const canonical = JSON.stringify(stored, null, 2);
  const hash = sha256(canonical);
  const file = path.join(evidenceDir, `${id}.json`);

  fs.writeFileSync(file, canonical, "utf8");

  const pointer = {
    request_id: id,
    reference: file,
    hash,
    timestamp:
      stored.timestamp || new Date().toISOString()
  };

  fs.writeFileSync(
    latestFile,
    JSON.stringify(pointer, null, 2),
    "utf8"
  );

  return {
    record: stored,
    reference: file,
    hash,
    state: "verified"
  };
}

function latest() {
  ensureReady();

  if (!fs.existsSync(latestFile)) {
    return null;
  }

  const pointer = JSON.parse(
    fs.readFileSync(latestFile, "utf8")
  );

  if (!fs.existsSync(pointer.reference)) {
    throw new Error("latest evidence target missing");
  }

  const content = fs.readFileSync(
    pointer.reference,
    "utf8"
  );

  const actualHash = sha256(content);

  return {
    record: JSON.parse(content),
    reference: pointer.reference,
    hash: pointer.hash,
    actual_hash: actualHash,
    verified: pointer.hash === actualHash
  };
}

function health() {
  try {
    ensureReady();

    const probe = {
      request_id: crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      type: "evidence-health-probe",
      outcome: "pass"
    };

    const saved = write(probe);
    const readBack = latest();

    return {
      status:
        readBack &&
        readBack.verified &&
        saved.hash === readBack.hash
          ? "pass"
          : "fail",
      source: "persistent_evidence_store",
      reference: saved.reference,
      hash: saved.hash
    };
  } catch (error) {
    return {
      status: "fail",
      source: "persistent_evidence_store",
      error: error.message
    };
  }
}

module.exports = {
  write,
  latest,
  health
};