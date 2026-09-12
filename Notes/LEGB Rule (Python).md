---
tags:
  - computer_science
  - python
---

# Definition
> [!info] LEGB Rule (Python)[^1]
> Python's name-resolution order: an unqualified name referenced inside a function is searched for in up to four [[Scope (Python)|scopes]], in this order — Local (the function itself), Enclosing (any enclosing functions' locals), Global (the containing module), and Built-in — stopping at the first place the name is found.

# Properties
- Assigning a name inside a function always creates or changes that name in the function's own local scope by default, no matter what same-named variable might exist in an enclosing, global, or built-in scope, unless the name is declared with [[Global Statement (Python)|global]] or [[Nonlocal Statement (Python)|nonlocal]][^1].
- At the top level of a module (or at an interactive prompt), the local and global scope are one and the same, since there is no enclosing function.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=616&annotation=LNYA268G)
