# Use PowerShell Safely State

## Current implementation

Canonical editable source is the 5-file package under
[`skills/use-powershell-safely/`](../../../skills/use-powershell-safely/). Every package file and retained
case or fixture is an exact Git blob from `80910a8b2375a11be897e9660c4b00a06d00dd13`.

## Repository ownership

This repository owns its Git history, documentation, checks, and future version,
evaluation, installation, and release decisions. It has no implicit dependency
on another Skill repository. Its public origin is
`https://github.com/junwei529/use-powershell-safely.git`.

The public identity is `junwei529/use-powershell-safely`. Version `v0.3.0` is
the initial independent public Release; later versions are independently owned
by this repository.

The public-source candidate
[`release/v0.3.0-public-release-candidate.json`](../../../release/v0.3.0-public-release-candidate.json)
preserves its `PENDING_HUMAN_APPROVAL` pre-publication snapshot. The separate
[`public-release evidence`](../../../release/v0.3.0-public-release-evidence.json)
records exact public source P, annotated tag object, human-approved Release,
same-version managed lifecycle, origin-aware absence, and final exact installed
copy. The Planner accepted exact evidence subject F
`21eca7724a84b4073c98c68e548b1816c52a0ff0`, tree
`a53e693d29d33dddd6bb673ba3f54a2fcedbfe54`, at public evidence id
`B2-PS-PUBLIC-EVIDENCE-F-01`; the evidence state is now `VERIFIED`.

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

Public source P is commit `13edb84cd1b072cb64926c5ae600714c6f7203e7`
with tree `6f03b9a5717f823f87d117fc17b5040e0531dcc8`; annotated tag object
`58cd1276ad43589c93489c919c285ce7fec2d42d` peels to P. GitHub Release
`v0.3.0` is public, non-draft, and non-prerelease. Exact Release-note review,
immutable public source, publication, persistent same-version lifecycle,
origin-aware absence, sole installed-copy discovery, stable installed-copy
identity, complete five-file load, and bounded three-scenario behavior are
`VERIFIED` observations accepted by the Planner for exact evidence subject F.

Cross-version update/rollback, live WSL, cross-Harness behavior, untested
contexts, and broad product efficacy remain `UNKNOWN`. The retained legacy copy
is preserved outside Skill discovery roots; its private recovery locator remains
controller-side.

## Next gate

B2 public-release and stable-copy acceptance is durably recorded. No further B2
effect is authorized by this state transition. Ordinary local changes must
preserve the provenance record or explicitly supersede the mapped baseline.

## Recovery entry

Read the root [`AGENTS.md`](../../../AGENTS.md),
[`PROVENANCE.md`](../../../PROVENANCE.md), [Design](DESIGN.md), this State, and
[Verification](VERIFICATION.md). Verify Git status, current branch, package
identity, and writer ownership before changing files.
