# Use PowerShell Safely

[简体中文](README.zh-CN.md)

Diagnoses and safely executes boundary-sensitive Windows shell workflows across PowerShell, native executables, and WSL.

This repository is the independent local product repository for `use-powershell-safely`. Its
installable package is [`skills/use-powershell-safely/`](skills/use-powershell-safely/), preserved byte for
byte from source commit `80910a8b2375a11be897e9660c4b00a06d00dd13`.

## Local v0.3.0 candidate

The independently versioned `v0.3.0` candidate targets the approved future
public identity `junwei529/use-powershell-safely`. Its exact package tree is
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`; the candidate changes repository
qualification and release-lifecycle material, not package behavior.

Candidate state is `PENDING_PLANNER_ACCEPTANCE`, and human review of
[`CHANGELOG.md`](CHANGELOG.md) is pending before any public release. Local
deterministic checks do not prove a public Release, persistent lifecycle,
stable installed-copy behavior, model behavior, or broad efficacy.

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
repository. A remote, tag, Release, publication, persistent installation,
Profile, or discovery-configuration effect remains outside this candidate.
