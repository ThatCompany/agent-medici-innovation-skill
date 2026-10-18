"""Run local package sanity checks; this is not the official skill validator."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
EDITION = ROOT / "editions/codex"
SKILL = EDITION / "skills/medici-exploration"


def main():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    assert match, "Missing or malformed frontmatter"
    metadata = yaml.safe_load(match.group(1))
    assert isinstance(metadata, dict)
    assert metadata["name"] == "medici-exploration"
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["name"])
    assert len(metadata["name"]) <= 64
    assert isinstance(metadata["description"], str)
    assert 0 < len(metadata["description"]) <= 1024

    expected = json.loads((ROOT / "tests/recorded-results.json").read_text())
    for name, fingerprint in expected["skill_files"].items():
        assert hashlib.sha256((SKILL / name).read_bytes()).hexdigest() == fingerprint, (
            "Skill differs from recorded validated edition: " + name
        )

    for path in SKILL.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            assert (path.parent / target.split("#", 1)[0]).is_file(), (path, target)

    for path in SKILL.rglob("*.py"):
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    replay = json.loads((ROOT / "tests/draw-replay.json").read_text())
    command = [
        sys.executable, str(SKILL / "scripts/draw_perspectives.py"),
        "--own-perspective", replay["own_perspective"],
        "--count", str(replay["count"]), "--seed", replay["seed"],
        "--expected-pool-sha256", replay["pool_sha256"],
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    receipt = json.loads(result.stdout)
    assert [item["id"] for item in receipt["selected_families"]] == replay["selected_family_ids"]

    manifest = json.loads((EDITION / "plugin.json").read_text())
    assert manifest["version"] == expected["version"]
    assert manifest["license"] == "MIT"
    assert (ROOT / "LICENSE").is_file()

    fixtures = json.loads((ROOT / "tests/cases.json").read_text())
    output = json.loads((ROOT / "tests/recorded-codex-output.json").read_text())
    observed = {case["case_id"]: case for case in output["cases"]}
    for case in fixtures["cases"]:
        actual = observed[case["case_id"]]
        assert actual["authored_notes"] == case["saved_state"]["authored_notes"]
        for question in case["saved_state"]["submitted_user_questions"]:
            controls = [item for item in actual["question_controls"]
                        if item["author"] == question["author"]
                        and item["question"] == question["question"]]
            assert len(controls) == 1
            assert controls[0]["options"] == question["options"]
            assert controls[0]["free_text"] is True
            assert controls[0]["answer_required"] == question["answer_required"]

    print(json.dumps({
        "package_sanity": "passed",
        "validated_bundle_fingerprints": "matched",
        "local_references": "passed",
        "helper_replay": "passed",
        "recorded_submissions": "preserved",
        "scope": "Mechanical packaging checks; no new behavioral or efficacy run.",
    }, indent=2))


if __name__ == "__main__":
    main()
