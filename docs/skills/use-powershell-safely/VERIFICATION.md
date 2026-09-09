# Use PowerShell Safely Verification

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

## Current 0.3.2 source and local installation

The canonical working package now has tree
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

## Current 0.3.2 verification entry points

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

## Repository check

```powershell
python -B scripts/check_repository.py --json
```

This verifies exact Git-blob identity for unchanged exact inputs, rewritten
target hashes and retained original source mappings, expected package and
evaluation shape, UTF-8/BOM and Markdown-link boundaries, and publication safety.
The default route uses `provenance/source-map-v0.3.2.json`, checks its pinned
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

For current `0.3.2`, this command verifies its pinned package manifest and then
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
