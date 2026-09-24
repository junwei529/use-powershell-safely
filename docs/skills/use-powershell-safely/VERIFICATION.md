# Use PowerShell Safely Verification

## v0.3.6 publication verification

Independent R inspected the full 18-path outgoing diff, four newly tracked
candidate/map files, necessary consumers and the complete Release body, with
no P0/P1/P2 finding. SOURCE passed 14/14 checks, repository/provenance passed
44 mapped files, and staged `diff --check` passed before source commit. The
committed package tree is `3e5e3f6463ad582e1279a94e27c36b07225127e2`.

An atomic push advanced remote `main` to source commit
`ac5e422cf1732d50e5b0ac6a54805039ba98a108` and created annotated tag
object `d2e01ddf1cfc5aeb524af0ebc42dd2db6495b573`, which peels to that
commit. The GitHub Release readback returned ID `395421385`, tag `v0.3.6`,
the exact commit target, `draft=false`, `prerelease=false`, and
`published_at=2026-09-24T07:08:03Z`; `/releases/latest` returned the same ID.
The Release body contains the reviewed cumulative 0.3.5/0.3.6 notes and the
local installation evidence limits. This is publication verification, not
fresh-task or natural-behavior verification.

## v0.3.6 publication gate

The publication source must retain the accepted five-file package tree
`3e5e3f6463ad582e1279a94e27c36b07225127e2`. The full outgoing diff,
including untracked candidate and mapping files, requires independent commit
review after the current documentation and Release body are stable. SOURCE
and repository/provenance checks must pass on those final bytes. Fast-forward
main, annotated tag, Release target/body/state and any post-publication records
are separate observed results, not implied by local source checks. The frozen
v0.3.0 `CHANGELOG.md` cannot be rewritten as a 0.3.6 note without invalidating
historical evidence.

## Unreleased 0.3.6 verification

The current 0.3.6 entrypoint links to the existing Native reference's Runtime
Readiness procedure. The five-file shape and the retained 0.3.5 evidence below
are unchanged. Current SOURCE, repository/provenance, focused boundary and
managed-install checks bind the v0.3.6 candidate and source map; test results
are distinct from installation evidence. SOURCE passed 14/14 checks, the
repository/provenance check passed 44 mapped files, the focused boundary
checker passed 59 assertions on each of PowerShell 7 and Windows PowerShell
5.1, metadata validation passed, and the disposable managed lifecycle self-test
passed for 0.3.6. All returned terminal exit 0. The current managed-install
dry run bound source identity and target tree without applying a write.

The independent cold R1 inspected the cumulative actual diff, four untracked
candidate/map identities, necessary consumers and source checks, with no
actionable finding. Automatic approval rejected the first two exact update
attempts before process start, including one after a direct readback of the
original user authorization. A direct user reply in the action task then
authorized the exact managed update and ACL check. That one update installed
MANAGED 0.3.6 and produced five source-matching files and a valid receipt.

The update wrapper returned exit 1 because its exact-SDDL postflight found
Windows-reordered inherited allow ACEs on eight nodes. Read-only follow-up
confirmed unchanged owner/control fields and the same allow ACE multiset on
all nine nodes; the root SDDL was exact. No further ACL mutation was made.
Ordinary sandbox access read all five files and the receipt, with 5/5 hashes
matching the 0.3.6 candidate. The complete old package, receipt, ACL record
and rollback source are retained outside discovery roots; the 0.3.6-to-0.3.5
manager rollback dry run passed with terminal exit 0. The same independent R
reviewed these permission and installation results without a new finding.
Fresh-task loading and
natural adherence remain `UNKNOWN`.

## Retained 0.3.5 verification

That checkpoint's subject was the bounded timestamp-guidance source revision.
SOURCE passed all 14 existing checks, followed by the repository binding check
with 42 mapped files; metadata validation passed. The existing PowerShell
checker passed 59 assertions on both PowerShell 7 and Windows PowerShell 5.1
with the updated package pin. These results have terminal exit code 0.

