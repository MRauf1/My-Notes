---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Mutability (Python)[^1]
> The classification of every [[Object (Python)|Python object]] as either mutable (changeable in place after creation) or immutable (unchangeable).

# Properties
- Among the core object types, numbers, strings, and [[Python Tuple|tuples]] are immutable, while [[Python List|lists]], [[Python Dictionary|dictionaries]], and [[Python Set|sets]] are mutable and can grow, shrink, or change in place freely[^1].
- An immutable object's operations always return a new object rather than modifying the original — every [[Python String|string]] operation, for instance, produces a new string[^2].
- Text can still be mutated in place only through workarounds: expanding it into a list of characters and rejoining it, or using the special-purpose `bytearray` object, which supports in-place changes but only for narrow, at-most-8-bit-wide text[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=106&annotation=2JZ7VHEN)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=105&annotation=BFV2SQTP)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=106&annotation=YKT7DF44)
