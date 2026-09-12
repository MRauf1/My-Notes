---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Module (Python)[^1]
> A self-contained package of variables — a namespace — that organizes components into a larger system; every name defined at the top level of a module file becomes an attribute of the resulting module object, but a file's names remain invisible elsewhere until explicitly imported, and never clash with names in other files.

# Properties
- Typically corresponds to a Python source file, though a module may also correspond to a compiled extension coded in another language, or to an entire directory in a [[Package (Python)|package]] import[^2].
- Provides three main benefits: code reuse, since a module's code is saved to a file and can be rerun or reused by any number of clients; minimized redundancy, since shared code can be written once and imported by many files instead of copy-pasted; and namespace partitioning, since modules are the highest-level, self-contained namespace layer in a Python program[^3].
- A program consists of one top-level ("script") file holding the main flow of control, plus zero or more module files that act as libraries of tools; module files generally do nothing useful when run directly and exist to be imported instead[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=860&annotation=W2GRSWHW)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=859&annotation=S9FKAE3C)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=860&annotation=W2GRSWHW)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=862&annotation=BLIIH45S)
