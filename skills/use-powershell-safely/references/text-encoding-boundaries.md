# Text And Encoding Boundaries

Load this reference only when the task involves text bytes, UTF-8, BOM,
newlines, hashes, JSON/schema files, native text streams, non-ASCII content, or
a legacy code page. UTF-8 correctness is general; Chinese and other CJK text
commonly expose legacy assumptions but do not require a separate correctness
model.

## Contents

- [Diagnose Before Rewriting](#diagnose-before-rewriting)
- [PowerShell Version Differences](#powershell-version-differences)
- [Files, JSON, Schema, And Hashes](#files-json-schema-and-hashes)
- [Cross-Shell Text Contracts](#cross-shell-text-contracts)
- [Native Text Streams](#native-text-streams)
- [Legacy Locale And CJK Exposure](#legacy-locale-and-cjk-exposure)
- [Stop Conditions](#stop-conditions)
- [Official Sources](#official-sources)

## Diagnose Before Rewriting

Use this order:

1. Preserve the original bytes.
2. Identify the producer, consumer, declared format, and required byte or text
   contract.
3. Inspect BOM and representative bytes when byte identity matters.
4. Decode with the expected encoding and parse the structured format.
5. Compare file encoding, console rendering, native stdin/stdout encoding, and
   locale as separate boundaries.
6. Reproduce with an explicit reader before changing the application or file.
7. Rewrite only when the stored bytes or producer contract is actually wrong.

Garbled terminal output is evidence of an unresolved boundary, not proof that
the file is corrupt. Conversely, readable output does not prove the bytes,
newline sequence, or BOM are correct.

## PowerShell Version Differences

| Behavior | Windows PowerShell 5.1 | PowerShell 7 |
|---|---|---|
| Default text output | Cmdlet defaults vary and may use a legacy code page or UTF-16 | Defaults to UTF-8 without BOM |
| `-Encoding UTF8` writes | UTF-8 with BOM | UTF-8 without BOM |
| UTF-8-without-BOM scripts containing non-ASCII | Can be interpreted through the active ANSI code page | Treated as UTF-8 |
| `-Encoding Ansi` | Not available | Available beginning in 7.4 and maps to the current culture's ANSI code page |

Prefer a supported PowerShell 7 release for modern text workflows, but still
specify and verify encoding when another program, an exact file format, or a
byte hash defines the contract.

Do not “fix” a 5.1 ambiguity by changing a user profile or session-global
encoding defaults. Use explicit call-site behavior or a byte-oriented writer.

## Files, JSON, Schema, And Hashes

- For a known UTF-8 file, use an explicit UTF-8 reader:

  ```powershell
  $text = Get-Content -LiteralPath $path -Raw -Encoding UTF8
  ```

- When exact bytes matter, use `[System.IO.File]::ReadAllBytes()` and inspect
  the first bytes before parsing or hashing.
- For BOM-free UTF-8 output, prefer a repository-aware edit tool or
  `[System.Text.UTF8Encoding]::new($false)` with .NET file APIs.
- Do not use PowerShell text cmdlets to write images, archives, executables, or
  other binary data.
- Validate JSON or a schema semantically after decoding; do not infer validity
  from display output.
- Do not rewrite the input before reproducing a parser failure. A rewrite can
  remove the evidence by changing BOM, newline, normalization, or encoding.
- Distinguish a semantic text hash from a raw byte hash. State whether newline
  normalization, BOM removal, or Unicode normalization is part of the hash
  contract.
- Preserve the repository's newline policy. Inspect bytes when CRLF versus LF
  affects a consumer or hash rather than relying on the current host default.
- When text must be truncated by a byte budget, decode it first or select a
  validated UTF-8 code-point boundary. An arbitrary byte slice can end inside a
  multi-byte sequence and create invalid UTF-8.
- Avoid `Out-File`, `Set-Content`, `Add-Content`, `>` or `>>` when their
  version-specific encoding or append behavior cannot be proven to preserve
  the target contract.

PowerShell's `$OutputEncoding` affects communication with external programs;
it does not set the encoding used by every file-writing cmdlet or redirection
path. Diagnose those boundaries separately.

## Cross-Shell Text Contracts

Treat a PowerShell, Python, Bash, WSL, or native bridge as a text protocol.
Identify the producer, every bridge that decodes or re-emits text, and the
consumer. Define encoding, BOM policy, newline sequence, final-newline
behavior, and empty-line preservation at the consumer boundary.

When a Unix or Bash consumer requires UTF-8 without BOM and LF, do not rely on
the Windows platform newline or on a text cmdlet's version-dependent default.
For a known line-oriented payload:

```powershell
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$payload = ($lines -join "`n") + "`n"
[System.IO.File]::WriteAllBytes($path, $utf8NoBom.GetBytes($payload))
```

Use that shape only when the consumer contract requires one final LF. Do not
normalize arbitrary text, signed content, or repository files without first
establishing their contract.

Inspect the bytes after the last bridge, not only the string displayed by the
producer. When LF-only is required, assert that line terminators are `0A`,
that no `0D` remains before them, and that the consumer does not receive a
trailing carriage return as data. Apply the same check to temporary test
bridges: a test adapter that rewrites LF to CRLF can invalidate an otherwise
correct production path.

## Native Text Streams

For a native program, determine:

- which encoding it expects on stdin;
- which encoding it emits on stdout and stderr;
- whether it follows a console code page, locale, explicit command option,
  environment variable, or fixed protocol;
- whether PowerShell converts strings before sending or after receiving them.

Prefer the native tool's explicit encoding, JSON, or output-file option. If
stdout and stderr use different contracts, capture them separately. Do not
merge them before diagnosing mojibake or byte preservation.

PowerShell 7.4 can preserve native stdout bytes through native redirection and
native-to-native pipelines, but merging stderr into stdout turns the combined
streams into string data. See the native/process reference before relying on
this version-specific behavior.

## Legacy Locale And CJK Exposure

Load this subsection only after evidence points to a legacy code page or
locale-sensitive native program.

1. Record the PowerShell edition/version, active culture, relevant console code
   page, and the native program's documented encoding behavior.
2. Prove whether corruption happens in storage, display, stdin, stdout,
   argument transport, or an intermediate file.
3. Test a small payload containing ASCII plus representative non-ASCII
   characters. Do not use sensitive production text.
4. Prefer a tool-specific UTF-8 flag, explicit decoder/encoder, or controlled
   per-process environment over a system-wide change.
5. Keep a 5.1 compatibility route only when required by the real consumer.

`chcp` reports or changes a console code page; it does not prove the encoding
of a file, a GUI application, or every native stream. A Chinese Windows locale
often exposes CP936/GBK assumptions, but English environments can have the same
UTF-8/BOM/newline defects and should follow the same general diagnostic order.

A locale-specific failure observed on one machine supports a bounded
hypothesis about the producer, consumer, or code-page boundary. It does not
justify publishing that machine's locale, environment-variable values, or
tool paths as a general prerequisite.

Do not default to changing system locale, registry, profile, global code page,
the “Beta: Use Unicode UTF-8” setting, or application-wide defaults. Those
changes are broad, persistent, compatibility-sensitive, and require a separate
authorized host decision.

If explicit UTF-8 decoding, byte inspection, and the consumer contract all
agree, stop treating encoding as the leading hypothesis even when the
environment is non-English.

## Stop Conditions

Stop and ask when:

- the expected encoding or byte-hash contract is unknown;
- rewriting would destroy forensic evidence or a signed/hashed artifact;
- the only proposed remedy is a profile, locale, registry, or system-wide code
  page change;
- a legacy consumer cannot accept UTF-8 and the required compatibility policy
  is user-owned;
- a binary stream would pass through a text-only tool;
- the operation would mutate many files without a bounded preview and rollback.

## Official Sources

- [about_Character_Encoding](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding)
- [about_Redirection](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection)
- [Introduction to character encoding in .NET](https://learn.microsoft.com/en-us/dotnet/standard/base-types/character-encoding-introduction)
- [UTF8Encoding class](https://learn.microsoft.com/en-us/dotnet/api/system.text.utf8encoding)
