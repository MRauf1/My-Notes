---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python Bytecode[^1]
> A platform-independent intermediate format that [[CPython|the standard Python implementation]] compiles source code statements into before execution, providing portability across machines.

# Properties
- Compiled once and then executed by the [[Python Virtual Machine|Python Virtual Machine (PVM)]], rather than by the CPU directly; unlike a [[Compiler]] that translates a [[High-Level Programming Language]] all the way down to [[Machine Language]], Python's compile step stops at this intermediate, platform-independent format[^2].
- Cached to disk as a startup-speed optimization: saved in a `__pycache__` subdirectory of the source directory, in files named after the Python version that created them (e.g., `script0.cpython-312.pyc` for version 3.12)[^3].
- A cached file is reused, skipping recompilation, only if the bytecode is present, the source has not changed since it was saved, and the same Python version created it; any source change or version mismatch triggers a fresh compile[^4].
- If Python cannot write the cache to disk, the bytecode is generated in memory instead and discarded when the program exits, so the program still runs correctly[^5].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=22&annotation=Q7F8JXYY)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=40&annotation=ZWFVG4DE)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=40&annotation=SPQA4TM8)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=40&annotation=VVC2S74U)
[^5]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=41&annotation=BV2VMSQB)