A separate synthetic method sample passed 13 assertions on PowerShell 7.6.3
and 7 on Windows PowerShell 5.1. The former returned DateTime by default,
preserved the raw strings with `DateKind String`, and retained explicit offsets
with `Offset`; the latter had no `DateKind` parameter but its default parser
preserved the sample strings. Equivalent offsets, the open lower and closed
upper endpoints, and the timezone-free coverage gap were verified from the
explicit original values. This does not generalize a parser guarantee to
unexamined inputs or turn parameter absence into a required shell upgrade.

The first 5.1 sample failed before timestamp assertions because the temporary
harness wrapped its array result as one pipeline object. A read-only probe
isolated that representation difference; direct-assignment normalization
corrected the harness. The failed result remains evidence and did not justify
changing the package scope. Independent read-only R1 inspected all 15 changed
paths, the full reconstructed diff, 41 baseline and 43 candidate identities,
necessary semantic context and the exact-target application script. It returned
no actionable findings. The primary maintainer's mechanical record closeout
changes only State, Verification and their source-map bindings; package,
candidate and other reviewed inputs remain unchanged. Repository binding is
refreshed for those records before exact source application and readback.

The first real application stopped at its Git ownership preflight before any
source writes. A command-scoped trust setting for the exact fixed repository
address resolved that execution boundary without changing Git configuration.
The same independent reviewer inspected the complete one-line application
script difference and record closeout as R2, with no findings. The reviewed
application then returned exit code 0 and verified all 43 source file hashes.
Only State, Verification and their source-map bindings change in the final
records-only closeout; package and other reviewed source inputs are unchanged.

The source delivery did not include installation. A subsequent, separately
authorized local update received independent R3 review with no findings.
Review covered the exact target and source bindings, package and receipt,
link and path checks, all nine nodes' owner and permissions, retained recovery
input, the one-use application marker, same-volume directory replacement and
bounded failure recovery. Ordinary access to the private preparation evidence
was denied; an authorized read-only inspection confirmed the prepared inputs
and unchanged live copy. That denial remains preparation evidence.

The actual update and ordinary-reader postflight both completed with exit
code 0. Status is MANAGED 0.3.5, package tree
`e92783850c3a26c6427e8b1bf7742e702b5aaae2`, and receipt SHA-256
`f1e4afb9c72b3099e9dc4e38939a64e9631cdf24e7a3d1572e09333c04c600b7`.
All five installed files match the source package; nine nodes' original owner
and permissions and the destination parent context are preserved. The old
0.3.4 package, receipt and permission recovery input remain outside discovery
roots. The final records-only closeout updates State, Verification, both README
languages and their source-map bindings; reviewed package bytes are unchanged.

No new model qualification, host-setting change or full historical
lifecycle/adversarial matrix was run. Passing deterministic checks, installation
or a written case does not establish fresh-task loading or natural model
adherence. Prior 0.3.4 evidence below retains its original scope.

## v0.3.4 publication verification

SOURCE 14 checks and repository 40 mapped files passed for the final publication
input, with terminal exit code 0. Where applicable, SOURCE preceded repository
validation; actual-source checks after applying reviewed records also passed.
The complete diff and Release notes received independent read-only review.
R1 identified PUB-R1-01 (P2): the new PowerShell Release linked to
missing lifecycle trust instructions. Both README languages now describe
independent current/target trust, exact source, dry-run and apply, and
recovery limits. R2 closed the finding with no new findings.

