#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import shutil
import stat
import tempfile
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCT = "use-powershell-safely"
PUBLIC_IDENTITY = "junwei529/use-powershell-safely"
RECEIPT_NAME = ".use-powershell-safely-install.json"
RECEIPT_SCHEMA = "use-powershell-safely-install-receipt/v1"
CANDIDATE_SCHEMA = "use-powershell-safely-local-release-candidate/v1"
EXPECTED_FILES = {
    "SKILL.md",
    "agents/openai.yaml",
    "references/native-process-boundaries.md",
    "references/text-encoding-boundaries.md",
    "references/windows-wsl-boundaries.md",
}
EXPECTED_DIRECTORIES = {
    Path(relative).parent.as_posix()
    for relative in EXPECTED_FILES
    if Path(relative).parent.as_posix() != "."
}
TRUSTED_PACKAGE_TREES = {
    "0.3.0": "7e10775d423bfb08bc4ad6388875b7277ce3c18c",
}


class LifecycleError(RuntimeError):
    pass


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolved(path):
    return Path(path).expanduser().resolve(strict=False)


def is_link_like(path):
    if path.is_symlink():
        return True
    try:
        attributes = getattr(path.lstat(), "st_file_attributes", 0)
    except OSError:
        return False
    return bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0))


def assert_safe_destination(destination, source=None):
    if not str(destination).strip():
        raise LifecycleError("destination must not be empty")
    unresolved = Path(destination).expanduser().absolute()
    for path in (unresolved, *unresolved.parents):
        if path.exists() and is_link_like(path):
            raise LifecycleError(
                "destination or ancestor is a symbolic link, junction, or reparse point"
            )
    destination = unresolved.resolve(strict=False)
    if destination == Path(destination.anchor) or destination == Path.home().resolve():
        raise LifecycleError("destination must not be a filesystem root or home directory")
    if source is not None:
        source = resolved(source)
        if destination == source or source in destination.parents or destination in source.parents:
            raise LifecycleError("destination and source repository must not contain each other")
    return destination


def candidate_metadata(source, expected_version):
    source = resolved(source)
    path = source / "release" / f"v{expected_version}-candidate.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise LifecycleError(f"candidate descriptor is unreadable: {error}") from error
    if not isinstance(value, dict) or not isinstance(value.get("package"), dict):
        raise LifecycleError("candidate descriptor must be an object with an object package")
    tree = value.get("package", {}).get("tree")
    if (
        value.get("schema") != CANDIDATE_SCHEMA
        or value.get("product") != PRODUCT
        or value.get("public_identity") != PUBLIC_IDENTITY
        or value.get("version") != expected_version
        or not isinstance(tree, str)
        or len(tree) != 40
        or any(character not in "0123456789abcdef" for character in tree)
    ):
        raise LifecycleError("candidate descriptor identity mismatch")
    return value


def git_object_hash(kind, raw):
    header = f"{kind} {len(raw)}\0".encode("ascii")
    return hashlib.sha1(header + raw).hexdigest()


def git_tree_hash(directory, excluded_names=frozenset()):
    children = [child for child in directory.iterdir() if child.name not in excluded_names]
    children.sort(
        key=lambda child: (child.name + ("/" if child.is_dir() else "")).encode("utf-8")
    )
    records = []
    for child in children:
        if is_link_like(child):
            raise LifecycleError(f"package contains a link-like entry: {child.name}")
        if child.is_dir():
            mode = b"40000"
            digest = bytes.fromhex(git_tree_hash(child))
        elif child.is_file():
            mode = b"100644"
            digest = bytes.fromhex(git_object_hash("blob", child.read_bytes()))
        else:
            raise LifecycleError(f"package contains an unsupported path: {child.name}")
        records.append(mode + b" " + child.name.encode("utf-8") + b"\0" + digest)
    return git_object_hash("tree", b"".join(records))


