# Use PowerShell Safely

[简体中文](README.zh-CN.md)

Diagnoses and safely executes boundary-sensitive Windows shell workflows across PowerShell, native executables, and WSL.

This repository is the independent local product repository for
`use-powershell-safely`. Its canonical editable package is
[`skills/use-powershell-safely/`](skills/use-powershell-safely/). The frozen
migration and `v0.3.0` baseline preserved package bytes from source commit
`80910a8b2375a11be897e9660c4b00a06d00dd13`; the current working source contains
a `0.3.2` local increment described in [State](docs/skills/use-powershell-safely/STATE.md).

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

## Current 0.3.2 local installation

The working five-file package and PowerShell boundary case now include a
source-only increment for proportionate harness diagnosis, wrapper-aware text
contracts, JSON representation limits, explicit Python UTF-8 handling, and
related eval coverage. The current package tree is
`f76f6deaec88101ecdda4c5dbc47405d8b930a65`. The user-confirmed `0.3.2`
USER installation matches all five source files and is readable in the ordinary
sandbox. The old `0.3.1-local.3` copy is retained for recovery. Fresh-task
loading, model qualification, and publication are not established for `0.3.2`;
the frozen `v0.3.0` evidence remains unchanged.
See [Verification](docs/skills/use-powershell-safely/VERIFICATION.md) for the
current verification entry points and retained historical failure records.

## Repository contents

- Product package: [`skills/use-powershell-safely/`](skills/use-powershell-safely/)
- Product design and state: [`docs/skills/use-powershell-safely/`](docs/skills/use-powershell-safely/)
- Evaluation cases and fixtures: [`evals/`](evals/README.md)
- Standalone verification: [`scripts/check_repository.py`](scripts/check_repository.py)
- Source mapping: [`PROVENANCE.md`](PROVENANCE.md),
  [current mapping](provenance/source-map-v0.3.2.json), and
  [frozen historical mapping](provenance/source-map.json)

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
