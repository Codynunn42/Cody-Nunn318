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

function validateRequestId(id) {
  if (
    typeof id !== "string" ||
    id.length === 0 ||
    id.length > 128 ||
    !/^[A-Za-z0-9][A-Za-z0-9._-]*$/.test(id)
  ) {
    throw new Error("invalid request_id");
  }

  return id;
}

function write(record) {
  ensureReady();

  const id =
    record.request_id !== undefined && record.request_id !== null
      ? validateRequestId(record.request_id)
      : crypto.randomUUID();

  const stored = {
    ...record,
    request_id: id
  };

  const canonical = JSON.stringify(stored, null, 2);
  const hash = sha256(canonical);
  const file = path.join(evidenceDir, `${id}.json`);

  fs.writeFileSync(file, canonical, {
    encoding: "utf8",
    flag: "wx"
  });

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

function readLatest() {
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

function latest() {
  ensureReady();
  return readLatest();
}

function health() {
  try {
    if (!fs.existsSync(evidenceDir)) {
      return {
        status: "fail",
        source: "persistent_evidence_store",
        error: "evidence directory missing"
      };
    }

    const readBack = readLatest();

    return {
      status:
        readBack &&
        readBack.verified
          ? "pass"
          : "fail",
      source: "persistent_evidence_store",
      reference: readBack ? readBack.reference : null,
      hash: readBack ? readBack.hash : null,
      error: readBack ? null : "latest evidence missing"
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