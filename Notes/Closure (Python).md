---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Closure (Python)[^1]
> A nested [[Function (Python)|function]] that remembers the values of variables from an enclosing function's [[Scope (Python)|scope]], even after that enclosing call has already returned.

# Properties
- Also called a factory function: an enclosing function that creates and returns such a nested function produces a fresh, independent packet of retained state on each call, rather than one state shared across all of them.
- The retained values can be read through ordinary scope lookup, but changing them from within the nested function requires declaring them with [[Nonlocal Statement (Python)|nonlocal]].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=633&annotation=9VYHYCCP)
