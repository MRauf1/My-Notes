---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Argument Passing (Python)[^1]
> [[Function (Python)|Function]] arguments are passed by assignment — that is, by object reference: the caller and the function share the same objects, but argument names are never aliased to the caller's names, so reassigning an argument name inside the function has no effect on the caller.

# Properties
- Because arguments are references rather than copies, changing a passed-in [[Mutability (Python)|mutable]] object in place — as opposed to reassigning its argument name — can affect the object the caller sees, letting a mutable argument serve as both an input and an output of the call[^1].
- In practice, this makes immutable arguments behave like "pass by value" (the caller's value can never change, since it can't be mutated in place) and mutable arguments behave like "pass by pointer" (in-place edits are visible to the caller)[^2].
- Because `return` can package any number of values together in a [[Python Tuple|tuple]], a function can simulate "pass by reference" argument passing by returning updated values for the caller to reassign back onto its own names[^3].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=658&annotation=2Z7LZA4Y)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=659&annotation=PPZ6AE2D)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=664&annotation=GYXTT7FA)
