---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Assignment Statement (Python)[^1]
> The statement that stores a reference to an [[Object (Python)|object]] in a name or data-structure component; assignment always creates a reference to the object rather than copying it, which is why Python [[Variable (Python)|variables]] behave more like pointers than like data-storage cells.

# Properties
- A name is created the first time it is assigned a value, so Python names never need to be predeclared; once assigned, a name is simply replaced by the object it references wherever it appears in an expression[^2].
- Using a name that has not yet been assigned is an error that raises an exception, rather than silently returning some default value — a deliberate design choice that makes typos in unassigned names easy to catch[^3].
- Assignment happens implicitly in many other Python contexts beyond the `=` statement — module imports, function and class definitions, `for`-loop targets, and function arguments are all forms of implicit assignment that bind a name or object component to an object reference the same way[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=414&annotation=GNMBVI3F)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=414&annotation=LUER6QR2)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=415&annotation=9NYFRI75)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=415&annotation=8JH637GL)
