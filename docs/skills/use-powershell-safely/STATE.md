# Use PowerShell Safely State

## Current implementation

Canonical editable source is the 5-file package under
[`skills/use-powershell-safely/`](../../../skills/use-powershell-safely/). Every package file and retained
case or fixture is an exact Git blob from `80910a8b2375a11be897e9660c4b00a06d00dd13`.

## Repository ownership

This repository owns its Git history, documentation, checks, and future version,
evaluation, installation, and release decisions. It has no implicit dependency
on another Skill repository and begins with no configured remote.

The approved future public identity is
`junwei529/use-powershell-safely`. Version `v0.3.0` is the initial independent
candidate; later versions are independently owned by this repository.

## Evidence state

The migration proves current package byte identity, mapped case and fixture
byte identity, local link and publication-safety checks, and repository-local
verification. Candidate C is immutable commit
`ad8f056b110ee3798a5f92ed9715c1085e45fe72`, tree
`4a2597202b89b91c330e559f86d04fc288894bea`, and exact package tree
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`. The Planner accepted exact C with
public evidence id `Q04`; the separate
[`v0.3.0 local-release receipt`](../../../release/v0.3.0-local-release-receipt.json)
records `LOCAL_RELEASE_READY=VERIFIED` without rewriting C.

Historical `c42eef3...` model and loaded-copy evidence belongs to different
package tree `22c230...` and is not forwarded to this candidate. Q01 and Q02
remain sealed transport/permission stops with behavior `UNKNOWN_NOT_ASSESSED`;
Q03 remains a sealed preflight stop with no SOURCE transmission. Accepted Q04
is one projectless, read-only, no-tool `gpt-5.6-sol/high` turn against the exact
five-file current tree. Its one final response (SHA-256
`8fba2576f76755e77d848574b60e19b2276d378e5e5de46027b9dcd97774c085`)
passed only the frozen PowerShell native/JSON positive, ordinary-cmdlet
negative, and POSIX-only negative scenarios.

Selection/load attribution, installed-copy behavior, public Release,
persistent install/update/uninstall behavior, stable installed copy, live WSL,
and broad efficacy remain `UNKNOWN`. Human public release-note review remains
`PENDING`.

## Next gate

The next release gate is the separately authorized immutable public source and
publication route. Any remote, persistent installation, tag, Release,
publication, discovery/configuration, installed-copy evaluation, or broader
model-evaluation action requires its own authority and fresh evidence. Ordinary
local changes must preserve the provenance record or explicitly supersede the
mapped baseline.

## Recovery entry

Read the root [`AGENTS.md`](../../../AGENTS.md),
[`PROVENANCE.md`](../../../PROVENANCE.md), [Design](DESIGN.md), this State, and
[Verification](VERIFICATION.md). Verify Git status, current branch, package
identity, and writer ownership before changing files.
