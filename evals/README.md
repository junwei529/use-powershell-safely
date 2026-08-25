# Use PowerShell Safely Evaluations

These retained cases and fixtures are exact Git blobs from source commit
`80910a8b2375a11be897e9660c4b00a06d00dd13`. They define the repository-local evaluation surface without
importing another Skill or the former monorepo evaluation envelope.

## Cases

- [`powershell-boundary.md`](cases/powershell-boundary.md)

## Fixtures

- [`powershell-boundary`](fixtures/powershell-boundary/)

## Deterministic verification

Run `python -B scripts/check_repository.py --json` from the repository root.
Case execution that invokes a model, installs a Skill, or uses an external
provider remains a separately authorized evidence action.
