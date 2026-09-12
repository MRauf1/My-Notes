---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Nonlocal Statement (Python)[^1]
> A declaration inside a nested [[Function (Python)|function]] that gives it read and write access to a name already assigned in a syntactically enclosing function's local scope, rather than creating a new local name for it.

# Properties
- Unlike [[Global Statement (Python)|global]], a name declared `nonlocal` must already be assigned somewhere in an enclosing function; it is an error to use `nonlocal` for a name no enclosing function assigns, and lookup for that name never falls through to the global or built-in scopes[^2].
- Gives [[Closure (Python)|closures]] a dedicated way to retain changeable state between calls, without resorting to global variables or classes.

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=636&annotation=R638G4BJ)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=637&annotation=NIBU4LU3)