def package_files(source, expected_tree):
    package = resolved(source) / "skills" / PRODUCT
    if not package.is_dir() or is_link_like(package):
        raise LifecycleError("package root is missing or link-like")
    entries = list(package.rglob("*"))
    if any(is_link_like(path) for path in entries):
        raise LifecycleError("package contains a symbolic link, junction, or reparse point")
    actual = {
        path.relative_to(package).as_posix()
        for path in entries
        if path.is_file()
    }
    if actual != EXPECTED_FILES:
        raise LifecycleError(f"package path set mismatch: {sorted(actual)}")
    tree = git_tree_hash(package)
    if tree != expected_tree:
        raise LifecycleError(f"package tree mismatch: expected {expected_tree}, got {tree}")
    return package, {relative: sha256(package / relative) for relative in sorted(actual)}, tree


def package_digest(files):
    encoded = json.dumps(files, ensure_ascii=True, sort_keys=True, separators=(",", ":")).encode(
        "ascii"
    )
    return hashlib.sha256(encoded).hexdigest()


def read_receipt(destination):
    receipt_path = destination / RECEIPT_NAME
    if not receipt_path.is_file():
        return None
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
        raise LifecycleError(f"managed receipt is unreadable: {error}") from error
    if not isinstance(receipt, dict) or not isinstance(receipt.get("destination"), str):
        raise LifecycleError("destination receipt shape mismatch")
    if (
        receipt.get("schema") != RECEIPT_SCHEMA
        or receipt.get("product") != PRODUCT
        or receipt.get("public_identity") != PUBLIC_IDENTITY
        or resolved(receipt.get("destination", "")) != destination
    ):
        raise LifecycleError("destination receipt is malformed, mismatched, or aliased")
    return receipt


def current_state(destination, trusted_tree=None):
    destination = resolved(destination)
    if not destination.exists():
        return {"state": "ABSENT"}
    if not destination.is_dir() or is_link_like(destination):
        return {"state": "FOREIGN_COPY", "reason": "destination is not an ordinary directory"}
    try:
        receipt = read_receipt(destination)
    except LifecycleError as error:
        return {"state": "DRIFTED", "reason": str(error)}
    if receipt is None:
        return {"state": "FOREIGN_COPY", "reason": "management receipt is absent"}
    expected = receipt.get("files")
    if not isinstance(expected, dict) or set(expected) != EXPECTED_FILES:
        return {"state": "DRIFTED", "reason": "receipt file set mismatch"}
    version = receipt.get("version")
    if not isinstance(version, str):
        return {"state": "DRIFTED", "reason": "receipt version is invalid"}
    trusted_tree = TRUSTED_PACKAGE_TREES.get(version) or trusted_tree
    if trusted_tree is None or receipt.get("package_tree") != trusted_tree:
        return {"state": "FOREIGN_COPY", "reason": "receipt is not bound to a trusted package tree"}
    entries = list(destination.rglob("*"))
    if any(is_link_like(path) for path in entries):
        return {"state": "DRIFTED", "reason": "managed package contains a link-like entry"}
    actual_files = {
        path.relative_to(destination).as_posix()
        for path in entries
        if path.is_file() and path.relative_to(destination).as_posix() != RECEIPT_NAME
    }
    actual_directories = {
        path.relative_to(destination).as_posix()
        for path in entries
        if path.is_dir()
    }
    if actual_files != EXPECTED_FILES or actual_directories != EXPECTED_DIRECTORIES:
        return {"state": "DRIFTED", "reason": "managed path set mismatch"}
    actual_hashes = {}
    for relative, expected_hash in expected.items():
        actual_hash = sha256(destination / relative)
        actual_hashes[relative] = actual_hash
        if actual_hash != expected_hash:
            return {"state": "DRIFTED", "reason": f"managed file changed: {relative}"}
    if receipt.get("package_sha256") != package_digest(actual_hashes):
        return {"state": "DRIFTED", "reason": "managed package digest mismatch"}
    if git_tree_hash(destination, {RECEIPT_NAME}) != trusted_tree:
        return {"state": "DRIFTED", "reason": "managed package tree mismatch"}
    return {
        "state": "MANAGED",
        "version": version,
        "package_sha256": receipt.get("package_sha256"),
        "package_tree": receipt.get("package_tree"),
    }


