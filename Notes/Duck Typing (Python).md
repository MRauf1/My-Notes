---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Duck Typing (Python)[^1]
> The Pythonic practice of coding to an [[Object (Python)|object's]] interface — the operations it supports — rather than to its specific type, so that any object with a compatible interface works regardless of its type.

# Properties
- Explicit type testing (via `type(obj) == type(other)`, `type(obj) == sometype`, or `isinstance(obj, sometype)`) is supported by the language but generally discouraged, since it locks code to one type and forfeits the flexibility that [[Polymorphism (Python)|polymorphism]] otherwise gives it for free[^2].
- Type hints are meant only for documentation and use by third-party tools; the Python language itself does not use or enforce them, so they carry no runtime typing guarantee the way [[Strong Typing (Python)|strong typing]] does[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=135&annotation=ASATZZLC)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=135&annotation=MRP5DRBP)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=135&annotation=A2VT59SF)
