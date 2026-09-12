---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Package (Python)[^1]
> A directory of [[Module (Python)|module]] files, and possibly nested subdirectories, that extends the import model to nested files: importing `dir1.dir2.mod` implies a directory `dir1` (itself located on the [[Module Search Path (Python)|module search path]]) containing a subdirectory `dir2`, which in turn contains a module `mod`.

# Properties
- An `__init__.py` file placed in a package directory runs automatically the first time that directory is imported, giving a natural hook for package-wide setup code; its own top-level assignments become attributes of the package's module object[^2].
- A `__main__.py` file placed in a package directory instead runs when that directory itself is launched as a program[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=910&annotation=3NLW8M6I)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=915&annotation=89HGMSS5)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=917&annotation=RRJY9WWU)
