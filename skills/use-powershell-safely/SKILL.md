---
name: use-powershell-safely
description: Diagnose and safely execute material Windows shell boundaries across PowerShell, native executables, text, permissions, and WSL. Use before the first relevant command when a non-trivial PowerShell workflow has a material parser, version, argument, stream, encoding, path, permission, destructive filesystem, process, or WSL boundary, or when symptoms such as NativeCommandError, misleading exit status, missing output, quoting drift, byte mismatch, sandbox denial, or cross-shell transport require diagnosis. Do not use for ordinary version-independent cmdlets, simple documented native calls with no boundary symptom, general Windows work, or POSIX-only work.
---

# Use PowerShell Safely

Treat the shell boundary as part of correctness. Use this skill as the minimum
combination of boundary diagnosis and safe execution guidance, not as a general
PowerShell tutorial or an automatic system installer.

## Select Before The First Risk Command

- Select this Skill before generating or executing explicit non-trivial
  PowerShell when a material parser, parameter, version, argument, stream,
  encoding, path, permission, destructive filesystem, process, or WSL boundary
  is present. Do not wait for that boundary to fail.
- Strong pre-error cues include a `.ps1` deliverable, a `pwsh` or
  `powershell.exe` invocation, multiline logic, loops, `try`/`catch`, regex,
  hashtables or object construction, complex pipelines, native or child
  processes when they make one of those boundaries material.
- Treat destructive filesystem work as a material boundary and select before
  generating or executing it. Authorization and literal-target containment
  remain separate requirements.
- Keep an ordinary version-independent cmdlet with no boundary risk or symptom,
  a simple documented native call with no boundary symptom, general Windows
  work, and POSIX-only work outside the Skill.

## Prepare The Command Before Execution

- Put loops, `try`/`catch`, regex, hashtables, object construction, or complex
  pipelines in a `.ps1` file when practical. If inline PowerShell is required,
  parse the exact payload without executing it in the same PowerShell
  executable and version that will run it, and stop on any parser error.
- Do not repair complex inline code by adding `cmd.exe`, another PowerShell
  process, encoded transport, or another quoting layer.
- Check the target cmdlet or script's actual parameter set before reusing a
  familiar path parameter. `-LiteralPath` is not universal: `New-Item` exposes
  `-Path`, not `-LiteralPath`.
- For a critical cmdlet step, use a narrow terminating contract such as the
  supported `-ErrorAction Stop` plus `try`/`catch`, then verify the expected
  artifact or state. A later successful command or outer exit `0` does not
  erase a non-terminating cmdlet error. `$LASTEXITCODE` belongs to a native
  process contract, not a cmdlet failure contract.
- Before execution, check variable-name boundaries such as `${name}:`, use a
  non-interpolating representation when regex must contain literal `$env:` or
  `$script:`, do not reuse automatic `$Matches` for an application collection,
  and collect statement-form `foreach` output before piping it.
- Read [Native And Process Boundaries](references/native-process-boundaries.md)
  for parse-only examples and the detailed parameter and error contracts.

## Start With Runtime And Boundary Readiness

- Do not run a version probe for every routine cmdlet. Probe when the task
  materially depends on text encoding, native argument passing, stream
  behavior, WSL transport, or PowerShell-version compatibility.
- Inspect the current edition, version, and executable before relying on
  version-specific behavior:

```powershell
$PSVersionTable.PSEdition
$PSVersionTable.PSVersion
$PSHOME
@(
    Get-Command pwsh -CommandType Application -All -ErrorAction SilentlyContinue
)
```

- Prefer a supported PowerShell 7 release for modern UTF-8, native-command, and
  WSL workflows when the target modules and scripts are compatible. Keep a
  Windows PowerShell 5.1 path when a legacy module or host requires it.
- If no usable `pwsh` exists and the current task would materially benefit from
  PowerShell 7, explain the task-specific benefit, note that 7 installs
  side-by-side with 5.1, and ask whether the user wants the official
  installation path. Detection alone never authorizes installation.
- Read the runtime-readiness and installation sections in
  [Native And Process Boundaries](references/native-process-boundaries.md)
  before calling a resolved executable usable or recommending a version or
  installation method. Resolution, launch, probe output, and support status are
  separate facts.

## Classify Evidence Before Generalizing

- Treat documented platform behavior and a reproduced version boundary as
  portable guidance.
- Treat a failure seen on one host as a bounded hypothesis until the mechanism,
  prerequisite, and affected versions are established. State the uncertainty
  instead of turning one observation into a universal PowerShell rule.
