---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Module Search Path (Python)[^1]
> The ordered list of directories Python searches, left to right, to resolve an [[Import Statement (Python)|import]]; recorded at runtime as the `sys.path` list.

# Properties
- Home directory (automatic): the directory of the running program's top-level script, or the current working directory in a REPL; always searched first[^2].
- `PYTHONPATH` directories (configurable): user-set directories listed in the `PYTHONPATH` environment variable, searched next; only needed for imports that cross directory boundaries[^3].
- Standard-library directories (automatic): where Python's own standard-library modules are installed[^4].
- The `site-packages` directory (automatic): where third-party packages are installed, typically by a tool like `pip`[^5].
- `.pth` path files (configurable): text files of extra directory names dropped into `site-packages`, serving as an alternative to setting `PYTHONPATH`[^6].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=872&annotation=DQS2JE6C)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=873&annotation=WNNYJJQZ)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=873&annotation=ZJHSM7N9)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=874&annotation=JHUZW3KR)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=874&annotation=P69XZNWW)
[^6]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=874&annotation=CZTDBZKT)
