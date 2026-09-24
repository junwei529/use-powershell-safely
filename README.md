# Use PowerShell Safely

[简体中文](README.zh-CN.md)

See [GitHub Releases](https://github.com/junwei529/use-powershell-safely/releases) for the latest published version and [State](docs/skills/use-powershell-safely/STATE.md) for source, installation and publication evidence.

**Help AI run commands correctly on Windows.**

Use PowerShell Safely is a Windows command-execution and troubleshooting Skill for Codex. It focuses on the error-prone boundaries between PowerShell, external programs, text files, and WSL, helping AI check key conditions before execution, locate causes after a failure, and verify actual results afterward.

It is useful for tasks involving complex arguments, paths containing Chinese characters, file encodings, subprocesses, or Windows/WSL interaction.

## How it helps

- **Check key conditions before execution.** Choose a suitable command form based on the versions, arguments, paths, and permissions involved in the task.
- **Pinpoint the failing step.** Distinguish application-code issues from command parsing, argument passing, output handling, and runtime-environment problems, so fixes address the actual cause.
- **Verify the real result.** Check whether the process has finished, whether its exit status is reliable, and whether output files and text contents match expectations.

## An example scenario

PowerShell calls Python to process JSON containing Chinese text. The command appears to have finished, but the output is incorrect.

Check the arguments Python actually received, the encodings used to read and write the file, and the process exit result. Use a minimal reproduction to locate the problem. Once the cause is clear, decide whether the command, environment, or code needs to change.

## Get started

Before executing a complex command:

```text
$use-powershell-safely
I want to call Python from PowerShell to process a JSON file whose path contains Chinese characters.
Check argument passing, encoding, and exit-status handling first, then perform the authorized operations.
```

After encountering a problem:

```text
This command says it has finished, but the expected file was not produced.
Locate the failing step and explain the evidence before proposing a fix.
```

When relevant runtime conditions have already been verified and remain unchanged, reuse that evidence; read only the diagnostic details needed for the current problem.

## Learn more

[Design](docs/skills/use-powershell-safely/DESIGN.md) ·
[Verification scope](docs/skills/use-powershell-safely/VERIFICATION.md) ·
[Evaluation scenarios](evals/cases/powershell-boundary.md)

<details>
<summary>Installation and verification, version history, and evidence limits</summary>

This repository is the independent local product repository for
`use-powershell-safely`. Its canonical editable package is
[`skills/use-powershell-safely/`](skills/use-powershell-safely/). The frozen
migration and `v0.3.0` baseline preserved package bytes from source commit
`80910a8b2375a11be897e9660c4b00a06d00dd13`; the current working source contains
a `0.3.6` source increment described in [State](docs/skills/use-powershell-safely/STATE.md).

## v0.3.0 public release

The independently versioned [`v0.3.0` public Release](https://github.com/junwei529/use-powershell-safely/releases/tag/v0.3.0)
uses public identity `junwei529/use-powershell-safely`. Its exact package tree is
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`; at that release boundary, the
candidate changed repository qualification and release-lifecycle material, not
package behavior.

Exact candidate C was accepted and is bound by
[`release/v0.3.0-local-release-receipt.json`](release/v0.3.0-local-release-receipt.json),
so `LOCAL_RELEASE_READY` is `VERIFIED`. The immutable candidate descriptor
retains its original `PENDING_PLANNER_ACCEPTANCE` snapshot. The separate
[`public-source descriptor`](release/v0.3.0-public-release-candidate.json)
preserves the immutable pre-publication snapshot. The separate
[`public-release evidence`](release/v0.3.0-public-release-evidence.json) binds
public source commit `13edb84cd1b072cb64926c5ae600714c6f7203e7`, annotated tag
`v0.3.0`, the approved non-draft/non-prerelease Release, same-version managed
lifecycle evidence, and the final exact installed copy. That evidence subject
was independently accepted by the Planner at public evidence id
`B2-PS-PUBLIC-EVIDENCE-F-01`.

Accepted Q04 proves bounded SOURCE-forward behavior for three frozen scenarios.
Fresh projectless witnesses separately prove origin-aware absence and the sole
USER-scope exact installed copy's selection, full five-file load, and the same
three bounded scenarios. Cross-version lifecycle, live WSL, cross-Harness
behavior, untested contexts, and broad efficacy remain `UNKNOWN`.

## Retained 0.3.2 local installation

The retained `0.3.2` five-file package and its PowerShell boundary case include a
source-only increment for proportionate harness diagnosis, wrapper-aware text
contracts, JSON representation limits, explicit Python UTF-8 handling, and
related eval coverage. Its package tree is
`f76f6deaec88101ecdda4c5dbc47405d8b930a65`. The user-confirmed `0.3.2`
USER installation matched all five `0.3.2` source files and was readable in the ordinary
sandbox. It and the older `0.3.1-local.3` copy are retained for recovery. Fresh-task
loading, model qualification, and publication are not established for `0.3.2`;
the frozen `v0.3.0` evidence remains unchanged.
See [Verification](docs/skills/use-powershell-safely/VERIFICATION.md) for the
current verification entry points and retained historical failure records.

## Current 0.3.6 source

The user-confirmed, unreleased 0.3.6 entrypoint reuses the package's existing
[Runtime Readiness](skills/use-powershell-safely/references/native-process-boundaries.md#runtime-readiness)
procedure. Runtime and capability evidence, PowerShell 5.1 and 7 compatibility,
version and installation decisions, process results, and authorization boundaries
remain in their existing owners. The current source candidate and mapping are
[v0.3.6](release/v0.3.6-candidate.json) and
[source-map-v0.3.6](provenance/source-map-v0.3.6.json); see
[State](docs/skills/use-powershell-safely/STATE.md) and
[Verification](docs/skills/use-powershell-safely/VERIFICATION.md) for delivery
evidence and limits. At this preparation checkpoint, the published release was 0.3.4.
The local managed copy is 0.3.6 and matches all five source files; see State
for the retained approval and ACL postflight evidence.

## Retained 0.3.5 source

The retained, unpublished 0.3.5 source clarifies JSON timestamp result
types, explicit timezone and interval semantics, and version-dependent
`DateKind` capability in the existing Text reference. The existing evaluation
case and identity consumers follow this candidate. [State](docs/skills/use-powershell-safely/STATE.md)
and [Verification](docs/skills/use-powershell-safely/VERIFICATION.md) separate
source checks from installation and natural behavior. The separately authorized
local managed installation was 0.3.5 at that checkpoint; its source identity, ordinary-reader
access and preserved permissions were verified. The published release remains
0.3.4. Fresh-task loading and natural adherence remain unverified.

## Retained 0.3.4 source

The user-confirmed 0.3.4 revision shortens only the catalog description while
retaining the material pre-command and diagnostic triggers and ordinary-task
exclusions. Body instructions, references, agent metadata, and case definitions
are unchanged. [State](docs/skills/use-powershell-safely/STATE.md) and
[Verification](docs/skills/use-powershell-safely/VERIFICATION.md) distinguish this
source and verified 0.3.4 local installation from the retained 0.3.3 rollback
copy and historical evidence.

## Retained 0.3.3 source and installation

The user-confirmed `0.3.3` source separates pre-command boundary preparation
from failure diagnosis, reuses verified unchanged-runtime evidence, and loads
reference details only for the material question. Its candidate is a source
assessment snapshot, not installation or model-behavior evidence. Independent
source acceptance and the USER update to the matching `0.3.3` copy are complete.
Following separately approved exact-root ACL inheritance repair, ordinary-sandbox
checks verify all five files, receipt and managed status. Fresh-task loading and
model behavior remain unproven; see [State](docs/skills/use-powershell-safely/STATE.md).

## Repository contents

- Product package: [`skills/use-powershell-safely/`](skills/use-powershell-safely/)
- Product design and state: [`docs/skills/use-powershell-safely/`](docs/skills/use-powershell-safely/)
- Evaluation cases and fixtures: [`evals/`](evals/README.md)
- Standalone verification: [`scripts/check_repository.py`](scripts/check_repository.py)
- Source mapping: [`PROVENANCE.md`](PROVENANCE.md),
  [current mapping](provenance/source-map-v0.3.6.json), and
  [frozen historical mapping](provenance/source-map.json)

## Managed install, update and rollback

Use an immutable checkout of the published tag and verify its resolved commit.
The tool's built-in trust map contains only `0.3.0`. The intended `0.3.6`
package tree is `3e5e3f6463ad582e1279a94e27c36b07225127e2`; after publication,
verify it independently against the GitHub Release and retain that trust value
apart from the checkout. Do not take it solely from the candidate or installed
receipt that it is meant to verify.

Run these examples from the verified `v0.3.6` repository root and replace quoted
placeholders with your exact paths or independently verified identities. These
commands are dry-runs; `install` requires an absent destination, while `update`
and `rollback` require an unchanged managed copy with a valid receipt.

```text
python -B scripts/manage_install.py install --source . --destination "<destination>" --expected-version 0.3.6 --trusted-target-package-tree 3e5e3f6463ad582e1279a94e27c36b07225127e2
python -B scripts/manage_install.py update --source . --destination "<destination>" --expected-version 0.3.6 --trusted-current-package-tree "<independently-retained-current-tree>" --trusted-target-package-tree 3e5e3f6463ad582e1279a94e27c36b07225127e2
```

`--trusted-target-package-tree` verifies the version being installed.
`--trusted-current-package-tree` verifies the version already at the destination;
it is required when that version is absent from the built-in map, including
`0.3.6`. For a current `0.3.0` copy, the current-tree argument may be omitted.
After an authorized `0.3.6` update, verify status with its independently checked tree:

```text
python -B scripts/manage_install.py status --destination "<destination>" --trusted-current-package-tree 3e5e3f6463ad582e1279a94e27c36b07225127e2
```

To roll back from `0.3.6`, retain the older immutable source and its independently
verified tree; a successful update may remove its temporary backup. Use the
current tool with the older source and version as the target:

```text
python -B scripts/manage_install.py rollback --source "<verified-older-checkout>" --destination "<destination>" --expected-version "<older-version>" --trusted-current-package-tree 3e5e3f6463ad582e1279a94e27c36b07225127e2 --trusted-target-package-tree "<independently-retained-older-tree>"
```

`uninstall` takes the same destination and current-tree options as `status` and
is also a dry-run by default. Review a dry-run's version, destination and tree,
then append `--apply` to the same mutating command only when the actual effect
is authorized. `status` never takes `--apply`. Stop on drift or a foreign copy;
do not change the trust value to make a rejection pass. These instructions
describe the tool contract, not a new cross-version or host-permission test.

## Verify

```powershell
python -B scripts/check_source_contract.py --json
python -B scripts/manage_install.py self-test --source .
python -B scripts/check_repository.py --json
python -B scripts/check_repository.py --adversarial
pwsh -NoLogo -NoProfile -NonInteractive -File evals/check-powershell-boundaries.ps1
powershell.exe -NoLogo -NoProfile -NonInteractive -File evals/check-powershell-boundaries.ps1
```

The lifecycle tool is dry-run by default and requires an explicit destination
plus `--apply` for a real change. The repository has no implicit dependency on
another Skill repository. The retained public evidence distinguishes immutable
source, publication, same-version lifecycle, and loaded-copy behavior; it does
not claim cross-version lifecycle, Profile mutation, live WSL, cross-Harness
behavior, untested contexts, or broad product efficacy.

</details>
