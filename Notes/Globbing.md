---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Globbing[^1]
> Globbing is the process by which the [[Shell (Unix)|shell]] matches simple wildcard patterns against file and directory names.

# Properties
- Arguments containing globs are substituted with matching filenames before the command runs; this substitution is called expansion.
- If no files match a glob, the shell performs no expansion, and the command runs with the literal glob characters (such as *).
- The shell performs expansions before running commands, and only then; a glob character that reaches a command unexpanded is left for that command to interpret.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=42&annotation=7IUTQKMK)
