# Windows And WSL Boundaries

Load this reference only when a task crosses between Windows and WSL through
execution, paths, stdin/stdout, files, permissions, environment, or state.
PowerShell 7 is a better default Windows-side transport for modern text and
native-command behavior, but it does not make complex cross-shell quoting safe.

## Contents

- [Map The Boundary](#map-the-boundary)
- [Prefer Direct Execution](#prefer-direct-execution)
- [Path And Filesystem Semantics](#path-and-filesystem-semantics)
- [Streams, Encoding, And Exit Status](#streams-encoding-and-exit-status)
- [Environment And Permissions](#environment-and-permissions)
- [State-Changing WSL Operations](#state-changing-wsl-operations)
- [Diagnostic Sequence](#diagnostic-sequence)
- [Official Sources](#official-sources)

## Map The Boundary

Identify each owner:

1. the calling tool or Harness;
2. the active Windows shell and PowerShell version;
3. `wsl.exe`;
4. the selected distribution and Linux user;
5. any Linux shell such as Bash;
6. the target executable, path namespace, filesystem, and output contract.

Do not debug all layers at once. First verify the active PowerShell host, then
use a read-only WSL probe, then add the target command.

If the PowerShell minor version or native argument mode is not observed, keep
it unknown. On PowerShell 7.3 and newer, record
`$PSNativeCommandArgumentPassing` when argument transport is part of the
hypothesis.

## Prefer Direct Execution

Use an explicit distribution and executable with separate arguments:

```powershell
$wslCandidates = @(
    Get-Command wsl.exe -CommandType Application -All -ErrorAction SilentlyContinue
)

if ($wslCandidates.Count -eq 0) {
    throw 'No wsl.exe application candidate was found.'
}
if ($wslCandidates.Count -gt 1) {
    $wslCandidates | Select-Object Name, Path, CommandType
    throw 'Multiple wsl.exe candidates require an explicit identity rule.'
}

$wsl = $wslCandidates[0]
$distribution = 'Example-Distro'
$wslArgs = @(
    '--distribution'
    $distribution
    '--exec'
    '/bin/echo'
    'wsl-ok'
)

& $wsl.Path @wslArgs
$wslExitCode = [int]$LASTEXITCODE
if ($wslExitCode -ne 0) {
    throw "The exact wsl.exe probe failed with exit $wslExitCode."
}
```

The selected value remains the one `ApplicationInfo` object, and invocation
uses its exact `.Path`. Do not index a possibly scalar path string, accept a
non-application alias, silently choose the first of several candidates, or run
another native command before capturing the typed exit status.

Then replace only the Linux executable and arguments needed by the task. Avoid
long inline `bash -lc` payloads, Bash heredocs, command substitutions, or nested
PowerShell strings. Put complex Linux logic in a `.sh` script with LF line
endings and invoke that script with simple arguments.

If a shell is genuinely required, count both the PowerShell and Bash parsers
and test literal quotes, dollar signs, spaces, wildcards, and newlines at that
boundary.

## Path And Filesystem Semantics

- Windows paths and Linux paths are different namespaces. Pass Linux paths such
  as `/mnt/c/...` to Linux tools; do not assume a raw Windows path is
  understood.
- Use `wslpath` or an explicit, verified mapping when conversion is needed.
  Do not convert paths with broad string replacement.
- A Linux command launched from PowerShell through `wsl.exe` normally starts
  from the corresponding current Windows working directory, runs as the
  distribution's default Linux user unless specified otherwise, and inherits
  the calling process's Windows administrative rights.
- Windows filesystems are normally case-insensitive while Linux filesystems
  are case-sensitive. Do not collapse paths that differ only by case without
  checking the actual filesystem.
- Cross-filesystem metadata, executable bits, symlinks, permissions,
  performance, and newline behavior can differ. Keep active Linux project files
  in the Linux filesystem when the workload is primarily Linux, unless the
  target project's policy says otherwise.
- Use UNC or mounted paths only with an explicit ownership and performance
  reason. Do not hide a path mismatch by adding another shell.

## Streams, Encoding, And Exit Status

- Capture `$LASTEXITCODE` immediately after `wsl.exe`; a successful PowerShell
  invocation does not prove the Linux program succeeded.
- Treat Windows PowerShell, `wsl.exe`, the Linux process, and any Bash wrapper
  as separate encoding and exit-code boundaries.
- Test stdout and stderr separately when missing, reordered, or garbled output
  matters.
- Avoid stdin pipelines until a direct executable probe succeeds. PowerShell
  object pipelines, native byte streams, and Linux stdin are not interchangeable
  without a defined conversion.
- Use explicit UTF-8 and LF semantics for scripts or structured text shared
  with Linux. Inspect bytes when BOM or newline identity matters.
- Do not pass binary data through PowerShell text cmdlets. Prefer a native
  output-file option or a verified byte-safe route.

## Environment And Permissions

- Verify the distribution, Linux user, working directory, executable, and
  relevant environment rather than assuming the default.
- Prove identity and location with direct read-only commands such as
  `/usr/bin/whoami` and `/bin/pwd` after selecting the distribution. Use
  `--user` only when the task requires a specific known Linux account.
- Windows elevation does not equal Linux `root`; Linux `sudo` is a separate
  authority boundary.
- A sandbox may block `wsl.exe` process creation or access before Linux runs.
  Preserve the exact failure and prove where execution stopped before changing
  project code or WSL configuration.
- Do not print complete environments. Inspect only named variables required by
  the task and redact secrets.
- Stop when the requested distribution is absent, stopped for an unexplained
  reason, owned by another user, or governed by an organization policy that
  has not been established.

## State-Changing WSL Operations

Inspect with narrow read-only commands such as `wsl.exe --status`,
`wsl.exe --version`, and `wsl.exe --list --verbose` when relevant.

Treat shutdown, termination, mount/unmount, distribution import/export,
default-version changes, package installation, and service changes as external
state mutations requiring explicit authorization and post-checks.
`wsl.exe --unregister` permanently removes a distribution and its data; never
use it as a troubleshooting shortcut.

Before deleting or moving files across Windows and WSL:

1. resolve the Windows and Linux views of the target;
2. prove both refer to the intended location;
3. reject roots, home directories, unresolved variables, and broad globs;
4. keep enumeration and mutation in one owning shell;
5. preview the exact target set and define recovery.

## Diagnostic Sequence

1. Verify the active PowerShell edition/version and resolved `wsl.exe`.
2. Record the native argument mode when supported and material; otherwise keep
   it unknown.
3. Inspect WSL status and distribution identity only as needed.
4. Run a direct read-only executable probe.
5. Confirm the actual Linux user, working directory, rights, and path
   namespace with separate probes rather than inferred defaults.
6. Test stdout, stderr, and exit status separately with a fixed non-sensitive
   payload when stream behavior is material.
7. Add the real command with one array element per argument.
8. Add stdin, pipelines, redirection, or a shell only after the direct form
   works.
9. Capture exit status and streams at every added boundary.
10. Classify the failure before changing the application, WSL state, or system
    configuration.

## Official Sources

- [Basic commands for WSL](https://learn.microsoft.com/en-us/windows/wsl/basic-commands)
- [Working across Windows and Linux file systems](https://learn.microsoft.com/en-us/windows/wsl/filesystems)
- [WSL interoperability](https://learn.microsoft.com/en-us/windows/wsl/filesystems#run-linux-tools-from-a-windows-command-line)
- [about_Parsing](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_parsing)
