# Use PowerShell Safely State

## Current implementation

Canonical editable source is the 5-file package under
[`skills/use-powershell-safely/`](../../../skills/use-powershell-safely/). It is
currently the user-confirmed `0.3.3` source with package tree
`842b87d85c151a9c944cb855123c0ce7d69be1e5` and SOURCE-list digest
`461cb805672dbe3bda67151227692845a34e0c6ddbf2a88c29d4b733c6aea478`.
It distinguishes material pre-command preparation from failure diagnosis,
reuses verified unchanged-runtime evidence, and loads reference details only
as needed. Only the entrypoint and Native/Text references change from `0.3.2`;
existing safeguards, agent metadata and Windows/WSL guidance are retained.

The managed USER update to `0.3.3` completed once. Management-context
verification confirms all five files match the accepted source tree above.
After separately approved exact-root ACL inheritance repair, ordinary-sandbox
checks verify all five files, receipt and managed status. Its installer mapping digest is
`ec5e05c5a144285952f05a7e31935e2d16efa3831bcf5de3286681ce4d763d9c`;
the SOURCE-list digest hashes a sorted list rather than the installer's
mapping, so the two digest values are not interchangeable. The old `0.3.2`
tree `f76f6deaec88101ecdda4c5dbc47405d8b930a65` and original receipt are
retained outside discovery roots as verified recovery input. The older
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

The `0.3.3` candidate retains its source-assessment snapshot. Independent source
acceptance is complete. The same-location USER update and management-context
byte verification are complete. Ordinary-sandbox readability and identity checks
also pass after the separately approved exact-root ACL inheritance repair.
These separate observations are not inferred from candidate generation. New scenario contracts are
not model qualification or fresh-task loading/behavior evidence.

Current local checks pass: Skill structure, SOURCE 14 checks, repository 38-file
inventory/provenance, PowerShell 7 and Windows PowerShell 5.1 each 59 focused
assertions, and the disposable `0.3.3` lifecycle self-test.

### Local 0.3.3 installation checkpoint

After independent source acceptance, preparation bound the source, old managed
copy and original receipt, retained the `0.3.2` files, and passed update dry-run.
One live update returned `MANAGED 0.3.3`. Its new receipt SHA-256 is
`a8e004e9e00887bfb76555bd8c56e0a6a26d5893bec6a6651447680d1de23c48`.
Management-context verification passed exact five-file hashes, strict UTF-8/LF,
receipt, managed status and rollback dry-run to the retained `0.3.2` source.
No live rollback was performed.

The ordinary sandbox initially could read none of the five files or receipt. Read-only
ACL inspection found the replacement root protected from inheritance while its
parent retains the sandbox read permission. Following separate explicit approval,
inheritance was enabled only on that exact root, preserving explicit entries and
without a recursive switch or parent-directory change. The command processed
one directory successfully. The unchanged verifier then passed in the ordinary
sandbox: all five files and receipt readable, exact hashes, strict UTF-8/no-BOM/LF,
`MANAGED 0.3.3`, retained recovery identity and rollback dry-run. The earlier
permission failure remains historical failure evidence. No second update, live
rollback or model run was performed. Independent assessment accepted this exact
source and local installation checkpoint, including ordinary-sandbox identity,
readability and retained recovery evidence.

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

### Retained 0.3.2 verification

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
review. The independently accepted root README update completed its own native
review and commit as `92ad426f3bfc358a8df21fe633264edffbb994c0`. Both original
commit identities remain unchanged. Their first ordinary GitHub `main` push
was rejected by platform approval before a process started; that rejection
remains historical evidence. After a new explicit user approval for the exact
two-commit range and normal platform approval, the non-force push completed.
Remote `main` was independently read back as
`92ad426f3bfc358a8df21fe633264edffbb994c0`. No `0.3.3` commit was included.

The `0.3.3` source is independently accepted and the same-location USER update
has completed. Separately approved exact-root ACL inheritance repair and ordinary-
sandbox identity/readability checks are complete and independently accepted.
No further environment changes are authorized. Commit, push, tag/Release and
new model/runtime-effect claims are not established by this source work.

## Documentation impact

- `0.3.3`: entrypoint and Native/Text references plus the existing case record
  own the preparation/reuse change. Root presentation content is retained;
  lifecycle disclosures, product README pair, Design, State, Verification,
  PROVENANCE and eval index distinguish accepted SOURCE, the completed USER
  update, and ordinary-sandbox readability verified after separately approved
  exact-root ACL inheritance repair, retaining the initial failure as history.
  Existing validation entry points target the new candidate/current map;
  `0.3.2` candidate/map and all `v0.3.0` history remain unchanged. The installer
  production path is unchanged; only its self-test's version/tree selection
  advances, retaining historical explicit-version self-tests.

- README follow-up: the root bilingual entry now explains purpose, usage and
  an illustrative scenario, with existing version, installation, verification
  and evidence limits retained in a closing disclosure. The scenario is not a
  new test result; package and installed-copy evidence are unchanged.
- Retained `0.3.2` documentation history: the root README pair, product README
  pair, Design, State, Verification, `PROVENANCE.md`, and `evals/README.md`
  distinguished frozen `v0.3.0` evidence from the then-current `0.3.2` source and local installed
  copy; the old local package remains a recovery copy.
- Retained `0.3.2` validation history: its candidate, source map, four existing
  validation entry points and their documentation identified `0.3.2` separately
  from historical release evidence. The full `0.3.2` increment changed
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