def write_receipt(destination, metadata, files, receipt_destination):
    receipt = {
        "destination": str(resolved(receipt_destination)),
        "files": files,
        "package_sha256": package_digest(files),
        "package_tree": metadata["package"]["tree"],
        "product": PRODUCT,
        "public_identity": PUBLIC_IDENTITY,
        "schema": RECEIPT_SCHEMA,
        "version": metadata["version"],
    }
    (destination / RECEIPT_NAME).write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def stage_source(package, files, destination, metadata):
    stage = Path(tempfile.mkdtemp(prefix=f".{destination.name}.stage-", dir=destination.parent))
    try:
        for relative in sorted(files):
            target = stage / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(package / relative, target)
        write_receipt(stage, metadata, files, destination)
        staged_tree = git_tree_hash(stage, {RECEIPT_NAME})
        if staged_tree != metadata["package"]["tree"]:
            raise LifecycleError("staged package failed tree verification")
        if any(sha256(stage / relative) != digest for relative, digest in files.items()):
            raise LifecycleError("staged package failed file verification")
        return stage
    except Exception:
        shutil.rmtree(stage, ignore_errors=True)
        raise


def synchronize(
    action,
    source,
    destination,
    expected_version,
    apply,
    trusted_current_tree=None,
    trusted_target_tree=None,
):
    source = resolved(source)
    destination = assert_safe_destination(destination, source)
    state = current_state(destination, trusted_current_tree)
    if action == "install" and state["state"] != "ABSENT":
        raise LifecycleError(f"install requires an absent destination; observed {state['state']}")
    if action in {"update", "rollback"} and state["state"] != "MANAGED":
        raise LifecycleError(f"{action} requires an unchanged managed destination; observed {state['state']}")
    metadata = candidate_metadata(source, expected_version)
    built_in_tree = TRUSTED_PACKAGE_TREES.get(expected_version)
    if built_in_tree is not None and trusted_target_tree not in (None, built_in_tree):
        raise LifecycleError("trusted target override conflicts with the built-in release tree")
    trusted_target_tree = built_in_tree or trusted_target_tree
    if trusted_target_tree is None or metadata["package"]["tree"] != trusted_target_tree:
        raise LifecycleError("source candidate is not bound to a trusted package tree")
    package, files, tree = package_files(source, trusted_target_tree)
    result = {
        "action": action,
        "destination": str(destination),
        "effect": "APPLY" if apply else "DRY_RUN",
        "source_identity": metadata["public_identity"],
        "version": metadata["version"],
        "package_tree": tree,
    }
    if not apply:
        return result
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = stage_source(package, files, destination, metadata)
    backup = destination.parent / f".{destination.name}.backup-{uuid.uuid4().hex}"
    moved_old = False
    try:
        if destination.exists():
            os.replace(destination, backup)
            moved_old = True
        os.replace(stage, destination)
        if current_state(destination, tree).get("state") != "MANAGED":
            raise LifecycleError("installed destination failed receipt verification")
    except Exception:
        if destination.exists():
            shutil.rmtree(destination, ignore_errors=True)
        if moved_old and backup.exists():
            os.replace(backup, destination)
        if stage.exists():
            shutil.rmtree(stage, ignore_errors=True)
        raise
    if moved_old:
        try:
            shutil.rmtree(backup)
        except OSError as error:
            result["backup_path"] = str(backup)
            result["cleanup_error"] = str(error)
            result["result"] = "MANAGED_WITH_BACKUP"
            return result
    result["package_sha256"] = package_digest(files)
    result["result"] = "MANAGED"
    return result


