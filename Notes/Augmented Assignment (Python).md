---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Augmented Assignment (Python)[^1]
> A shorthand [[Assignment Statement (Python)|assignment]] form, such as `X += Y`, that combines a binary expression with an assignment to its left operand; it works on any type that supports the implied binary operation.

# Properties
- Compared to writing the long form `X = X + Y` out in full, the augmented form only evaluates the left-hand target once rather than twice, so it is usually both shorter to write and faster to run[^2].
- For a type that supports in-place changes, the augmented form automatically performs that in-place mutation instead of building a new object: for a [[Python List|list]], `L += X` behaves like the `extend` method — mutating `L` in place and accepting any iterable `X` — whereas `L = L + X` requires another list and always builds a new object[^3].
- Because `+=` mutates a [[Mutability (Python)|mutable]] object in place while `+` concatenation creates a new one, the two are not interchangeable when the object is shared: `L += X` is visible through every name referencing that same list, while `L = L + X` only rebinds `L` itself[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=432&annotation=43T6PP7J)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=433&annotation=FEF5SENR)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=434&annotation=39NDZHMP)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=435&annotation=RIDDWU95)