- Treat exact executable paths, installed versions, account or distribution
  names, environment-variable values, `PATH` order, package provenance,
  sandbox identities, and current host state as local evidence. Verify them on
  the active host and do not expose unrelated values.
- Generalize the diagnostic question or safe command shape, not the private
  host answer.

## Load Only The Relevant Detail

- Read [Native And Process Boundaries](references/native-process-boundaries.md)
  for cmdlets versus native executables, versions, arguments,
  `NativeCommandError`, streams, pipelines, `ProcessStartInfo`,
  `Start-Process`, permissions, destructive operations, or PowerShell 7
  installation guidance.
- Read [Text And Encoding Boundaries](references/text-encoding-boundaries.md)
  only when text bytes, UTF-8, BOM, newline, JSON/schema, hashes, non-ASCII
  content, or a legacy code page may matter.
- Read [Windows And WSL Boundaries](references/windows-wsl-boundaries.md) only
  when execution, paths, data, or state crosses between Windows and WSL.

## Diagnose In Order

1. Identify the current PowerShell edition and every parser, process, encoding,
   path, permission, and WSL boundary involved.
2. Establish one explicit working-directory or tool-root base for each relative
   path, and normalize uncertain pipeline or discovery output before indexing
   it or selecting an executable.
3. Reproduce the failure with the smallest read-only command that preserves the
   suspected boundary.
4. Establish the command contract: supported cmdlet parameters and PowerShell
   object/error semantics, or native arguments, stdout, stderr, and exit
   status.
5. Prefer a direct cmdlet or `& $exe @args`; move complex multi-line logic into
   a script for the shell that owns it.
6. Inspect exact bytes only when text encoding, BOM, newline, or byte identity
   is relevant.
7. Capture `$LASTEXITCODE` immediately after a native program whose contract is
   exit-status based; never substitute it for a cmdlet error contract.
8. Classify the result as application defect, argument or parser transport,
   stream or exit handling, text encoding, WSL or path semantics, environment
   drift, sandbox or permission, cleanup noise, or still unknown.
9. Change application code only when the direct, correctly transported
   reproduction demonstrates an application defect.

## Emit A Complete Native Shape

When a user-runnable native example discovers an executable, carry candidate
identity, argument structure, stream semantics, and exit status through the
example instead of showing only the happy-path invocation:

```powershell
$candidates = @(
    Get-Command $commandName -CommandType Application -All `
        -ErrorAction SilentlyContinue
)
if ($candidates.Count -ne 1) {
    $candidates | Select-Object Name, Path, CommandType
    throw "Expected one application candidate; found $($candidates.Count)."
}

$exe = $candidates[0]
$nativeArgs = @('--input', $inputPath)
& $exe.Path @nativeArgs
$exitCode = $LASTEXITCODE
```

Use a documented precedence or identity rule instead of the exact-one check
only when the task actually provides one. The direct form above inherits the
console streams; it does not capture stdout and stderr separately. When their
distinction is material, including when the user asks what each stream
contains, show the tool's independent output-file options or an explicitly
redirected process API. Never claim separate capture unless the example and
evidence actually preserve both streams.

Before using a version-specific command or API, report the observed
PowerShell edition/version and verify the required capability; a
`PowerShell 7` label is not runtime evidence. When the current host is
available, run the read-only runtime and capability probes and report their
results before offering the version-specific command. Merely placing probes in
a command the user could run later is not observed evidence. If execution is
unavailable, keep the runtime unknown and present the command as a guarded
option rather than a verified host-compatible shape.

Keep every other material branch in the answer. If the task also raises JSON,
encoding, BOM, newline, or byte identity, load the text reference and close
that hypothesis with an explicit decode, parse, or byte check that matches the
actual producer and consumer contract. Do not infer file validity from a
transport fix or parse a plain-text status as JSON.

## Stop And Ask

- Obtain explicit authorization before installing or updating PowerShell,
  elevating, downloading packages, changing profiles or execution policy, or
  modifying system locale, code page, registry, firewall, services, WSL state,
  or other system configuration.
- Stop for organizational policy, unavailable package tooling, required
  administrator approval, an incompatible legacy module, or uncertainty about
  the intended installation scope.
- Before destructive recursion, resolve every target to an absolute literal
  path and prove it stays inside the intended root. Keep enumeration and
  mutation in one shell.
- Do not expose credentials, tokens, cookies, private keys, environment-file
  contents, or unrelated host paths.
- Do not retry with more parser layers, broader permissions, or a riskier
  transport until the failure is classified and the added authority is
  justified.

Report the observed runtime, failing boundary, evidence, safe command shape,
authorization status, and remaining uncertainty.
