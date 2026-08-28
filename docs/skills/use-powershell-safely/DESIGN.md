# Use PowerShell Safely Design

## Product boundary

Diagnoses and safely executes boundary-sensitive Windows shell workflows across PowerShell, native executables, and WSL. The canonical installable source is
[`skills/use-powershell-safely/`](../../../skills/use-powershell-safely/). Package instructions, references,
assets, and metadata preserve the exact source blobs from `80910a8b2375a11be897e9660c4b00a06d00dd13`.

The repository owns one Skill product. Cross-Skill composition is optional and
cannot grant authority or create a hard dependency.

## Package contract

The package contains exactly 5 files. `SKILL.md` owns
selection and entry behavior; directly linked references and assets own detailed
guidance and templates. The repository checker fails if any package byte or
expected path differs from the recorded baseline mapping.

## Evaluation surface

- `evals/cases/powershell-boundary.md`

Cases and fixtures are exact source blobs. They define deterministic inputs and
expected boundaries; model runs, installation, and release remain separately
authorized evidence classes.

## Independent release qualification

The local `v0.3.0` candidate binds the unchanged five-file package tree and a
deterministic SOURCE contract. Repository-local lifecycle tooling accepts an
explicit immutable candidate source and explicit destination, is dry-run by
default, and refuses roots, homes, link-like paths, foreign copies, and drifted
managed copies. Disposable self-tests exercise install, update, rollback,
drift refusal, foreign-copy refusal, and uninstall without changing persistent
discovery or user configuration.

The local candidate descriptor and a later Planner-acceptance receipt are
separate identities: candidate acceptance can prove `LOCAL_RELEASE_READY` for
one immutable commit, but only a later authorized public phase can prove a tag,
Release, stable installed copy, or fresh loaded-copy behavior.

Candidate C remains immutable. Its separate local-release receipt binds the
exact candidate commit, candidate tree, unchanged package tree, independent
Planner acceptance, and the hash-addressed bounded Q04 SOURCE-forward evidence
without recording private task, turn, message, host, or checkout identifiers.

The separate public-source descriptor is intentionally non-circular: it binds
the accepted B1 receipt, unchanged package tree and package digest, exact
release-note hash, repository identity, default branch, annotated tag, and
GitHub Release settings without embedding its own future commit. Its pending
snapshot can qualify immutable source preparation but cannot prove a public ref
or an external Release effect.

## Standalone constraints

- No other Skill package is included.
- Verification uses only repository-local files and standard host tools.
- Source provenance is explicit in [`../../../provenance/source-map.json`](../../../provenance/source-map.json).
- Historical monorepo state is not a runtime dependency or acceptance condition.
