const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const test = require("node:test");

const modulePath = path.join(__dirname, "..", "src", "evidence-strore.js");

function loadStore(root) {
  process.env.SSAI_DATA_DIR = root;
  delete require.cache[require.resolve(modulePath)];
  return require(modulePath);
}

test("health verifies existing evidence without mutating the store", (t) => {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), "ssai-evidence-test-"));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));

  const store = loadStore(root);
  const saved = store.write({
    request_id: "substantive-record",
    type: "governance-decision",
    outcome: "observed"
  });
  const latestBefore = fs.readFileSync(
    path.join(root, "latest.json"),
    "utf8"
  );
  const filesBefore = fs.readdirSync(path.join(root, "evidence")).sort();

  const result = store.health();

  assert.equal(result.status, "pass");
  assert.equal(result.reference, saved.reference);
  assert.equal(result.hash, saved.hash);
  assert.equal(
    fs.readFileSync(path.join(root, "latest.json"), "utf8"),
    latestBefore
  );
  assert.deepEqual(
    fs.readdirSync(path.join(root, "evidence")).sort(),
    filesBefore
  );
});

test("health fails without creating a missing evidence store", (t) => {
  const parent = fs.mkdtempSync(path.join(os.tmpdir(), "ssai-evidence-test-"));
  const root = path.join(parent, "missing");
  t.after(() => fs.rmSync(parent, { recursive: true, force: true }));

  const result = loadStore(root).health();

  assert.equal(result.status, "fail");
  assert.equal(result.error, "evidence directory missing");
  assert.equal(fs.existsSync(root), false);
});
