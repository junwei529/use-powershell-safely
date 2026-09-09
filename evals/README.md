# Use PowerShell Safely Evaluations

The retained `v0.3.0` case and fixture baseline consists of exact Git blobs from
source commit `80910a8b2375a11be897e9660c4b00a06d00dd13`. The current
`powershell-boundary.md` case has a `0.3.2` repository-native extension;
the fixture remains unchanged. Together they define the repository-local
evaluation surface without importing another Skill or the former monorepo
evaluation envelope.

## Cases

- [`powershell-boundary.md`](cases/powershell-boundary.md)

## Fixtures

- [`powershell-boundary`](fixtures/powershell-boundary/)

## Deterministic verification

Run `python -B scripts/check_source_contract.py --json` and
`python -B scripts/check_repository.py --json` from the repository root. The
focused PowerShell boundary checker remains the executable synthetic contract.
The local lifecycle self-test operates only in a disposable temporary root.
Its default source subject is `0.3.2`; an exact historical source can be checked
with `--expected-version 0.3.0`. Current SOURCE and repository checks retain
frozen historical identity checks separately from the current candidate/map.

Accepted Q04 is bounded fresh exact-`v0.3.0`-candidate forward-behavior evidence
from one projectless, read-only, no-tool `gpt-5.6-sol/high` turn. It establishes
only the three frozen scenarios and does not qualify the current case extension.
Selection/load attribution, installed-copy behavior, publication, stable
installation, persistent lifecycle, live WSL, and broad efficacy remain
`UNKNOWN`. Any further model execution, persistent installation, discovery
change, or provider use remains separately authorized.
