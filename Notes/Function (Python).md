---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Function (Python)[^1]
> A package of code invoked by name: a `def` [[Compound Statement (Python)|statement]] that labels and groups a set of statements so they can be run more than once, optionally computing a result and accepting parameters that serve as inputs that may differ on each call.

# Properties
- `def` is executable code, not a compile-time declaration: the function does not exist until Python actually runs its `def`, so a `def` can legally appear anywhere a statement can — even nested inside an `if`, a loop, or another `def`[^2].
- Factoring an operation into a function, rather than duplicating its code by copy-paste, means future changes to that operation need to be made in only one place, and lets complex systems be split into smaller, reusable, independently understandable parts.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=591&annotation=D7CBHPRH)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=599&annotation=K4272FX7)
