#!/usr/bin/env python3
import argparse
import hashlib
import json
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills" / "use-powershell-safely"
CANDIDATE = ROOT / "release" / "v0.3.0-candidate.json"
RECEIPT = ROOT / "release" / "v0.3.0-local-release-receipt.json"
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
    receipt_error = None
    receipt = {}
    try:
        parsed_receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
        if not isinstance(parsed_receipt, dict):
            raise ValueError("local release receipt must be an object")
        for field in (
            "candidate",
            "evidence_states",
            "planner_acceptance",
            "source_forward_behavior",
        ):
            if not isinstance(parsed_receipt.get(field), dict):
                raise ValueError(f"local release receipt field {field!r} must be an object")
        if not isinstance(parsed_receipt.get("sealed_qualification_history"), list):
            raise ValueError("sealed_qualification_history must be an array")
        receipt = parsed_receipt
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        receipt_error = str(error)

    evidence_states = receipt.get("evidence_states", {})
    source_forward = receipt.get("source_forward_behavior", {})
    checks["receipt.identity_readiness_and_bounded_source"] = (
        receipt.get("schema") == "use-powershell-safely-local-release-receipt/v1"
        and receipt.get("product") == "use-powershell-safely"
        and receipt.get("version") == "0.3.0"
        and receipt.get("candidate", {}).get("commit")
        == "ad8f056b110ee3798a5f92ed9715c1085e45fe72"
        and receipt.get("candidate", {}).get("descriptor")
        == "release/v0.3.0-candidate.json"
        and receipt.get("candidate", {}).get("tree")
        == "4a2597202b89b91c330e559f86d04fc288894bea"
        and receipt.get("candidate", {}).get("package_tree") == package_tree
        and receipt.get("planner_acceptance", {}).get("evidence_id") == "Q04"
        and receipt.get("planner_acceptance", {}).get("verdict") == "ACCEPTED"
        and evidence_states.get("local_release_ready") == "VERIFIED"
        and evidence_states.get("source_forward_model_behavior")
        == "VERIFIED_BOUNDED_SOURCE"
        and all(
            evidence_states.get(field) == "UNKNOWN"
            for field in (
                "broad_product_efficacy",
                "installed_copy_behavior",
                "live_wsl",
                "persistent_lifecycle",
                "public_release",
                "selection_load_attribution",
                "stable_installed_copy",
            )
        )
        and receipt.get("human_release_notes_review") == "PENDING"
        and receipt.get("sealed_qualification_history")
        == [
            {
                "behavior_result": "UNKNOWN_NOT_ASSESSED",
                "evidence_id": "Q01",
                "result": "QUALIFICATION_FAILED/TRANSPORT_TERMINAL",
            },
            {
                "behavior_result": "UNKNOWN_NOT_ASSESSED",
                "evidence_id": "Q02",
                "result": "ESCALATION_DENIED",
            },
            {
                "behavior_result": "UNKNOWN_NOT_ASSESSED",
                "evidence_id": "Q03",
                "result": "PREFLIGHT_STOP/NO_SOURCE_TRANSMISSION",
            },
        ]
        and source_forward.get("evidence_id") == "Q04"
        and source_forward.get("model") == "gpt-5.6-sol"
        and source_forward.get("reasoning_effort") == "high"
        and source_forward.get("result") == "ACCEPTED"
        and source_forward.get("scope")
        == "fresh projectless read-only no-tool exact-SOURCE three-scenario"
        and source_forward.get("package_tree") == package_tree
        and source_forward.get("request_payload_sha256")
        == "cfa75604ca5dbf49f6f5f7452e9c9dfe6eb927981ac6028c08d9dd7b602f538c"
        and source_forward.get("controller_rubric_sha256")
        == "63621cb8c6d2e625b8fbeabbe51ea007bc828ce0bb05c7a32cc2dbae506273f8"
        and source_forward.get("response_sha256")
        == "8fba2576f76755e77d848574b60e19b2276d378e5e5de46027b9dcd97774c085"
        and source_forward.get("task_turns") == 1
        and source_forward.get("reasoning_records") == 2
        and source_forward.get("final_messages") == 1
        and source_forward.get("tool_events") == 0
    )
    failures.extend(name for name, passed in checks.items() if not passed)
    if receipt_error:
        failures.append(f"receipt.unreadable: {receipt_error}")
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
            "this deterministic checker executes no model and transmits no source",
            "Q04 proves only bounded SOURCE-forward behavior for three frozen scenarios",
            "no persistent install, update, rollback, or uninstall",
            "no stable installed-copy or loaded-copy proof",
            "no selection/load attribution or live WSL proof",
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
