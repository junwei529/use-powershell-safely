# Use PowerShell Safely Design

## Product boundary

Diagnoses and safely executes boundary-sensitive Windows shell workflows across PowerShell, native executables, and WSL. The canonical installable source is
[`skills/use-powershell-safely/`](../../../skills/use-powershell-safely/). The
frozen migration and `v0.3.0` baseline preserved package instructions,
references, assets, and metadata as exact source blobs from
`80910a8b2375a11be897e9660c4b00a06d00dd13`. The current editable package may
contain repository-native increments explicitly recorded in [State](STATE.md)
without relabeling that historical identity.

The repository owns one Skill product. Cross-Skill composition is optional and
cannot grant authority or create a hard dependency.

## Package contract

The package contains exactly 5 files. `SKILL.md` owns
selection and entry behavior; directly linked references and assets own detailed
guidance and templates. The repository checker verifies current paths and bytes
against `provenance/source-map-v0.3.2.json`. It separately verifies the unchanged
historical map and release evidence. Original migration source records stay in
the current map, while explicit rewrite records identify repository-native
changes without claiming exact original byte identity.

## Evaluation surface

- `evals/cases/powershell-boundary.md`

The `v0.3.0` case and fixture baseline consists of exact source blobs. The
current PowerShell boundary case may extend that repository-native evaluation
contract while the fixture remains unchanged. Model runs, installation, and
release remain separately authorized evidence classes.

## Current 0.3.2 local increment

The current source increment keeps the same five-file product shape while
adding proportionate harness-versus-child diagnosis, callback-aware terminal
routing, wrapper-aware text contracts, JSON representation limits, explicit
Python UTF-8 handling, and matching eval coverage. It preserves the accepted
local Git brace-revspec and command-local `safe.directory` guidance. This is a
user-confirmed `0.3.2` local installation source. Installation and ordinary
sandbox readability are recorded in State; model qualification, public release,
and fresh-task runtime consumption are not established.

## Independent release qualification

The `0.3.2` candidate identifies current SOURCE and local installation only.
SOURCE checks compare historical evidence to its historical package and current
evidence to the accepted current package. The focused checker pins the current
package manifest before running the same synthetic assertions. Lifecycle
self-test defaults to the independently pinned `0.3.2` source and also accepts
`--expected-version 0.3.0` when supplied an exact historical source directory.
Production install/update/rollback trust and ACL behavior are unchanged.

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
