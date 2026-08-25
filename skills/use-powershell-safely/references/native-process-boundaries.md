# Native And Process Boundaries

Use this reference for PowerShell runtime readiness, cmdlet/native distinctions,
arguments, stdout/stderr, exit codes, pipelines, process APIs, permissions,
destructive operations, and PowerShell 7 installation guidance.

## Contents

- [Runtime Readiness](#runtime-readiness)
- [Installation Is A Separate Authorized Action](#installation-is-a-separate-authorized-action)
- [Parse Complex PowerShell Before Execution](#parse-complex-powershell-before-execution)
- [Cmdlet Or Native Executable](#cmdlet-or-native-executable)
- [Cmdlet Parameters And Failure Contracts](#cmdlet-parameters-and-failure-contracts)
- [Command Discovery And Result Shape](#command-discovery-and-result-shape)
- [Native Errors And Preference Variables](#native-errors-and-preference-variables)
- [Preserve Native Arguments](#preserve-native-arguments)
- [Complete User-Runnable Examples](#complete-user-runnable-examples)
- [Streams, Pipelines, And Redirection](#streams-pipelines-and-redirection)
- [Process APIs](#process-apis)
- [Paths, Permissions, And Destructive State](#paths-permissions-and-destructive-state)
- [Junction And Reparse-Point Removal](#junction-and-reparse-point-removal)
- [Official Sources](#official-sources)

## Runtime Readiness

Probe only when version-specific behavior is material. Start with the current
host and a read-only lookup:

```powershell
$currentHost = [pscustomobject]@{
    Edition = $PSVersionTable.PSEdition
    Version = $PSVersionTable.PSVersion.ToString()
    Home = $PSHOME
}

$pwshCandidates = @(
    Get-Command pwsh -CommandType Application -All -ErrorAction SilentlyContinue
)

$pwsh = $null
if ($pwshCandidates.Count -eq 1) {
    $pwsh = $pwshCandidates[0]
}
elseif ($pwshCandidates.Count -gt 1) {
    $pwshCandidates | Select-Object Name, Path, CommandType
    throw 'Multiple pwsh candidates require an explicit selection rule.'
}
```

If exactly one `pwsh` resolves, verify that exact executable rather than
trusting `PATH`. Keep resolution, launch, output-contract, and support status
separate:

```powershell
$probeArgs = @(
    '-NoLogo'
    '-NoProfile'
    '-NonInteractive'
    '-Command'
    '$PSVersionTable.PSVersion.ToString()'
)

$pwshLaunchSucceeded = $false
$pwshProbeExit = $null
$pwshProbeText = ''
$pwshProbeError = $null

if ($null -ne $pwsh) {
    try {
        $pwshProbeText = (& $pwsh.Path @probeArgs | Out-String)
        $pwshProbeExit = [int]$LASTEXITCODE
        $pwshLaunchSucceeded = $true
    }
    catch {
        $pwshProbeError = $_
    }
}

$pwshProbeLines = @(
    (($pwshProbeText -replace "`r`n?", "`n") -split "`n") |
        ForEach-Object { $_.Trim() } |
        Where-Object { $_.Length -gt 0 }
)
$pwshOutputValid = (
    $pwshProbeLines.Count -eq 1 -and
    $pwshProbeLines[0] -match '^\d+\.\d+(?:\.\d+)?(?:-[0-9A-Za-z.-]+)?$'
)
$pwshUsable = (
    $null -ne $pwsh -and
    $pwshLaunchSucceeded -and
    $pwshProbeExit -eq 0 -and
    $pwshOutputValid
)
```

Capture `$LASTEXITCODE` immediately after the exact native probe and coerce it
to an integer before another native command runs. A resolved path is not a
usable runtime when launch fails, the exit is nonzero, stdout is empty, or the
normalized stdout contains anything other than one well-formed version value.
Keep support status `UNKNOWN` until current official lifecycle evidence is
checked; a valid version string alone does not establish support.

Classify the result:

| Observation | Response |
|---|---|
| Exact probe launches, exits zero, emits one valid version, and current lifecycle evidence says supported | Prefer it for version-sensitive modern workflows when the task is compatible |
| `pwsh` resolves but cannot launch, exits nonzero, emits empty output, or emits malformed output | Treat it as not yet usable; preserve which launch, exit, or output contract failed before proposing repair or another install |
| Only Windows PowerShell 5.1 is usable | Continue on a 5.1-compatible path; conditionally recommend 7 when it materially reduces task risk |
| The installed PowerShell 7 may be out of support | Check the current official lifecycle; do not hard-code a support date |
| A required module or host supports only 5.1 | Keep that workload on 5.1 or stop for a compatibility decision |
| No usable PowerShell host exists | Stop PowerShell execution and offer official installation guidance |

PowerShell 7 uses `pwsh` and installs side-by-side with Windows PowerShell 5.1;
it does not replace `powershell.exe`. Some legacy modules still require 5.1.
Prefer a supported stable or LTS release, but verify the current lifecycle at
the time of use. If current lifecycle evidence is unavailable, report support
status as unknown instead of inferring it from the major/minor version.

When 7 is absent, recommend it only with a task-specific reason:

> Only Windows PowerShell 5.1 is currently usable. This task depends on
> PowerShell-version-sensitive text, native-command, or WSL behavior.
> PowerShell 7 can reduce those compatibility risks and installs side-by-side
> with 5.1. Would you like the official installation options?

Do not imply that PowerShell 7 makes nested quoting, incompatible modules, or
cross-shell transport automatically safe.

## Installation Is A Separate Authorized Action

Detection and recommendation are read-only. Before an installation:

1. Obtain explicit user authorization for the network download and host
   mutation.
2. Check Windows version, architecture, enterprise policy, administrator
   requirements, existing installation method, and whether `winget` is usable.
3. Re-open the current Microsoft installation guide because package formats,
   versions, and supported methods change.
4. On a supported Windows client, WinGet is the usual first option:

   ```powershell
   winget install --id Microsoft.PowerShell --source winget
   ```

5. On Windows Server or an enterprise-managed host, use the approved MSI,
   MSIX, ZIP, or managed deployment route from the current official guidance.
   Do not bootstrap WinGet or bypass organizational controls automatically.
6. Explain material installer choices such as scope, `PATH`, updates, remoting,
   profiles, and package sandbox limitations before accepting non-default
   behavior.
7. After installation, start a fresh process if necessary, resolve `pwsh`
   again, verify its edition/version/exit status, and rerun the original
   minimal reproduction.

Never silently install or update PowerShell, elevate, select a preview release,
change the default shell or terminal profile, remove Windows PowerShell 5.1, or
modify locale, execution policy, registry, or global code page.

## Parse Complex PowerShell Before Execution

Prefer a `.ps1` file for loops, `try`/`catch`, regex, hashtables, object
construction, or complex pipelines. It removes an inline transport boundary
and gives the target PowerShell parser the complete source. The parser API uses
the current process's grammar, so run the parse-only block inside the same exact
PowerShell executable and version that will execute the target script. A
PowerShell 7 parse does not qualify a later Windows PowerShell 5.1 run. Parse
the exact file without executing it before the first run:

```powershell
$tokens = $null
$parseErrors = $null
[void][System.Management.Automation.Language.Parser]::ParseFile(
    $scriptPath,
    [ref]$tokens,
    [ref]$parseErrors
)
if ($parseErrors.Count -ne 0) {
    $parseErrors | Select-Object Message, Extent
    throw 'PowerShell parse-only readiness failed.'
}
```

If the current process is not the target runtime, put this parser block in a
small `.ps1` driver and invoke it directly with the already selected target
executable. Pass the target script path or inline payload as data; do not put
the payload inside another `-Command` string. Capture that target parser
process's exit code and stop before execution when it reports errors.

For an unavoidable inline payload, call `Parser.ParseInput` on the exact string
inside that same target runtime and reject any parse error. This is a syntax
check, not proof of parameter compatibility, runtime success, or side-effect
correctness. Do not add a second shell, encoded command, or more complex
quoting to make an unparsed payload launch.

Keep these high-value traps explicit:

- delimit a variable before a literal colon, for example `${name}:` rather
  than `$name:`;
- when a regex must contain literal `$env:` or `$script:`, use a
  non-interpolating string or escape the dollar sign instead of a double-
  quoted interpolating string;
- reserve automatic `$Matches` for the most recent `-match` result and use a
  distinct application collection name; and
- do not attach statement-form `foreach (...) { ... }` directly to a pipeline.
  Collect its output first, or use a pipeline-native form such as
  `ForEach-Object` when that is the intended contract.

## Cmdlet Or Native Executable

Establish which contract applies:

- A cmdlet writes PowerShell objects and PowerShell streams. Judge failures
  through its error contract, exceptions, and common parameters.
- A native executable receives process arguments and byte/text streams. Judge
  it through its documented stdout, stderr, and exit-code contract.
- `$?` is useful context, but capture `$LASTEXITCODE` immediately when the
  native program's numeric status matters.
- A native tool may write diagnostics or progress to stderr and still exit
  successfully. Text on stderr is not automatically failure.

For routine cmdlets, prefer named parameters and use a literal-path parameter
only when the command actually supports it:

```powershell
Get-Content -LiteralPath $path -Encoding UTF8
```

## Cmdlet Parameters And Failure Contracts

`-LiteralPath` is not a universal filesystem parameter. Inspect the target
command when its contract is uncertain:

```powershell
$command = Get-Command New-Item -CommandType Cmdlet
$command.Parameters.Keys
Get-Help New-Item -Full
```

`New-Item` supports `-Path` and does not support `-LiteralPath`. Use its actual
parameter contract and validate the intended result; do not generalize this
one parameter shape to every cmdlet:

```powershell
try {
    New-Item -ItemType Directory -Path $directoryPath `
        -ErrorAction Stop | Out-Null
    if (-not (Test-Path -LiteralPath $directoryPath -PathType Container)) {
        throw 'The expected directory was not created.'
    }
}
catch {
    throw "Directory creation failed: $($_.Exception.Message)"
}
```

Many cmdlet errors are non-terminating by default. A script can emit such an
error, continue to a later successful statement, and leave an outer process
with exit `0` while the required artifact is absent. For a critical step, use
the narrowest supported terminating behavior, normally `-ErrorAction Stop`
inside a focused `try`/`catch`, and verify the expected artifact or state.
Do not infer cmdlet success from the final `$?`, output truthiness, or the outer
process exit alone. `$LASTEXITCODE` records native process status; it is not a
cmdlet failure signal.

## Command Discovery And Result Shape

PowerShell can expose zero, one, or many pipeline results with different
runtime shapes. Normalize an uncertain result with `@(...)` before reading
`.Count` or indexing it:

```powershell
$candidates = @(
    Get-Command $commandName -CommandType Application -All `
        -ErrorAction SilentlyContinue
)

switch ($candidates.Count) {
    0 {
        throw "No application candidate was found for $commandName."
    }
    1 {
        $exe = $candidates[0]
    }
    default {
        $candidates | Select-Object Name, Path, CommandType
        throw "Multiple application candidates require an explicit selection rule."
    }
}
```

Do not index a possibly scalar string or pipeline result: `[0]` can select the
first character instead of the first path. Do not coerce several
`ApplicationInfo` objects or their paths into one command string. Select one
object first, then invoke its exact path.

`Get-Command -All` returns same-named commands in execution-precedence order.
Choosing the first item is valid only when the explicit contract is “the
command a bare name would invoke”; record that rule and the selected path.
When provenance, architecture, environment ownership, or destructive impact
matters, inspect every candidate and fail closed until the intended executable
identity is established.

## Native Errors And Preference Variables

Windows PowerShell 5.1 can surface text written by a native executable to
stderr as a `NativeCommandError` record. In some hosts or collection shapes,
`$ErrorActionPreference = 'Stop'` can then terminate the surrounding
PowerShell operation before the caller has classified the native result. The
error record is evidence about the PowerShell stream boundary; it does not
replace the executable's documented stdout, stderr, and numeric exit-code
contract.

PowerShell 7 behavior also depends on version and preferences. When available,
inspect `$PSNativeCommandUseErrorActionPreference` before assuming that a
nonzero native exit is or is not converted into a PowerShell error. Do not
change that preference globally as a diagnostic shortcut.

Use this order:

1. record the PowerShell edition, version, relevant preference values, and
   invocation shape;
2. reproduce with the smallest direct native invocation;
3. preserve stdout, stderr, and `$LASTEXITCODE` as separate evidence;
4. decide success from the native tool's documented contract; and
5. change preference handling only in the narrow owning scope when the task
   requires it.

Do not catch and discard a terminating error merely to force a green result.
If PowerShell prevents complete stream capture, use the native tool's
output-file options or an explicitly configured process API and keep the
original error as evidence.

## Preserve Native Arguments

Prefer one array item per argument:

```powershell
$exe = 'tool.exe'
$nativeArgs = @(
    '--input'
    $inputPath
    '--format'
    'json'
    '--empty'
    ''
)

& $exe @nativeArgs
$exitCode = $LASTEXITCODE
```

Omitted arguments, `''`, and `$null` are distinct. Do not pre-quote values that
are already separate array elements, concatenate untrusted strings into a
command, or repair quoting by adding `cmd.exe /c`, another `powershell
-Command`, or `Invoke-Expression`.

PowerShell 7.3 changed native argument passing. On Windows,
`$PSNativeCommandArgumentPassing` normally uses `Windows` mode, which falls
back to legacy behavior for `cmd.exe`, Windows Script Host, and common batch or
script extensions. When quotes or empty arguments arrive differently:

```powershell
$PSNativeCommandArgumentPassing
Trace-Command -Name ParameterBinding -Expression { & $exe @nativeArgs } -PSHost
```

Treat a 5.1-to-7 behavior change as a compatibility hypothesis, not immediate
proof that either the application or PowerShell is defective. Use the
Windows-only stop-parsing token `--%` only for a narrow native-command case
that cannot be expressed safely with normal argument arrays; it is not a
cross-platform or multi-line solution.

## Complete User-Runnable Examples

Do not let a diagnostic rule disappear when turning it into a command the user
can run. A native example that discovers its executable must show or reuse:

1. an application-only candidate collection normalized with `@(...)`;
2. explicit handling for zero, one, and unresolved multiple candidates;
3. the selected `ApplicationInfo` object or exact path;
4. one array element per native argument;
5. the actual stdout/stderr disposition; and
6. immediate exit-code capture; and
7. observed runtime and capability evidence for every version-specific API.

The entry-point example uses an exact-one rule and inherited console streams.
That is complete only when separate stream contents are not needed. A request
to report or compare both streams makes independent capture material. If the
tool contract permits bare-name execution precedence, selecting the first
`Get-Command -All` result may replace exact-one selection, but state that rule
and report the selected path. If stream distinction is material, use the
tool's independent output files or the redirected process pattern below.

Do not write “capture stdout and stderr separately” next to an invocation that
inherits, merges, or discards them. State what the command actually does and
what remains unobserved.

When the current host is accessible, execute the read-only runtime and
capability probes and report the observed values before relying on
version-specific syntax. A probe embedded in a future user command is a guard,
not evidence that the current host already passed it. When execution is
unavailable, state that limitation and keep compatibility unknown.

## Streams, Pipelines, And Redirection

- Capture stdout and stderr separately when their distinction matters.
- Save `$LASTEXITCODE` before another native command can overwrite it.
- A PowerShell pipeline normally carries objects; a native pipeline carries
  process streams. Do not assume POSIX stdin or byte behavior across a
  PowerShell cmdlet boundary.
- `pwsh -File` is usually clearer for multi-line automation. A `pwsh -Command`
  wrapper has its own exit semantics; preserve or explicitly `exit
  $LASTEXITCODE` when the wrapped native status must cross that boundary.
- PowerShell 7.4 and newer preserve native stdout bytes when redirecting them
  to a file or piping them to another native command. This guarantee does not
  apply after merging stderr into stdout with `2>&1`.
- For binary output, prefer the native tool's output-file option or a verified
  byte-safe route. Do not pass binary data through text cmdlets.
- If output is missing, truncated, reordered, or reformatted, remove
  formatting and filtering stages, use a minimal command, and capture streams
  independently before changing application code.

## Process APIs

Use the simplest structure-preserving mechanism:

1. a cmdlet with explicit parameters;
2. `& $exe @nativeArgs` for a foreground native process;
3. a `.ps1` or target-shell script for complex multi-line logic;
4. `ProcessStartInfo.ArgumentList` when separate process control, environment,
   or redirected streams are genuinely required;
5. `Start-Process` for an approved need such as elevation, a new window,
   detached execution, credentials, or shell association.

`Start-Process -ArgumentList` joins array elements into one command-line string.
It is not a structured argument API for complex quotes, empty strings, JSON, or
regular expressions. `ProcessStartInfo.ArgumentList` is available on the modern
.NET runtime used by PowerShell 7 and accepts arguments one at a time without
pre-escaping:

```powershell
$currentHost = [pscustomobject]@{
    Edition = $PSVersionTable.PSEdition
    Version = $PSVersionTable.PSVersion.ToString()
}
$argumentListAvailable = $null -ne (
    [System.Diagnostics.ProcessStartInfo].GetProperty('ArgumentList')
)
[pscustomobject]@{
    Runtime = $currentHost
    ArgumentListAvailable = $argumentListAvailable
}
if (-not $argumentListAvailable) {
    throw "ProcessStartInfo.ArgumentList is unavailable in $($currentHost.Edition) $($currentHost.Version)."
}

# $exe is the ApplicationInfo selected by the discovery rule above.
$startInfo = [System.Diagnostics.ProcessStartInfo]::new()
$startInfo.FileName = $exe.Path
$startInfo.UseShellExecute = $false

foreach ($argument in $nativeArgs) {
    [void]$startInfo.ArgumentList.Add($argument)
}
```

When separate text streams are required and the tool's encoding contract is
known, redirect and drain both streams independently:

```powershell
$startInfo.RedirectStandardOutput = $true
$startInfo.RedirectStandardError = $true

$process = [System.Diagnostics.Process]::new()
$process.StartInfo = $startInfo
if (-not $process.Start()) {
    throw 'The native process did not start.'
}

$stdoutTask = $process.StandardOutput.ReadToEndAsync()
$stderrTask = $process.StandardError.ReadToEndAsync()
$process.WaitForExit()

$stdout = $stdoutTask.GetAwaiter().GetResult()
$stderr = $stderrTask.GetAwaiter().GetResult()
$exitCode = $process.ExitCode
$process.Dispose()
```

Set `StandardOutputEncoding` and `StandardErrorEncoding` only when the native
tool's documented text contract justifies those values. Set environment,
working directory, wait behavior, and timeout deliberately. Validate
untrusted input even when the API preserves argument boundaries.

Windows PowerShell 5.1 runs on .NET Framework and does not provide
`ProcessStartInfo.ArgumentList`. Prefer direct `& $exe @nativeArgs` or a script
file there. If a separate 5.1 process is unavoidable, treat the string-based
`Arguments` property as a new quoting boundary and test it against the exact
target executable rather than presenting it as structured transport. Do not
present the PowerShell 7 capture example as a 5.1-compatible command.

## Paths, Permissions, And Destructive State

- Use `-LiteralPath` only when the target command supports it and literal path
  semantics are required. Otherwise inspect the command's parameter contract;
  do not substitute an unsupported parameter mechanically.
- Give each relative path exactly one declared base: the observed working
  directory, an explicit tool root, or a documented project root. Record the
  raw path, `Get-Location`, the resolved literal path, and the tool's own
  read-only root when available before changing application code.
- Resolve a relative path once. If a value is already rooted or has already
  been resolved, do not join it to the base again.
- Resolve ambiguous command names before destructive work. For example,
  `rd`/`rmdir` may name a PowerShell alias or a `cmd.exe` built-in depending on
  the parser. Use `Get-Command <name> -All` for PowerShell resolution and name
  the intended executable or cmdlet explicitly.
- Before recursive delete, move, or overwrite, reject empty, unresolved, root,
  home, or workspace-wide targets; resolve each target and prove it stays under
  the intended root.
- Keep enumeration and mutation in one PowerShell process. Preview a new
  destructive shape with a read-only listing or `-WhatIf` when supported.
- Do not enumerate paths in PowerShell and concatenate them into a
  `cmd.exe /c rd` or `rmdir` string. If a native or `cmd.exe` operation is
  genuinely required, treat it as a new parser boundary and revalidate every
  literal target in the owning shell.
- Treat success only with elevation as a permission boundary, not evidence for
  an application patch.
- Separate a sandbox process-creation denial, a program exit, and a write
  denial. Prove whether the command started and identify the literal write
  target and owning policy before requesting additional authority.
- If the task permits derived caches or bytecode elsewhere, prefer a
  task-specific temporary root inside an authorized boundary. Do not disable
  the sandbox, change a global cache, or patch application code merely to hide
  an environment failure. Retry outside the current boundary only after
  explicit authorization, and retry the same narrow command.
- Installing tools, changing profiles or policy, starting persistent
  processes, and modifying services, firewall, registry, networking, or WSL
  state require explicit authorization, verification, and a material rollback
  plan.

## Junction And Reparse-Point Removal

A failure from `Remove-Item` does not by itself justify a .NET fallback.
Before removing a Windows directory link:

1. resolve the proposed link path to an absolute literal path and reject roots,
   homes, workspace-wide targets, wildcards, and unresolved input;
2. inspect the exact item and prove that its reparse-point attribute and link
   type identify the intended Junction rather than an ordinary directory,
   symbolic link, mount point, or unknown reparse type;
3. record the link path and target as separate roles, prove which one is the
   disposable link and which one is retained source, and define a retained
   sentinel to verify afterward;
4. keep inspection and removal in the same PowerShell process; and
5. stop if identity, containment, permission, or recovery remains uncertain.

If `Remove-Item -LiteralPath` fails after those checks and removing only the
confirmed Junction is authorized, a bounded fallback is:

```powershell
[System.IO.Directory]::Delete($junctionPath, $false)
```

Pass `false`; never broaden this fallback to recursive deletion or a wildcard.
Afterward, prove that the link is absent and that the target plus its sentinel
still exist. .NET documents that directory reparse points are removed without
recursing through their targets, but this does not make every reparse-point
type or every observed access error interchangeable.

## Official Sources

- [Install PowerShell 7 on Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell support lifecycle](https://learn.microsoft.com/en-us/powershell/scripting/install/powershell-support-lifecycle)
- [Migrate from Windows PowerShell 5.1 to PowerShell 7](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7)
- [about_Parsing](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_parsing)
- [about_Arrays](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_arrays)
- [about_Automatic_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables)
- [about_Preference_Variables](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_preference_variables)
- [about_Redirection](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection)
- [Get-Command](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/get-command)
- [about_FileSystem_Provider](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_filesystem_provider)
- [Start-Process](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/start-process)
- [ProcessStartInfo.ArgumentList](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.processstartinfo.argumentlist)
- [Directory.Delete](https://learn.microsoft.com/en-us/dotnet/api/system.io.directory.delete)
