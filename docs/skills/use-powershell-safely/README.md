# Use PowerShell Safely

[简体中文](README.zh-CN.md)

Diagnoses and safely executes boundary-sensitive Windows shell workflows across PowerShell, native executables, and WSL.

The canonical package is [`skills/use-powershell-safely/`](../../../skills/use-powershell-safely/). See
[Design](DESIGN.md) for the product boundary, [State](STATE.md) for the current
standalone lifecycle, and [Verification](VERIFICATION.md) for evidence and
limits.

The frozen migration and `v0.3.0` snapshot preserves package bytes from source
commit `80910a8b2375a11be897e9660c4b00a06d00dd13`. The current canonical source has
a `0.3.3` repository-native preparation/diagnosis increment recorded in [State](STATE.md);
the accepted source was applied to the managed USER copy. After separately
approved exact-root ACL inheritance repair, ordinary-sandbox byte, receipt and
managed-status checks pass; fresh-task loading and model behavior remain unproven.
Baseline source-blob mappings remain historical identity evidence rather than
claims about those working bytes. Standalone documentation does not relabel
historical candidate, installed-copy, release, or efficacy evidence.
