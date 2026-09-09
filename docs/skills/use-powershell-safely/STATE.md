# Use PowerShell Safely State

## Current implementation

Canonical editable source is the 5-file package under
[`skills/use-powershell-safely/`](../../../skills/use-powershell-safely/). It is
currently the user-confirmed `0.3.2` local installation source with package tree
`f76f6deaec88101ecdda4c5dbc47405d8b930a65` and package digest
`bdbbe8e85e5d5d086c1f6fc4f760f1e5868b4803f54278080d80c6d987bc1d0b`.
It preserves the accepted local Git brace-revspec and command-local
`safe.directory` guidance and adds proportionate harness diagnosis,
callback-aware terminal routing, wrapper-aware text contracts, JSON
representation limits, explicit Python UTF-8 handling, and matching eval
coverage.

The managed USER copy is now `0.3.2`, with all five files byte-identical to
current source. Its installer mapping digest is
`ff909615ea97bcc60dad59b66a6d2ee5cdf3b2ac6620aec7e6c98615001b6003`;
the SOURCE digest above hashes a sorted list rather than the installer's
mapping, so the two digest values are not interchangeable. The old
`0.3.1-local.3` package tree `2b1c9fd648bfa7c9b1368d9ca2229501f99e388c`
and original receipt are retained outside Skill discovery roots for recovery.
This is a local installation, with no new public release or model qualification.

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

The migration and release records prove package, mapped case, and fixture byte
identity plus local link, publication-safety, and repository verification for
their named frozen subjects; they do not prove current working-source byte
identity. Candidate C is immutable commit
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
five-file `v0.3.0` candidate tree. Its one final response (SHA-256
`8fba2576f76755e77d848574b60e19b2276d378e5e5de46027b9dcd97774c085`)
passed only the frozen PowerShell native/JSON positive, ordinary-cmdlet
negative, and POSIX-only negative scenarios.

### Accepted source-only checkpoint history

At that checkpoint, the increment passed Skill structure validation, `git diff --check`,
and every non-identity deterministic SOURCE content check. Read-only examples
on PowerShell Core 7.6.3 confirmed nested outer-variable interpolation, quoted
Git `--format=%(...)`, empty-name JSON conversion guarded by live
`-AsHashtable` capability, and explicit Python UTF-8 decoding with optional
process-local `-X utf8`.

The SOURCE contract then returned failure for the frozen candidate, receipt,
public-source, and public-evidence identities. Repository verification reported
only the corresponding mapped byte/blob identity mismatches. The focused
PowerShell checker stopped at its first frozen package-manifest identity gate, so
its later assertions did not run and are not claimed as passing. No new model
qualification, installed-copy execution, cross-Harness proof, or runtime
consumption evidence was produced by that source-only acceptance.

### Current 0.3.2 verification

The user authorized current candidate and source-mapping records and the four
existing validation entry points. Current SOURCE checks now validate both the
frozen historical subjects and the accepted current package independently.
PowerShell 7 and Windows PowerShell 5.1 each complete all 59 boundary checks;
the `0.3.2` disposable lifecycle completes install/update/rollback and refusal
checks. Current inventory and provenance are owned by
`provenance/source-map-v0.3.2.json`; the historical map and all four `v0.3.0`
release objects remain byte-identical. The complete staged-index adversarial
matrix passes, including current-identity and frozen-history rejection cases.
This does not retroactively pass the
earlier failed commands or add model qualification.

### Local 0.3.2 installation

The existing installer completed an explicit-tree update to `0.3.2`.
A private-directory rehearsal verified old-package install, update to `0.3.2`,
and rollback to `0.3.1-local.3`; live rollback was dry-run only. The new live
receipt SHA-256 is
`e782b1fa9555db2710b4051c42cb4674b13f6346b3303020b6c84cfa3c15735f`.
The staged directory initially blocked sandbox reading through a protected ACL.
After explicit approval, parent ACL inheritance was enabled only on the
installed package directory, preserving existing entries. Ordinary sandbox
verification then read all five files and receipt, confirmed strict UTF-8/LF,
and verified source identity and managed status. Future installer replacements
may need the same permission check; installer behavior was not changed.
Fresh-task discovery, model loading and behavior remain `UNKNOWN`.

Public source P is commit `13edb84cd1b072cb64926c5ae600714c6f7203e7`
with tree `6f03b9a5717f823f87d117fc17b5040e0531dcc8`; annotated tag object
`58cd1276ad43589c93489c919c285ce7fec2d42d` peels to P. GitHub Release
`v0.3.0` is public, non-draft, and non-prerelease. Exact Release-note review,
immutable public source, publication, persistent same-version lifecycle,
origin-aware absence, sole installed-copy discovery, stable installed-copy
identity, complete five-file load, and bounded three-scenario behavior are
`VERIFIED` observations accepted by the Planner for exact evidence subject F.

Broad cross-version update/rollback, live WSL, cross-Harness behavior, untested
contexts, and broad product efficacy remain `UNKNOWN`. The retained legacy copy
is preserved outside Skill discovery roots; its private recovery locator remains
controller-side.

## Next gate

B2 public-release and stable-copy acceptance is durably recorded. No further B2
effect is authorized by this state transition. The confirmed `0.3.2` local
installation is complete. The local source commit
`9dccf92af9dbea3a84f551f47eb7088880be5688` completed verification and native
review. The subsequent root README update passed independent documentation
assessment and changes no package behavior. The user authorized its separate
native-review and commit gate, followed by an ordinary fast-forward push of
both commits to the existing GitHub origin's `main` branch. Git history and
live remote-ref verification establish completion of those Git effects; this
authorization is not itself completion evidence. Historical evidence remains
frozen. Tag/Release and new model or runtime-effect claims remain outside this
closeout.

## Documentation impact

- README follow-up: the root bilingual entry now explains purpose, usage and
  an illustrative scenario, with existing version, installation, verification
  and evidence limits retained in a closing disclosure. The scenario is not a
  new test result; package and installed-copy evidence are unchanged.
- Updated: the root README pair, product README pair, Design, this State,
  Verification, `PROVENANCE.md`, and `evals/README.md` now distinguish the
  frozen `v0.3.0` evidence from the current `0.3.2` source and local installed
  copy; the old local package remains a recovery copy.
- Current validation: the candidate, current source map, four existing
  validation entry points and their documentation identify `0.3.2` separately
  from historical release evidence. The full staged `0.3.2` increment changes
  three installable package files: `SKILL.md` and the Native/Text references.
  The subsequent validation-only follow-up makes no further package changes
  beyond that accepted source increment.
- Checked with no change: `CHANGELOG.md`, release candidates, receipts, public
  evidence, and `provenance/source-map.json` remain frozen historical identity
  records; the fixture README still describes an unchanged fixture.

## Recovery entry

Read the root [`AGENTS.md`](../../../AGENTS.md),
[`PROVENANCE.md`](../../../PROVENANCE.md), [Design](DESIGN.md), this State, and
[Verification](VERIFICATION.md). Verify Git status, current branch, package
identity, and writer ownership before changing files.
