# Use PowerShell Safely

[简体中文](README.zh-CN.md)

Diagnoses and safely executes boundary-sensitive Windows shell workflows across PowerShell, native executables, and WSL.

This repository is the independent local product repository for `use-powershell-safely`. Its
installable package is [`skills/use-powershell-safely/`](skills/use-powershell-safely/), preserved byte for
byte from source commit `80910a8b2375a11be897e9660c4b00a06d00dd13`.

## Repository contents

- Product package: [`skills/use-powershell-safely/`](skills/use-powershell-safely/)
- Product design and state: [`docs/skills/use-powershell-safely/`](docs/skills/use-powershell-safely/)
- Evaluation cases and fixtures: [`evals/`](evals/README.md)
- Standalone verification: [`scripts/check_repository.py`](scripts/check_repository.py)
- Source mapping: [`PROVENANCE.md`](PROVENANCE.md) and
  [`provenance/source-map.json`](provenance/source-map.json)

## Verify

```powershell
python -B scripts/check_repository.py --json
```

The repository has no implicit dependency on another Skill repository. Remote,
installation, tag, release, publication, and historical-continuity claims are
outside this migration snapshot.
