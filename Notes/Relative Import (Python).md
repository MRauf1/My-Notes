---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Relative Import (Python)[^1]
> A [[From Import Statement (Python)|from]] import whose source starts with one or more dots, identifying an item relative to the importing file's own [[Package (Python)|package]] rather than searching the [[Module Search Path (Python)|module search path]]; a single `.` means the immediately enclosing package folder, and each additional leading dot means one level further up.

# Properties
- Contrasted with an ordinary ("absolute") import, which is resolved against the module search path and never automatically checks the importing file's own package[^2].
- Guarantees that a package's internal imports load its own modules rather than an unrelated, same-named module found elsewhere on the search path — at the cost of only working when the file is actually used as part of a package[^1].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=925&annotation=RHYE78F5)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=926&annotation=J4CYJWW3)
