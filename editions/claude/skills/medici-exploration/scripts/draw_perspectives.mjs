// Draw standing-pool perspectives and emit a replayable JSON receipt.
// Node.js fallback for hosts without Python; selection and receipt match draw_perspectives.py.

import { createHash, randomBytes } from "node:crypto";
import { readFileSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { parseArgs } from "node:util";

const usage =
  "usage: draw_perspectives.mjs --own-perspective TEXT [--count N] [--seed SEED] " +
  "[--pool PATH] [--expected-pool-sha256 SHA256]";

function fail(message) {
  process.stderr.write(`${usage}\ndraw_perspectives.mjs: error: ${message}\n`);
  process.exit(2);
}

function main() {
  let values;
  try {
    ({ values } = parseArgs({
      options: {
        "own-perspective": { type: "string" },
        count: { type: "string", default: "3" },
        seed: { type: "string" },
        pool: { type: "string" },
        "expected-pool-sha256": { type: "string" },
      },
    }));
  } catch (error) {
    fail(error.message);
  }
  if (values["own-perspective"] === undefined) fail("the following arguments are required: --own-perspective");
  if (!/^\s*[-+]?\d+\s*$/.test(values.count)) fail(`argument --count: invalid int value: '${values.count}'`);
  const count = Number.parseInt(values.count, 10);
  const here = dirname(fileURLToPath(import.meta.url));
  const poolPath = values.pool ? resolve(values.pool) : resolve(here, "..", "references", "perspective-pool.json");
  const poolBytes = readFileSync(poolPath);
  const poolFingerprint = createHash("sha256").update(poolBytes).digest("hex");
  if (values.seed !== undefined && !values["expected-pool-sha256"]) {
    fail("Replay requires --expected-pool-sha256 from the original receipt.");
  }
  if (values["expected-pool-sha256"] && poolFingerprint !== values["expected-pool-sha256"]) {
    fail("Pool fingerprint differs from the receipt; choose the matching archived pool.");
  }
  const pool = JSON.parse(poolBytes.toString("utf8"));
  const families = pool.families;
  const minimum = pool.minimum_pool_perspectives;
  const identifiers = families.map((family) => family.id);
  if (minimum < 3 || new Set(identifiers).size !== identifiers.length) {
    fail("Pool must require at least three perspectives and contain unique family IDs.");
  }
  if (!(minimum <= count && count <= families.length)) fail(`Count must be between ${minimum} and ${families.length}.`);
  if (!values["own-perspective"].trim()) fail("Declare the orchestrator's own perspective before drawing.");
  const seed = values.seed !== undefined ? values.seed : randomBytes(32).toString("hex");
  if (!seed.trim()) fail("Replay seed cannot be empty.");

  // Hash ranking gives a stable ordering for replay, independent of pool order.
  const rank = (family) => createHash("sha256").update(`${seed}\0${family.id}`, "utf8").digest();
  const ranked = families.map((family) => ({ family, key: rank(family) }));
  ranked.sort((a, b) => Buffer.compare(a.key, b.key) || (a.family.id < b.family.id ? -1 : a.family.id > b.family.id ? 1 : 0));
  const selected = ranked.slice(0, count).map((entry) => entry.family);
  const receipt = {
    algorithm: "sha256-rank-v1",
    seed,
    replay: values.seed !== undefined,
    pool_version: pool.version,
    pool_sha256: poolFingerprint,
    pool_size: families.length,
    minimum_pool_perspectives: minimum,
    orchestrator_perspective: values["own-perspective"],
    selected_count: selected.length,
    selected_families: selected,
    limitation:
      "A draw limits discretionary selection within this pool; it does not establish completeness, independent beliefs, or sound conclusions.",
  };
  // Match Python's json.dumps(indent=2, ensure_ascii=True).
  const text = JSON.stringify(receipt, null, 2).replace(
    /[\u0080-\uffff]/g,
    (character) => "\\u" + character.charCodeAt(0).toString(16).padStart(4, "0"),
  );
  process.stdout.write(text + "\n");
}

main();
