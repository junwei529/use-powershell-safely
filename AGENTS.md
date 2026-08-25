# Agent Instructions

## Required reading

Before changing this repository, read `README.md`, `PROVENANCE.md`,
`docs/skills/use-powershell-safely/DESIGN.md`, `docs/skills/use-powershell-safely/STATE.md`, and
`docs/skills/use-powershell-safely/VERIFICATION.md`.

## Scope and ownership

- Treat `skills/use-powershell-safely/` as the only editable installable Skill source.
- Keep this repository independently useful, installable, invokable, and evaluable.
- Do not add an implicit dependency on another Skill repository.
- Keep one repository writer and preserve unrelated dirty work.
- A commit does not authorize a remote, push, tag, release, installation, or publication.

## Verification

- Run `python -B scripts/check_repository.py --json` for every change.
- Run any focused checker named in `docs/skills/use-powershell-safely/VERIFICATION.md`.
- Keep package behavior and provenance claims evidence-bound.
- Keep private paths, task or host identifiers, prompts, memories, and session data out of tracked files.