Reviewed source was committed as `08ee94624254ddeff750ead062358108d15d10f3`. Staged blob identity,
the commit's package tree `0547154333ea4da6ed307b851becad6c8b52c9b4`, and clean postcommit
working-tree state were verified. The public annotated tag and Release were
created with the approved version and read back against the exact commit.
Title and body matched the reviewed notes (normalizing line endings and final
newlines); the Release was public, non-prerelease and Latest, with old tags
unchanged. [State](STATE.md#v034-publication) owns public identities.

This closeout changes existing publication records and their mapping/checker
consumers only. Package, installer, historical candidates, tagged source and
published notes retain their bytes. No additional installer lifecycle, model,
fresh-task loading, cross-Harness or efficacy result is claimed.

## Current verification selection

Read the existing owner for the current decision and reuse unchanged reads.
Run the repository check once against the final candidate when mapped content,
package bytes or provenance change. Select focused SOURCE, metadata, behavior,
lifecycle or adversarial checks for the mechanism actually changed; repeat only
for changed inputs, failures, explicit applicable gates or material risks.
An ordinary text or repository-guidance edit alone does not require a complete
installer or historical adversarial matrix. Actual installation retains its
identity, permission and postflight checks, and frozen prior contracts retain
their original gates. Historical results below are not fresh runs by implication.

The earlier repository-guidance refinement changed AGENTS and documentation;
the already checked package description revision retains its existing bytes
and version at that checkpoint. Final repository checks passed on that source
with 40 mapped files. Independent review found no unresolved findings in
this refinement. Earlier paired installation attempts were rejected before
process creation and remain retained evidence. After direct user approval,
the reviewed local update and ordinary-reader verification completed with exit 0;
current identity, permissions and recovery evidence are recorded below.

## Accepted migration baseline

- Source commit: `80910a8b2375a11be897e9660c4b00a06d00dd13`
- Package path: `skills/use-powershell-safely/`
- Package files: 5
- Provenance manifest: [`../../../provenance/source-map.json`](../../../provenance/source-map.json)

## Local v0.3.0 candidate qualification

Candidate C preserves package tree
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`, which is exact at source package
commit `985e0d21ab1633c642a86826a86773f700ade729`, migration source commit
`80910a8b2375a11be897e9660c4b00a06d00dd13`, and the independent repository
baseline. [`../../../release/v0.3.0-candidate.json`](../../../release/v0.3.0-candidate.json)
binds the package, future public identity, evidence states, release-note review,
and verification commands.

Historical `c42eef3...` exact-commit model/loaded-copy evidence is not
admissible for the `v0.3.0` candidate's SOURCE-forward behavior because its
package tree is `22c230...`, not candidate tree `7e1077...`. That candidate
tree's historical 59-assertion deterministic evidence is retained only as
bounded SOURCE history.

Accepted Q04 is one fresh projectless, read-only, no-tool
`gpt-5.6-sol/high` qualification against exact candidate C. The frozen request
payload SHA-256 is
`cfa75604ca5dbf49f6f5f7452e9c9dfe6eb927981ac6028c08d9dd7b602f538c`,
the controller-only rubric SHA-256 is
`63621cb8c6d2e625b8fbeabbe51ea007bc828ce0bb05c7a32cc2dbae506273f8`,
and the single final response SHA-256 is
`8fba2576f76755e77d848574b60e19b2276d378e5e5de46027b9dcd97774c085`.
The retained controller evidence contains one user-visible turn, two reasoning
records, one final message, and zero tool events. It passed only the frozen
PowerShell native/JSON positive, ordinary-cmdlet negative, and POSIX-only
negative scenarios. Private task, turn, message, host, prompt, and checkout
locators remain controller-side rather than tracked.

Q01 remains sealed as `QUALIFICATION_FAILED/TRANSPORT_TERMINAL` and Q02 as
`ESCALATION_DENIED`; both have behavior `UNKNOWN_NOT_ASSESSED`. Q03 remains a
sealed preflight stop with no SOURCE transmission or behavior result. None is
retryable or evidence of a product defect.

The deterministic SOURCE contract checks exact five-file shape and tree,
strict UTF-8/LF/no-BOM bytes, pre-error positive and narrow negative selection
contracts, native identity/arguments/streams/exit boundaries, permission and
destructive stops, text/hash/cross-shell rules, and Windows/WSL identity and
state gates. The lifecycle self-test uses a disposable temporary root and
exercises dry-run, install, update, rollback, drift refusal, foreign-copy
refusal, and uninstall. It does not create persistent installed-copy evidence.

The public-source descriptor
[`../../../release/v0.3.0-public-release-candidate.json`](../../../release/v0.3.0-public-release-candidate.json)
records the exact repository identity, public default branch, intended
annotated tag, public non-draft/non-prerelease Release settings, exact
release-note hash, B1 receipt lineage, and unchanged package tree/digest. The
SOURCE checker verifies that local descriptor contract. It does not prove a
public ref, tag, GitHub Release, persistent lifecycle effect, or installed-copy
behavior; those require later live evidence bound to exact public source P.

## Public v0.3.0 and stable-copy qualification

Exact public source P is commit
`13edb84cd1b072cb64926c5ae600714c6f7203e7`, tree
`6f03b9a5717f823f87d117fc17b5040e0531dcc8`, with unchanged package tree
`7e10775d423bfb08bc4ad6388875b7277ce3c18c`. Annotated tag object
`58cd1276ad43589c93489c919c285ce7fec2d42d` peels to P. GitHub Release id
`378386983` is public, non-draft, and non-prerelease; its exact title/body were
human-approved and its normalized LF body SHA-256 is
`5c8c787136fd490aebd3b465e8687f59a68863da8d14bd62a92ee624f78b764f`.

The repository-native lifecycle route used an immutable public `v0.3.0` clone
and exact explicit destinations. It verified managed install, same-version
update, same-version rollback, origin-aware uninstall and absence, then public-
source restoration. The final installed package tree is the public package tree
and its origin-aware receipt SHA-256 is
`640a38a072c02ed8e8a1bd7c6bb256c7dd709e0b16ebca033a16a92a18eed659`.
The pre-existing exact public legacy copy is retained byte-unchanged outside
all Skill discovery roots; its private recovery locator stays controller-side.

`B2-PS-ABSENCE-01` is one fresh projectless witness for exact former USER-origin
absence after uninstall. `B2-PS-LOAD-01` is a separate fresh projectless witness
for sole exact-name USER-scope discovery, exact package/receipt identity,
complete five-file load, and the bounded PowerShell native/JSON positive,
ordinary-cmdlet negative, and POSIX-only negative scenarios. Both retained
evidence tasks, prompts, and outputs remain controller-side. The public
[`evidence subject`](../../../release/v0.3.0-public-release-evidence.json) binds
only publication-safe ids and hashes. The Planner accepted exact subject F
`21eca7724a84b4073c98c68e548b1816c52a0ff0`, tree
`a53e693d29d33dddd6bb673ba3f54a2fcedbfe54`, at public evidence id
`B2-PS-PUBLIC-EVIDENCE-F-01`.

## Retained 0.3.2 source and local installation

The retained `0.3.2` package has tree
`f76f6deaec88101ecdda4c5dbc47405d8b930a65` and digest
`bdbbe8e85e5d5d086c1f6fc4f760f1e5868b4803f54278080d80c6d987bc1d0b`.
It changes `SKILL.md` and the Native/Text references relative to the retained
managed `0.3.1-local.3` package tree
`2b1c9fd648bfa7c9b1368d9ca2229501f99e388c`; the agent metadata and Windows/WSL
reference remain byte-identical. The PowerShell boundary case has matching
eval changes. The user confirmed `0.3.2` and its USER installation is now
verified below. No new model qualification, publication, or fresh-task
runtime-consumption claim is attached to this source.

The accepted source-only checkpoint was checked with:

```powershell
python -B "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\use-powershell-safely
git diff --check
python -B scripts/check_source_contract.py --json
python -B scripts/check_repository.py --json
pwsh -NoLogo -NoProfile -NonInteractive -File evals/check-powershell-boundaries.ps1
```

- Skill structure validation and `git diff --check` pass.
- Every non-identity SOURCE contract check passes, including exact five-file
  shape, strict UTF-8/LF/no-BOM, narrow positive/negative selection, Native,
  Text, permission/destructive, and WSL contracts. The command still exits
  nonzero for the frozen candidate, receipt, public-source, and public-evidence
  identities.
- Read-only PowerShell Core 7.6.3 examples confirm premature outer expansion
  in a nested `pwsh -Command` payload, quoted versus unquoted Git
  `--format=%(refname)`, guarded empty-name JSON hashtable representation, and
  explicit strict Python UTF-8 subprocess decoding with optional process-local
  `-X utf8`.
- Repository verification exits nonzero only for mapped target/source/hash/blob
  identity differences caused by the authorized working changes.
- The focused checker stops at its first frozen package-manifest identity gate.
  No later focused assertion ran, so none is reported as passing for the
  current source.

These results are content and example evidence, not successor qualification.
The frozen candidate, receipt, source map, and public evidence remain unchanged.

### Local installation verification

The existing `manage_install.py` accepted explicit trusted old and new package
trees for a private frozen `0.3.2` installation snapshot. A rehearsal in a
directory outside discovery roots completed old-package install, update to
`0.3.2`, and rollback to `0.3.1-local.3`. The live update completed with exit 0
and `MANAGED`; live rollback was checked in dry-run mode only. The old five
files and original receipt remain retained outside discovery roots.

SOURCE-list digest is
`bdbbe8e85e5d5d086c1f6fc4f760f1e5868b4803f54278080d80c6d987bc1d0b`;
installer-mapping digest is
`ff909615ea97bcc60dad59b66a6d2ee5cdf3b2ac6620aec7e6c98615001b6003`.
A preparation assertion initially compared these different serialization
contracts and failed before any copy or installation. Correcting the private
assertion preserved both production algorithms and exact file identities.

After installation, ordinary sandbox reads initially failed with access denied:
the staged directory had a protected ACL. Following explicit approval, parent
ACL inheritance was enabled only on the exact installation directory, retaining
existing entries. The same verification then completed in the ordinary sandbox
with exit 0: all five files and receipt readable, all file hashes equal to
source, strict UTF-8/no-BOM/LF checks passing, `MANAGED 0.3.2`, and rollback
dry-run accepted. The receipt hash is recorded in State. The installer still
creates protected staging directories on this observed route; future updates
or rollback must verify readability and cannot inherit this run's success.

This is byte/readability and bounded local lifecycle evidence. No fresh-task
discovery or model-load/behavior run was performed. Historical identity-gate
failures remain failures; they were not converted to qualification PASS.

## Retained 0.3.2 verification entry points

The user authorized a current candidate and a separate current source map while
retaining the original map and four `v0.3.0` release objects byte-for-byte.
`check_source_contract.py` checks the historical objects against their original
package identity, verifies their frozen bytes, and independently checks the
current `0.3.2` candidate and accepted five-file package. Its current 14 checks
pass; the earlier four identity failures remain part of checkpoint history.
During this update one intermediate run still used current tree values in two
historical public-evidence comparisons and failed; those comparisons now use
the historical tree, with no historical-file mutation.

The focused script pins the current package manifest and has completed all 59
assertions on both PowerShell 7 and Windows PowerShell 5.1. The existing
`manage_install.py self-test --source .` now defaults to independently trusted
`0.3.2` and completes its disposable lifecycle. For an exact historical source,
`--expected-version 0.3.0` retains the old self-test subject. Production
install/update/rollback trust and ACL behavior are unchanged.

Repository adversarial tests use the complete staged index. They retain the
existing mapping/privacy/path cases and add current candidate/tree and frozen
history rejection cases. Run the producer staging step before this consumer;
prior empty-index or pre-manifest runs provide no current adversarial evidence.
The current complete staged-index matrix completed with exit 0 and every case
passing. Its external-link sentinel used the deterministic index-link-mode
branch, not a real host symlink. This adds checker rejection evidence, not model
qualification or new installed-copy behavior.

## Retained 0.3.4 verification subject

The user-confirmed revision shortens only the catalog description, preserving
pre-command material-boundary and diagnostic triggers and ordinary-task
exclusions. SKILL.md body and all other package files remain byte-identical
to 0.3.3. The 0.3.4 candidate and source map bind this new input; existing
SOURCE, repository, focused PowerShell and disposable lifecycle checks follow
that identity. Production install/update/rollback and historical trust remain
unchanged. Local verification on 2026-09-12 returned terminal exit code 0
for SOURCE (14 checks), repository validation (40 mapped files), Skill Creator
metadata validation, PowerShell 7 and Windows PowerShell 5.1 (59 focused
assertions each), and the disposable 0.3.4 lifecycle self-test. The self-test
reported no persistent effect. Package-body comparison confirms the remaining
four files and SKILL.md body are unchanged. Independent read-only technical
review inspected the bound 14-path source candidate and found no actionable or
blocking findings. The primary owner accepted the source delivery. Application
of the reviewed source returned exit 0; SOURCE and repository checks also
returned exit 0 at the actual source root.

A separate installation-preparation review confirmed the new five-file package
and receipt against the old managed installation: all nine staged/live nodes
matched their expected bytes, strict UTF-8, owner and full security descriptor.
The same-filesystem swap plan retains the old copy outside discovery roots.
Earlier temporary preparation failures are retained: a parser rejection, a
restricted-token Set-Acl failure, and inherited-permission mismatches. The final
preparation copied the existing Skill-parent permission model only to a new
staging parent and then matched the complete original descriptors. Actual Skill
files and parent permissions were not changed by preparation.

Earlier automatic approval reviews rejected the real update before process
creation, citing the need for direct user installation authorization. Those
attempts performed no live rename or new receipt and remain retained evidence.
After direct user approval, the same reviewed update and ordinary-reader
verification each completed with terminal exit 0. All nine nodes and the full
0.3.3 backup match their expected bytes, owners and security descriptors.
Native status is MANAGED 0.3.4, tree `0547154333ea4da6ed307b851becad6c8b52c9b4`,
installer mapping digest `057eedc74067dfa5915233bb6274f3e2f222bb9bde6605bdbd426be09d6d0806`.
Fresh-task selection, loading, model behavior and cost improvement remain UNKNOWN.

## Retained 0.3.3 verification subject

The current source tree is `842b87d85c151a9c944cb855123c0ce7d69be1e5`, with
SOURCE-list digest `461cb805672dbe3bda67151227692845a34e0c6ddbf2a88c29d4b733c6aea478`.
`release/v0.3.3-candidate.json` and `provenance/source-map-v0.3.3.json` bind
this source-assessment snapshot; the old `0.3.2` candidate/map remain unchanged.
The same SOURCE, repository and focused checks now target `0.3.3`. Lifecycle
self-test defaults to its independently pinned tree; exact old sources retain
explicit `--expected-version 0.3.0` and `--expected-version 0.3.2` routes.
Production install/update/rollback and ACL handling are unchanged.

The existing scenario case now distinguishes preparation, failure diagnosis,
unchanged-runtime reuse, changed-condition rechecking and routine-call exclusion.
These scenarios need independent content assessment; deterministic checks alone
do not prove actual model selection, loading, behavior or efficacy. Independent
source acceptance preceded the USER `0.3.3` update. Management-context checks
verify exact source bytes, receipt and managed status. Ordinary-sandbox checks
also pass after separately approved exact-root ACL inheritance repair, with the
initial failure preserved below.

At this source checkpoint, Skill structure validation, SOURCE's 14 checks,
repository verification for 38 mapped files, both PowerShell runtimes' 59
focused assertions, and the disposable `0.3.3` lifecycle self-test pass. The
lifecycle result explicitly reports no persistent effect. These results do not
relabel earlier failed checkpoints or establish USER installation usability.

### 0.3.3 same-location update and readability verification

Preparation verified the old `0.3.2` tree and receipt, retained both outside
discovery roots, and bound the accepted `0.3.3` source snapshot and distinct
SOURCE-list/installer-mapping digests. Update dry-run passed. One live managed
update completed with exit 0 and returned the accepted tree plus installer
mapping digest `ec5e05c5a144285952f05a7e31935e2d16efa3831bcf5de3286681ce4d763d9c`.

Ordinary-sandbox verification exited 1: all five package files and receipt
returned permission denied. A separate management-context read-only check
exited 0 and verified every accepted file hash, strict UTF-8/no-BOM/LF, receipt,
`MANAGED 0.3.3`, retained `0.3.2` recovery bytes and rollback dry-run. Receipt
SHA-256 is `a8e004e9e00887bfb76555bd8c56e0a6a26d5893bec6a6651447680d1de23c48`.
Privileged readability does not replace the failed ordinary-sandbox result.

Read-only ACL inspection found the replacement root's inheritance protected;
the parent still supplies sandbox read permission. Following separate explicit
approval, inheritance was enabled on that exact root only, preserving explicit
entries, without a recursive switch or changes to the parent. The command exited
0 with one directory processed and zero failures; inheritance is now enabled.
The same verifier then exited 0 in the ordinary sandbox: all five files and
receipt readable, exact accepted hashes, strict UTF-8/no-BOM/LF, `MANAGED 0.3.3`,
retained recovery bytes and rollback dry-run passed. The receipt hash is unchanged.
The earlier failed run remains failure evidence. No second installation, live
rollback or fresh-task model run was performed. Independent assessment accepted
the exact source and local installation after separately checking ordinary-
sandbox bytes, receipt, managed status, ACL inheritance and retained recovery
identity. This acceptance adds no fresh-task loading or model-behavior evidence.

### Retained two-commit push completion

After separate explicit user approval, read-only checks confirmed the original
actor, repository and `main` baseline, with exactly the two already-reviewed
commits `9dccf92af9dbea3a84f551f47eb7088880be5688` and
`92ad426f3bfc358a8df21fe633264edffbb994c0` in the fast-forward range. One
normally approved non-force Git push exited 0; a separate remote-ref read
confirmed `main` at `92ad426f3bfc358a8df21fe633264edffbb994c0`.
The original pre-process approval rejection remains history. No new `0.3.3`
commit, tag, Release, PR, history rewrite or cleanup was performed.

## Repository check

```powershell
python -B scripts/check_repository.py --json
```

This verifies exact Git-blob identity for unchanged exact inputs, rewritten
target hashes and retained original source mappings, expected package and
evaluation shape, UTF-8/BOM and Markdown-link boundaries, and publication safety.
The default route uses `provenance/source-map-v0.3.6.json`, checks its pinned
source-mapping projection, and separately verifies the frozen historical map and
release objects. It does not assume the former source repository is present.
An identity mismatch is a failing current check, not an accepted closeout state.

When the exact source Git object store is available during migration audit, run:

```powershell
python -B scripts/check_repository.py --json --source-repository <source-git-repository>
```

That explicit route resolves the recorded commit/tree and proves every mapped
source path, Git blob, and raw or normalized SHA-256 directly from Git objects;
it never reads source working-tree bytes.

## Adversarial checker matrix

```powershell
python -B scripts/check_repository.py --adversarial
```

This builds every disposable repository strictly from staged Git-index blobs;
working-tree, ignored, untracked, cache, and link-target bytes are not copied.
The admitted publication-classifier input domain is the UTF-8 text of mapped
repository files plus every string value consumed from the v2 provenance
manifest. Manifest paths remain strict POSIX repository-relative paths. Within
that domain, the locator grammar is limited to direct absolute Windows drive
profiles, direct/device UNC locators, and `file:` URIs that resolve to those
forms after exactly one percent-decoding pass. One separator/prefix
canonicalization handles equivalent slash forms and repeated leading
separators in direct and `file:` representations; explicit non-`file:` URIs,
repository-relative paths, POSIX
`file:` paths, and non-profile Windows roots remain portable. Locator-like
`file:` or UNC forms that cannot be classified unambiguously after that pass
fail closed, including `file:` candidates whose raw query or fragment
delimiter or raw-space token boundary would make the local path representation
ambiguous, and candidates whose percent escapes are not valid UTF-8. Direct UNC
forms with a server but no share also fail closed; the
portable `//` syntax-text partition requires no server token. This policy
protects the existing no-private-locator publication
contract; it does not promise another URI or filesystem grammar.
The finite fail-closed matrix covers drive-rooted private Windows profiles with
backslash, forward-slash, and mixed separators; ASCII-space and Unicode profile
names; end-of-string and deeper paths; and recognized device-drive prefixes.
It also covers ordinary, device, and extended UNC locators after one canonical
separator/prefix normalization. A shared structured UNC parser requires
nonempty server and share components, accepts Unicode and internal spaces, and
rejects controls and Windows-invalid component characters. Portable explicit
non-file URI, relative, embedded-drive, empty-profile, singular-root,
syntax-text, POSIX, and non-profile-root partitions remain accepted. A
URI-aware standard-library layer parses `file:` candidates,
decodes percent escapes once, and routes local-drive, `localhost`, UNC-authority,
drive-authority (including a once-decoded drive-rooted authority remainder),
and encoded device-drive representations through the same path predicates;
HTTP/HTTPS, other schemes, non-profile Windows roots, POSIX paths, bare schemes,
and empty-profile forms remain portable. Git-index snapshots remove inherited
`GIT_*` selectors case-insensitively, reintroduce only disabled optional locks,
and use an explicit repository route; a disposable hostile-selector matrix
proves both `ls-files` and `cat-file` stay bound to the intended repository.
The matrix also covers invalid UTF-8 and unpaired-Unicode-surrogate structured failure, manifest
identity and rewrite-source schema, exact-blob source SHA-256 verification,
top-level source-commit/source-tree identity, and a checker-pinned canonical
digest of every destination-to-source identity mapping. Exact tree membership
is established only by the explicit source-object audit above;
manifest duplicate-key rejection, top-level `manifest_provenance` source-record
schema/path validation, decoded-key/value publication safety, unsafe
destinations, source paths free of Unicode General_Category `Cc` controls
(covering C0, DEL, and C1 while preserving other admitted Unicode categories),
missing mapped content, the legacy
reparse fallback, and rejection of link-like source-repository ancestors. An external-link
sentinel proves that a link entry is rejected before its target blob is read or
copied; the result identifies whether the current host also created a real
disposable symlink or used the deterministic index-link-mode branch.

## Focused check

```powershell
pwsh -NoLogo -NoProfile -NonInteractive -File evals/check-powershell-boundaries.ps1
```

For current `0.3.6`, this command verifies its pinned package manifest and then
runs all focused assertions. The earlier checkpoint stopped at the old package
manifest gate and did not run its later assertions.

## Evidence limits

The focused suite is synthetic and local; accepted Q04 adds bounded
candidate-tree SOURCE-forward behavior for three frozen scenarios. Separate public and
projectless evidence proves the exact public source, Release, same-version
lifecycle, origin-aware absence, stable installed-copy identity and bounded
loaded-copy behavior. It does not prove cross-version lifecycle, live WSL,
cross-Harness behavior, untested contexts, or broad product efficacy. The
Planner accepted the exact public-release evidence subject. The retained
`UNKNOWN` layers are unchanged.
