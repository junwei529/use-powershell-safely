# Use PowerShell Safely

[简体中文](README.zh-CN.md)

Diagnoses and safely executes boundary-sensitive Windows shell workflows across PowerShell, native executables, and WSL.

This repository is the independent local product repository for `use-powershell-safely`. Its
installable package is [`skills/use-powershell-safely/`](skills/use-powershell-safely/), preserved byte for
byte from source commit `80910a8b2375a11be897e9660c4b00a06d00dd13`.

## v0.3.0 public-source candidate

The independently versioned `v0.3.0` candidate targets the approved future
public identity `junwei529/use-powershell-safely`. Its exact package tree is
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`; the candidate changes repository
qualification and release-lifecycle material, not package behavior.

Exact candidate C was accepted and is bound by
[`release/v0.3.0-local-release-receipt.json`](release/v0.3.0-local-release-receipt.json),
so `LOCAL_RELEASE_READY` is `VERIFIED`. The immutable candidate descriptor
retains its original `PENDING_PLANNER_ACCEPTANCE` snapshot. The separate
[`public-source descriptor`](release/v0.3.0-public-release-candidate.json)
binds the intended public repository, annotated tag, Release settings,
release-note hash, B1 receipt, and unchanged package identity. Human review of
the exact [`CHANGELOG.md`](CHANGELOG.md) title and body remains pending before
tag or GitHub Release creation.

Accepted Q04 proves only bounded SOURCE-forward behavior for three frozen
scenarios. It does not prove selection/load attribution, installed-copy
behavior, persistent lifecycle, a public Release, stable installation, live
WSL, or broad efficacy.

## Repository contents

- Product package: [`skills/use-powershell-safely/`](skills/use-powershell-safely/)
- Product design and state: [`docs/skills/use-powershell-safely/`](docs/skills/use-powershell-safely/)
- Evaluation cases and fixtures: [`evals/`](evals/README.md)
- Standalone verification: [`scripts/check_repository.py`](scripts/check_repository.py)
- Source mapping: [`PROVENANCE.md`](PROVENANCE.md) and
  [`provenance/source-map.json`](provenance/source-map.json)

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
plus `--apply` for a real change. Local qualification uses only its disposable
self-test root. The repository has no implicit dependency on another Skill
repository. This public-source candidate does not itself prove a remote ref,
tag, GitHub Release, publication, persistent installation, Profile, discovery
configuration, or installed-copy behavior.
