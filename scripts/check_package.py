"""Run local package sanity checks; this is not the official skill validator."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
CODEX = ROOT / "editions/codex"
SKILL_PATH = "skills/medici-exploration"
# Claude-only files; every other skill file must match the Codex edition byte for byte.
CLAUDE_ONLY = {"SKILL.md", "references/claude-hosts.md", "scripts/draw_perspectives.mjs"}
CLAUDE_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}


def skill_files(skill):
    return {path.relative_to(skill).as_posix() for path in skill.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", choices=["codex", "claude"], default="codex")
    edition_name = parser.parse_args().edition
    edition = ROOT / "editions" / edition_name
    skill = edition / SKILL_PATH
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    assert match, "Missing or malformed frontmatter"
    metadata = yaml.safe_load(match.group(1))
    assert isinstance(metadata, dict)
    assert metadata["name"] == "medici-exploration"
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", metadata["name"])
    assert len(metadata["name"]) <= 64
    assert isinstance(metadata["description"], str)
    assert 0 < len(metadata["description"]) <= 1024
    if edition_name == "claude":
        assert set(metadata) <= CLAUDE_FRONTMATTER, "Claude.ai uploads reject other frontmatter keys"
        assert len(metadata["description"]) <= 200, "Claude.ai help pages cap descriptions at 200 characters"
        assert len(metadata.get("compatibility", "")) <= 500
        codex_skill = CODEX / SKILL_PATH
        shared = skill_files(skill) - CLAUDE_ONLY
        assert shared == skill_files(codex_skill) - {"SKILL.md"}, "Claude edition shared file set differs"
        for name in shared:
            assert (skill / name).read_bytes() == (codex_skill / name).read_bytes(), (
                "Shared method file differs from the Codex edition: " + name
            )

    results = "recorded-results.json" if edition_name == "codex" else "claude-recorded-results.json"
    expected = json.loads((ROOT / "tests" / results).read_text())
    assert set(expected["skill_files"]) == skill_files(skill), "Recorded fingerprints do not cover the skill"
    for name, fingerprint in expected["skill_files"].items():
        assert hashlib.sha256((skill / name).read_bytes()).hexdigest() == fingerprint, (
            "Skill differs from recorded validated edition: " + name
        )

    for path in skill.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            assert (path.parent / target.split("#", 1)[0]).is_file(), (path, target)

    for path in skill.rglob("*.py"):
        compile(path.read_text(encoding="utf-8"), str(path), "exec")

    replay = json.loads((ROOT / "tests/draw-replay.json").read_text())
    helpers = {"python": [sys.executable, str(skill / "scripts/draw_perspectives.py")]}
    if (skill / "scripts/draw_perspectives.mjs").is_file():
        node = shutil.which("node")
        assert node, "Node.js is needed to check the Node draw helper"
        helpers["node"] = [node, str(skill / "scripts/draw_perspectives.mjs")]
    receipts = []
    for helper in helpers.values():
        command = helper + [
            "--own-perspective", replay["own_perspective"],
            "--count", str(replay["count"]), "--seed", replay["seed"],
            "--expected-pool-sha256", replay["pool_sha256"],
        ]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        receipts.append(json.loads(result.stdout))
        assert [item["id"] for item in receipts[-1]["selected_families"]] == replay["selected_family_ids"]
    assert all(receipt == receipts[0] for receipt in receipts), "Draw helpers produced different receipts"

    manifest_path = edition / ("plugin.json" if edition_name == "codex" else ".claude-plugin/plugin.json")
    manifest = json.loads(manifest_path.read_text())
    assert manifest["version"] == expected["version"]
    assert manifest["license"] == "MIT"
    assert (ROOT / "LICENSE").is_file()
    if edition_name == "claude":
        for marketplace_root, source in ((ROOT, "./editions/claude"), (edition, "./")):
            marketplace = json.loads((marketplace_root / ".claude-plugin/marketplace.json").read_text())
            entries = [item for item in marketplace["plugins"] if item["name"] == manifest["name"]]
            assert len(entries) == 1, marketplace_root
            assert entries[0]["source"] == source
            assert entries[0]["version"] == manifest["version"]

    if edition_name == "codex":
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

    report = {
        "edition": edition_name,
        "package_sanity": "passed",
        "validated_bundle_fingerprints": "matched",
        "local_references": "passed",
        "helper_replay": "passed (" + ", ".join(helpers) + ")",
    }
    if edition_name == "codex":
        report["recorded_submissions"] = "preserved"
    else:
        report["shared_method_files"] = "identical to Codex edition"
        report["marketplaces"] = "consistent"
    report["scope"] = "Mechanical packaging checks; no new behavioral or efficacy run."
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
