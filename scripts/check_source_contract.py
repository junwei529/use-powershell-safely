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
PUBLIC_RELEASE_CANDIDATE = ROOT / "release" / "v0.3.0-public-release-candidate.json"
PUBLIC_RELEASE_EVIDENCE = ROOT / "release" / "v0.3.0-public-release-evidence.json"
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


def package_digest(files):
    records = []
    for relative in sorted(files):
        raw = (PACKAGE / relative).read_bytes()
        records.append([relative, hashlib.sha256(raw).hexdigest()])
    encoded = json.dumps(records, separators=(",", ":"), ensure_ascii=True).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


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

    public_candidate_error = None
    public_candidate = {}
    release_notes_sha256 = None
    try:
        parsed_public_candidate = json.loads(
            PUBLIC_RELEASE_CANDIDATE.read_text(encoding="utf-8")
        )
        if not isinstance(parsed_public_candidate, dict):
            raise ValueError("public release candidate must be an object")
        for field in ("github_release", "lineage", "package", "public_repository"):
            if not isinstance(parsed_public_candidate.get(field), dict):
                raise ValueError(f"public release candidate field {field!r} must be an object")
        release_notes_sha256 = hashlib.sha256((ROOT / "CHANGELOG.md").read_bytes()).hexdigest()
        public_candidate = parsed_public_candidate
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        public_candidate_error = str(error)
    checks["public_release_candidate.identity"] = (
        public_candidate.get("schema")
        == "use-powershell-safely-public-release-candidate/v1"
        and "commit" not in public_candidate
        and public_candidate.get("product") == "use-powershell-safely"
        and public_candidate.get("version") == "0.3.0"
        and public_candidate.get("public_release_state") == "PENDING_HUMAN_APPROVAL"
        and public_candidate.get("human_release_notes_review") == "PENDING"
        and public_candidate.get("release_title") == "Use PowerShell Safely v0.3.0"
        and public_candidate.get("release_notes") == "CHANGELOG.md"
        and public_candidate.get("release_notes_sha256") == release_notes_sha256
        and public_candidate.get("tag") == "v0.3.0"
        and public_candidate.get("tag_type") == "annotated"
        and public_candidate.get("github_release")
        == {"draft": False, "prerelease": False}
        and public_candidate.get("lineage", {}).get("local_release_receipt")
        == "release/v0.3.0-local-release-receipt.json"
        and public_candidate.get("lineage", {}).get("local_release_receipt_commit")
        == "be782206fb12fd68874ba1e1846787530bb15159"
        and public_candidate.get("package", {}).get("path")
        == "skills/use-powershell-safely"
        and public_candidate.get("package", {}).get("tree") == package_tree
        and public_candidate.get("package", {}).get("sha256")
        == (package_digest(actual_files) if actual_files == EXPECTED_FILES else None)
        and public_candidate.get("public_repository", {}).get("full_name")
        == "junwei529/use-powershell-safely"
        and public_candidate.get("public_repository", {}).get("url")
        == "https://github.com/junwei529/use-powershell-safely"
        and public_candidate.get("public_repository", {}).get("default_branch") == "main"
        and public_candidate.get("public_repository", {}).get("visibility") == "public"
    )

    public_evidence_error = None
    public_evidence = {}
    try:
        parsed_public_evidence = json.loads(
            PUBLIC_RELEASE_EVIDENCE.read_text(encoding="utf-8")
        )
        if not isinstance(parsed_public_evidence, dict):
            raise ValueError("public release evidence must be an object")
        for field in (
            "evidence_states",
            "github_release",
            "installed_copy_behavior",
            "planner_acceptance",
            "persistent_lifecycle",
            "public_source",
            "tag",
        ):
            if not isinstance(parsed_public_evidence.get(field), dict):
                raise ValueError(f"public release evidence field {field!r} must be an object")
        if not isinstance(
            parsed_public_evidence.get("installed_copy_behavior", {}).get("evidence"),
            list,
        ):
            raise ValueError("installed-copy evidence must be an array")
        if not isinstance(
            parsed_public_evidence.get("persistent_lifecycle", {}).get("operations"),
            list,
        ):
            raise ValueError("persistent-lifecycle operations must be an array")
        public_evidence = parsed_public_evidence
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, ValueError) as error:
        public_evidence_error = str(error)

    public_states = public_evidence.get("evidence_states", {})
    public_source = public_evidence.get("public_source", {})
    public_tag = public_evidence.get("tag", {})
    github_release = public_evidence.get("github_release", {})
    persistent_lifecycle = public_evidence.get("persistent_lifecycle", {})
    installed_copy = public_evidence.get("installed_copy_behavior", {})
    expected_package_hashes = {
        relative: sha256(raw_files[relative]) for relative in sorted(raw_files)
    }
    checks["public_release_evidence.identity_and_limits"] = (
        public_evidence.get("schema")
        == "use-powershell-safely-public-release-evidence/v1"
        and public_evidence.get("product") == "use-powershell-safely"
        and public_evidence.get("version") == "0.3.0"
        and public_evidence.get("evidence_state") == "VERIFIED"
        and public_evidence.get("planner_acceptance")
        == {
            "evidence_id": "B2-PS-PUBLIC-EVIDENCE-F-01",
            "package_tree": package_tree,
            "subject_commit": "21eca7724a84b4073c98c68e548b1816c52a0ff0",
            "subject_tree": "a53e693d29d33dddd6bb673ba3f54a2fcedbfe54",
            "verdict": "ACCEPTED",
        }
        and public_evidence.get("release_notes_human_approval") == "VERIFIED"
        and public_source
        == {
            "commit": "13edb84cd1b072cb64926c5ae600714c6f7203e7",
            "package_sha256": "8c4bbdb586d69655e19f9e087cf1f9905c4e55c0b308debb64d3c60a369f8d8d",
            "package_tree": package_tree,
            "repository": "junwei529/use-powershell-safely",
            "tree": "6f03b9a5717f823f87d117fc17b5040e0531dcc8",
        }
        and public_tag
        == {
            "annotation": "Use PowerShell Safely v0.3.0",
            "name": "v0.3.0",
            "object": "58cd1276ad43589c93489c919c285ce7fec2d42d",
            "peeled_commit": "13edb84cd1b072cb64926c5ae600714c6f7203e7",
            "type": "annotated",
        }
        and github_release
        == {
            "body_normalized_lf_sha256": "5c8c787136fd490aebd3b465e8687f59a68863da8d14bd62a92ee624f78b764f",
            "draft": False,
            "id": 378386983,
            "prerelease": False,
            "published_at": "2026-08-28T09:41:46Z",
            "title": "Use PowerShell Safely v0.3.0",
            "url": "https://github.com/junwei529/use-powershell-safely/releases/tag/v0.3.0",
        }
        and persistent_lifecycle
        == {
            "cross_version_update_rollback": "UNKNOWN",
            "final_package_sha256": "4e65bac004d683f7b853082314daf209ad1e9b06d3d8065409629a5c2b9686f5",
            "final_package_tree": package_tree,
            "final_receipt_sha256": "640a38a072c02ed8e8a1bd7c6bb256c7dd709e0b16ebca033a16a92a18eed659",
            "final_state": "MANAGED",
            "legacy_copy_discovery_state": "PRESERVED_OUTSIDE_SKILL_DISCOVERY_ROOT",
            "legacy_copy_retained": True,
            "operations": [
                "install",
                "same-version update",
                "same-version rollback",
                "origin-aware uninstall",
                "public-source restoration",
            ],
            "source_identity": "junwei529/use-powershell-safely",
            "source_ref": "v0.3.0",
            "version": "0.3.0",
        }
        and installed_copy.get("evidence")
        == [
            {
                "evidence_id": "B2-PS-ABSENCE-01",
                "result": "ACCEPTED",
                "scope": "fresh projectless origin-aware absence after managed uninstall",
            },
            {
                "evidence_id": "B2-PS-LOAD-01",
                "result": "ACCEPTED",
                "scope": "fresh projectless sole-discovery loaded-copy identity and bounded three-scenario behavior",
            },
        ]
        and installed_copy.get("package_file_sha256") == expected_package_hashes
        and installed_copy.get("package_tree") == package_tree
        and installed_copy.get("receipt_sha256")
        == "640a38a072c02ed8e8a1bd7c6bb256c7dd709e0b16ebca033a16a92a18eed659"
        and public_states
        == {
            "broad_product_efficacy": "UNKNOWN",
            "cross_harness_behavior": "UNKNOWN",
            "cross_version_lifecycle": "UNKNOWN",
            "immutable_public_source": "VERIFIED",
            "installed_copy_behavior": "VERIFIED_BOUNDED",
            "live_wsl": "UNKNOWN",
            "local_release_ready": "VERIFIED",
            "persistent_same_version_lifecycle": "VERIFIED",
            "public_release": "VERIFIED",
            "sole_installed_copy_discovery": "VERIFIED",
            "stable_installed_copy": "VERIFIED",
            "untested_contexts": "UNKNOWN",
        }
    )
    failures.extend(name for name, passed in checks.items() if not passed)
    if receipt_error:
        failures.append(f"receipt.unreadable: {receipt_error}")
    if public_candidate_error:
        failures.append(f"public_release_candidate.unreadable: {public_candidate_error}")
    if public_evidence_error:
        failures.append(f"public_release_evidence.unreadable: {public_evidence_error}")
    package_hashes = {
        relative: sha256(raw_files[relative])
        for relative in sorted(raw_files)
    }
    result = {
        "checks": checks,
        "failures": failures,
        "package_files": package_hashes,
        "package_sha256": package_digest(actual_files) if actual_files == EXPECTED_FILES else None,
        "package_tree": package_tree,
        "proof_class": "deterministic-source-contract",
        "result": "PASS" if not failures else "FAIL",
        "scope_limits": [
            "this deterministic checker executes no model and transmits no source",
            "Q04 proves only bounded SOURCE-forward behavior for three frozen scenarios",
            "public evidence receipt binds retained publication, same-version lifecycle, and projectless witness results without replaying them",
            "cross-version lifecycle remains UNKNOWN",
            "no live WSL or cross-Harness proof",
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
