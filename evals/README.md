# Use PowerShell Safely Evaluations

These retained cases and fixtures are exact Git blobs from source commit
`80910a8b2375a11be897e9660c4b00a06d00dd13`. They define the repository-local evaluation surface without
importing another Skill or the former monorepo evaluation envelope.

## Cases

- [`powershell-boundary.md`](cases/powershell-boundary.md)

## Fixtures

- [`powershell-boundary`](fixtures/powershell-boundary/)

## Deterministic verification

Run `python -B scripts/check_source_contract.py --json` and
`python -B scripts/check_repository.py --json` from the repository root. The
focused PowerShell boundary checker remains the executable synthetic contract.
The local lifecycle self-test operates only in a disposable temporary root.

Accepted Q04 is bounded fresh exact-SOURCE forward-behavior evidence from one
projectless, read-only, no-tool `gpt-5.6-sol/high` turn. It establishes only the
three frozen scenarios; selection/load attribution, installed-copy behavior,
publication, stable installation, persistent lifecycle, live WSL, and broad
efficacy remain `UNKNOWN`. Any further model execution, persistent installation,
discovery change, or provider use remains separately authorized.
