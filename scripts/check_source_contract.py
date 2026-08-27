#!/usr/bin/env python3
import argparse
import hashlib
import json
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "use-powershell-safely"
CANDIDATE = ROOT / "release" / "v0.3.0-candidate.json"
EXPECTED_FILES = {
    "SKILL.md",
    "agents/openai.yaml",
    "references/native-process-boundaries.md",
    "references/text-encoding-boundaries.md",
    "references/windows-wsl-boundaries.md",
}


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def git_object_hash(kind, raw):
    header = f"{kind} {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def is_link_like(path):
    if path.is_symlink():
        return True
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
    except OSError:
        return False
    return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def package_entries(root):
    if is_link_like(root):
        raise ValueError(f"package root is link-like: {root}")
    entries = []
    pending = [root]
    while pending:
        current = pending.pop()
        for child in current.iterdir():
            if is_link_like(child):
                raise ValueError(f"package entry is link-like: {child}")
            entries.append(child)
            if child.is_dir():
                pending.append(child)
    return entries


def git_tree_hash(directory):
    children = sorted(
        directory.iterdir(),
        key=lambda child: (child.name + ("/" if child.is_dir() else "")).encode("utf-8"),
    )
    records = []
    for child in children:
        if is_link_like(child):
            raise ValueError(f"package entry is link-like: {child}")
        if child.is_dir():
            mode = b"40000"
            digest = bytes.fromhex(git_tree_hash(child))
        elif child.is_file():
            mode = b"100644"
            digest = bytes.fromhex(git_object_hash("blob", child.read_bytes()))
        else:
            raise ValueError(f"unsupported package entry: {child}")
        records.append(mode + b" " + child.name.encode("utf-8") + b"\0" + digest)
    return git_object_hash("tree", b"".join(records))


def contains_all(text, fragments):
    normalized = " ".join(text.split())
    return all(" ".join(fragment.split()) in normalized for fragment in fragments)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    failures = []
    try:
        entries = package_entries(PACKAGE)
    except (OSError, ValueError) as error:
        entries = []
        failures.append(f"package.scan: {error}")
    actual_files = {
        path.relative_to(PACKAGE).as_posix()
        for path in entries
        if path.is_file()
    }
    raw_files = {}
    texts = {}
    for relative in sorted(EXPECTED_FILES & actual_files):
        try:
            raw = (PACKAGE / relative).read_bytes()
            raw_files[relative] = raw
            texts[relative] = raw.decode("utf-8")
        except (OSError, UnicodeDecodeError) as error:
            failures.append(f"package.unreadable.{relative}: {error}")

    skill = texts.get("SKILL.md", "")
    metadata = texts.get("agents/openai.yaml", "")
    native = texts.get("references/native-process-boundaries.md", "")
    encoding = texts.get("references/text-encoding-boundaries.md", "")
    wsl = texts.get("references/windows-wsl-boundaries.md", "")

    try:
        candidate = json.loads(CANDIDATE.read_text(encoding="utf-8"))
        if not isinstance(candidate, dict) or not isinstance(candidate.get("package"), dict):
            raise ValueError("candidate descriptor must be an object with an object package")
        package_tree = git_tree_hash(PACKAGE)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        candidate = {}
        package_tree = None
        failures.append(f"candidate.unreadable: {error}")

    text_bytes_valid = all(
        not raw.startswith(b"\xef\xbb\xbf")
        and b"\r" not in raw
        and raw.endswith(b"\n")
        and not raw.endswith(b"\n\n")
        for raw in raw_files.values()
    )
    checks = {
        "package.exact_five_file_shape": actual_files == EXPECTED_FILES,
        "package.strict_utf8_lf_no_bom": len(raw_files) == 5 and text_bytes_valid,
        "candidate.identity": (
            candidate.get("schema") == "use-powershell-safely-local-release-candidate/v1"
            and candidate.get("product") == "use-powershell-safely"
            and candidate.get("public_identity") == "junwei529/use-powershell-safely"
            and candidate.get("version") == "0.3.0"
            and candidate.get("candidate_state") == "PENDING_PLANNER_ACCEPTANCE"
            and candidate.get("human_release_notes_review") == "PENDING"
            and candidate.get("package", {}).get("path") == "skills/use-powershell-safely"
            and candidate.get("package", {}).get("file_count") == 5
            and candidate.get("package", {}).get("tree") == package_tree
        ),
        "selection.pre_error_positive_and_narrow_negatives": contains_all(
            skill + "\n" + metadata,
            [
                "before the first relevant command",
                "destructive filesystem",
                "ordinary version-independent cmdlet",
                "simple documented native call with no boundary symptom",
                "general Windows work",
                "POSIX-only work",
            ],
        ),
        "command.readiness_and_authority": contains_all(
            skill,
            [
                "parse the exact payload without executing it",
                "New-Item` exposes `-Path`, not `-LiteralPath`",
                "$LASTEXITCODE` belongs to a native process contract",
                "Detection alone never authorizes installation",
            ],
        ),
        "native.identity_arguments_streams_and_exit": contains_all(
            native,
            [
                "Multiple application candidates require an explicit selection rule.",
                "one array item per argument",
                "Capture stdout and stderr separately when their distinction matters.",
                "Save `$LASTEXITCODE` before another native command",
                "ProcessStartInfo.ArgumentList",
            ],
        ),
        "native.permission_and_destructive_boundaries": contains_all(
            native,
            [
                "Before recursive delete, move, or overwrite",
                "prove it stays under the intended root",
                "Junction",
                "never broaden this fallback to recursive deletion",
                "Installing tools, changing profiles or policy",
            ],
        ),
        "text.encoding_hash_and_cross_shell_contract": contains_all(
            encoding,
            [
                "Preserve the original bytes.",
                "Distinguish a semantic text hash from a raw byte hash.",
                "UTF-8 without BOM",
                "newline sequence",
                "Do not use PowerShell text cmdlets to write images, archives, executables",
            ],
        ),
        "wsl.cardinality_identity_exit_and_state_gate": contains_all(
            wsl,
            [
                "$wslCandidates.Count -eq 0",
                "$wslCandidates.Count -gt 1",
                "$wslExitCode = [int]$LASTEXITCODE",
                "Windows elevation does not equal Linux `root`",
                "requiring explicit authorization",
            ],
        ),
    }
    failures.extend(name for name, passed in checks.items() if not passed)
    package_hashes = {
        relative: sha256(raw_files[relative])
        for relative in sorted(raw_files)
    }
    result = {
        "checks": checks,
        "failures": failures,
        "package_files": package_hashes,
        "package_tree": package_tree,
        "proof_class": "deterministic-source-contract",
        "result": "PASS" if not failures else "FAIL",
        "scope_limits": [
            "no model execution or source transmission",
            "no persistent install, update, rollback, or uninstall",
            "no stable installed-copy or loaded-copy proof",
            "no publication proof",
            "no broad product efficacy proof",
        ],
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"use-powershell-safely SOURCE contract: {result['result']}")
        for failure in failures:
            print(f"- {failure}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
