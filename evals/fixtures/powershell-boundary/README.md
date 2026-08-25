# PowerShell Boundary Fixture

The JSON verifier succeeds when called directly, but the PowerShell wrapper
reports that the same file is invalid.

Reproduce the wrapper failure from this repository root:

```powershell
pwsh -NoProfile -File .\evals\fixtures\powershell-boundary\tools\run-verifier.ps1
```

The input path intentionally contains a space.

[`command-readiness-cases.json`](command-readiness-cases.json) adds synthetic,
de-identified `New-Item` parameter and cmdlet-error contracts, invalid/valid
pairs for three parse-time traps, and the automatic `$Matches` runtime
collision. It also models resolved-but-unusable `pwsh` probes, application-only
WSL zero/one/many discovery and typed exits, destructive-filesystem selection,
and near-neighbor negatives. The focused checker executes only those bounded
mechanisms; it does not invoke WSL, and the fixture contains no production
command, private host path, session content, or model output.

Together the fixture covers direct-versus-nested argument transport and bounded
command-readiness pairs. It does not establish a supported PowerShell release,
a Windows PowerShell 5.1-only host, live WSL, legacy code pages, authorization
for a system change, or actual Harness selection.
