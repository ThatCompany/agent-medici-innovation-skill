"""Draw standing-pool perspectives and emit a replayable JSON receipt."""

import argparse
import hashlib
import json
from pathlib import Path
import secrets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--own-perspective", required=True)
    parser.add_argument("--count", type=int, default=3)
    parser.add_argument("--seed", help="Replay a recorded receipt; omit for a fresh draw.")
    parser.add_argument("--pool", type=Path, help="Use an archived pool when replaying an earlier version.")
    parser.add_argument("--expected-pool-sha256", help="Required for replay; use the fingerprint in the original receipt.")
    args = parser.parse_args()
    pool_path = args.pool or Path(__file__).resolve().parents[1] / "references" / "perspective-pool.json"
    pool_bytes = pool_path.read_bytes()
    pool_fingerprint = hashlib.sha256(pool_bytes).hexdigest()
    if args.seed is not None and not args.expected_pool_sha256:
        parser.error("Replay requires --expected-pool-sha256 from the original receipt.")
    if args.expected_pool_sha256 and pool_fingerprint != args.expected_pool_sha256:
        parser.error("Pool fingerprint differs from the receipt; choose the matching archived pool.")
    pool = json.loads(pool_bytes)
    families = pool["families"]
    minimum = pool["minimum_pool_perspectives"]
    identifiers = [family["id"] for family in families]
    if minimum < 3 or len(set(identifiers)) != len(identifiers):
        parser.error("Pool must require at least three perspectives and contain unique family IDs.")
    if not minimum <= args.count <= len(families):
        parser.error(f"Count must be between {minimum} and {len(families)}.")
    if not args.own_perspective.strip():
        parser.error("Declare the orchestrator's own perspective before drawing.")
    seed = args.seed if args.seed is not None else secrets.token_hex(32)
    if not seed.strip():
        parser.error("Replay seed cannot be empty.")

    # Hash ranking gives a stable ordering for replay, independent of pool order.
    def rank(family):
        return hashlib.sha256((seed + "\0" + family["id"]).encode("utf-8")).digest(), family["id"]

    selected = sorted(families, key=rank)[: args.count]
    receipt = {
        "algorithm": "sha256-rank-v1",
        "seed": seed,
        "replay": args.seed is not None,
        "pool_version": pool["version"],
        "pool_sha256": pool_fingerprint,
        "pool_size": len(families),
        "minimum_pool_perspectives": minimum,
        "orchestrator_perspective": args.own_perspective,
        "selected_count": len(selected),
        "selected_families": selected,
        "limitation": "A draw limits discretionary selection within this pool; it does not establish completeness, independent beliefs, or sound conclusions.",
    }
    print(json.dumps(receipt, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