def uninstall(destination, apply, trusted_tree=None):
    destination = assert_safe_destination(destination)
    state = current_state(destination, trusted_tree)
    if state["state"] == "ABSENT":
        return {"action": "uninstall", "destination": str(destination), "result": "ALREADY_ABSENT"}
    if state["state"] != "MANAGED":
        raise LifecycleError(
            "uninstall refuses an unreceipted, wrong-tree, modified, or drifted destination; "
            f"observed {state['state']}"
        )
    result = {
        "action": "uninstall",
        "destination": str(destination),
        "effect": "APPLY" if apply else "DRY_RUN",
    }
    if not apply:
        return result
    recovery_base = destination.parent / f".{destination.name}.recovery-{uuid.uuid4().hex}"
    recovery_archive = Path(shutil.make_archive(str(recovery_base), "zip", root_dir=destination))
    tombstone = destination.parent / f".{destination.name}.remove-{uuid.uuid4().hex}"
    os.replace(destination, tombstone)
    try:
        shutil.rmtree(tombstone)
    except Exception as error:
        try:
            destination.mkdir()
            shutil.unpack_archive(recovery_archive, destination, "zip")
            if current_state(destination, trusted_tree).get("state") != "MANAGED":
                raise LifecycleError("restored destination failed receipt verification")
        except Exception as restore_error:
            raise LifecycleError(
                f"uninstall failed; recovery archive retained at {recovery_archive}; "
                f"automatic restore failed: {restore_error}"
            ) from error
        raise LifecycleError(
            f"uninstall failed and destination was restored; recovery archive retained at {recovery_archive}"
        ) from error
    try:
        recovery_archive.unlink()
    except OSError as error:
        result["warning"] = f"uninstall completed; recovery archive retained: {error}"
        result["recovery_archive"] = str(recovery_archive)
    result["result"] = "ABSENT"
    return result


