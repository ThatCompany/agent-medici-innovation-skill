"""Build deterministic edition archives and checksums without external services."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]


def write_archive(target, entries):
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, source in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    with zipfile.ZipFile(target) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(entries)
        for name, source in entries.items():
            assert archive.read(name) == source.read_bytes()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--edition", required=True)
    parser.add_argument("--version", required=True)
    args = parser.parse_args()
    assert re.fullmatch(r"[a-z][a-z0-9-]*", args.edition), "Invalid edition name"
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-z0-9.-]+)?", args.version), "Invalid version"
    edition = ROOT / "editions" / args.edition
    skill = edition / "skills/medici-exploration"
    assert (skill / "SKILL.md").is_file(), "Edition has no skill"
    license_path = ROOT / "LICENSE"
    assert license_path.is_file(), "Include the repository license in distributions"
    files = {path.relative_to(skill).as_posix(): path for path in skill.rglob("*")
             if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"}
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    standalone = output / f"medici-exploration-{args.edition}-v{args.version}.zip"
    standalone_entries = {"medici-exploration/" + name: path for name, path in files.items()}
    standalone_entries["medici-exploration/LICENSE"] = license_path
    write_archive(standalone, standalone_entries)
    built = [standalone]

    manifest_path = edition / "plugin.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        assert manifest["version"] == args.version, "Manifest version mismatch"
        assert manifest["license"] == "MIT"
        plugin = output / f"{manifest['name']}-openai-v{args.version}.zip"
        plugin_entries = {"skills/medici-exploration/" + name: path for name, path in files.items()}
        plugin_entries.update({"plugin.json": manifest_path, "LICENSE": license_path})
        write_archive(plugin, plugin_entries)
        built.append(plugin)

    claude_manifest_path = edition / ".claude-plugin/plugin.json"
    if claude_manifest_path.is_file():
        manifest = json.loads(claude_manifest_path.read_text(encoding="utf-8"))
        assert manifest["version"] == args.version, "Claude plugin manifest version mismatch"
        assert manifest["license"] == "MIT"
        root = manifest["name"] + "/"
        plugin = output / f"{manifest['name']}-claude-plugin-v{args.version}.zip"
        plugin_entries = {root + path.relative_to(edition).as_posix(): path for path in edition.rglob("*")
                          if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"}
        plugin_entries[root + "LICENSE"] = license_path
        write_archive(plugin, plugin_entries)
        built.append(plugin)

    checksums = output / "SHA256SUMS.txt"
    # Write bytes so Windows text mode cannot turn the LF line endings into CRLF.
    checksums.write_bytes("".join(
        hashlib.sha256(path.read_bytes()).hexdigest() + "  " + path.name + "\n"
        for path in built
    ).encode("utf-8"))
    print(json.dumps({"archives": [path.name for path in built],
                      "checksums": checksums.name,
                      "archive_bytes_match_sources": True}, indent=2))


if __name__ == "__main__":
    main()