def create_test_source(root, version, marker):
    source = root / f"source-{version}"
    package = source / "skills" / PRODUCT
    for relative in sorted(EXPECTED_FILES):
        path = package / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{relative} {marker}\n", encoding="utf-8", newline="\n")
    descriptor = {
        "package": {"tree": git_tree_hash(package)},
        "product": PRODUCT,
        "public_identity": PUBLIC_IDENTITY,
        "schema": CANDIDATE_SCHEMA,
        "version": version,
    }
    candidate = source / "release" / f"v{version}-candidate.json"
    candidate.parent.mkdir(parents=True)
    candidate.write_text(
        json.dumps(descriptor, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return source


def self_test(source=None, expected_version="0.3.2"):
    source_a = resolved(source) if source is not None else ROOT
    # Self-test subjects are explicit accepted trees, not trust derived from
    # the candidate being tested. Production install trust is unchanged.
    test_trees = {
        "0.3.0": TRUSTED_PACKAGE_TREES["0.3.0"],
        "0.3.2": "f76f6deaec88101ecdda4c5dbc47405d8b930a65",
    }
    if expected_version not in test_trees:
        raise LifecycleError("unsupported self-test source version")
    metadata_a = candidate_metadata(source_a, expected_version)
    _, _, tree_a = package_files(source_a, metadata_a["package"]["tree"])
    if test_trees[expected_version] != tree_a:
        raise AssertionError("current candidate tree does not match the trusted self-test tree")
    with tempfile.TemporaryDirectory(prefix="use-powershell-safely-lifecycle-") as temporary:
        root = Path(temporary)
        source_b = create_test_source(root, "0.3.1", "b")
        tree_b = candidate_metadata(source_b, "0.3.1")["package"]["tree"]
        destination = root / "managed" / PRODUCT

        dry_install = synchronize("install", source_a, destination, expected_version, False,
                                  trusted_target_tree=tree_a)
        assert dry_install["effect"] == "DRY_RUN" and not destination.exists()
        synchronize("install", source_a, destination, expected_version, True,
                    trusted_target_tree=tree_a)
        assert current_state(destination, tree_a)["version"] == expected_version

        dry_update = synchronize(
            "update",
            source_b,
            destination,
            "0.3.1",
            False,
            trusted_current_tree=tree_a,
            trusted_target_tree=tree_b,
        )
        assert dry_update["effect"] == "DRY_RUN"
        assert current_state(destination, tree_a)["version"] == expected_version
        synchronize(
            "update",
            source_b,
            destination,
            "0.3.1",
            True,
            trusted_current_tree=tree_a,
            trusted_target_tree=tree_b,
        )
        assert current_state(destination, tree_b)["version"] == "0.3.1"
        synchronize(
            "rollback",
            source_a,
            destination,
            expected_version,
            True,
            trusted_current_tree=tree_b,
            trusted_target_tree=tree_a,
        )
        assert current_state(destination, tree_a)["version"] == expected_version

        changed = destination / "SKILL.md"
        original = changed.read_text(encoding="utf-8")
        changed.write_text(original + "drift\n", encoding="utf-8", newline="\n")
        assert current_state(destination, tree_a)["state"] == "DRIFTED"
        try:
            uninstall(destination, True, trusted_tree=tree_a)
        except LifecycleError:
            pass
        else:
            raise AssertionError("drifted destination uninstall was not refused")
        changed.write_text(original, encoding="utf-8", newline="\n")

        foreign = root / "foreign" / PRODUCT
        foreign.mkdir(parents=True)
        (foreign / "SKILL.md").write_text("foreign\n", encoding="utf-8", newline="\n")
        try:
            uninstall(foreign, True)
        except LifecycleError:
            pass
        else:
            raise AssertionError("unreceipted destination uninstall was not refused")

        dry_uninstall = uninstall(destination, False, trusted_tree=tree_a)
        assert dry_uninstall["effect"] == "DRY_RUN" and destination.exists()
        uninstall(destination, True, trusted_tree=tree_a)
        assert current_state(destination)["state"] == "ABSENT"
    return {
        "persistent_effect": False,
        "result": "PASS",
        "scope": "disposable dry-run/install/update/rollback/drift-refusal/foreign-refusal/uninstall",
        "source_package_tree": tree_a,
        "source_version": expected_version,
    }


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="action", required=True)
    for action in ("install", "update", "rollback"):
        command = subparsers.add_parser(action)
        command.add_argument("--source", required=True)
        command.add_argument("--destination", required=True)
        command.add_argument("--expected-version", required=True)
        command.add_argument("--trusted-current-package-tree")
        command.add_argument("--trusted-target-package-tree")
        command.add_argument("--apply", action="store_true")
    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("--destination", required=True)
    status_parser.add_argument("--trusted-current-package-tree")
    uninstall_parser = subparsers.add_parser("uninstall")
    uninstall_parser.add_argument("--destination", required=True)
    uninstall_parser.add_argument("--trusted-current-package-tree")
    uninstall_parser.add_argument("--apply", action="store_true")
    self_test_parser = subparsers.add_parser("self-test")
    self_test_parser.add_argument("--source", required=False)
    self_test_parser.add_argument("--expected-version", choices=("0.3.0", "0.3.2"), default="0.3.2")
    args = parser.parse_args()

    try:
        if args.action in {"install", "update", "rollback"}:
            result = synchronize(
                args.action,
                args.source,
                args.destination,
                args.expected_version,
                args.apply,
                trusted_current_tree=args.trusted_current_package_tree,
                trusted_target_tree=args.trusted_target_package_tree,
            )
        elif args.action == "status":
            destination = assert_safe_destination(args.destination)
            result = current_state(destination, args.trusted_current_package_tree)
            result["destination"] = str(destination)
        elif args.action == "uninstall":
            result = uninstall(
                args.destination,
                args.apply,
                trusted_tree=args.trusted_current_package_tree,
            )
        else:
            result = self_test(args.source, args.expected_version)
    except (LifecycleError, OSError, AssertionError) as error:
        print(json.dumps({"error": str(error), "result": "FAIL"}, sort_keys=True))
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
