---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python Tuple[^1]
> An immutable [[Sequence (Python)|sequence]], written in parentheses, that behaves like a [[Python List|list]] which cannot be changed once created — used to represent a fixed collection of items.

# Properties
- Cannot grow or shrink like a list or dictionary because it is immutable, though it still supports arbitrary mixed types, nesting, and the usual sequence operations[^2].
- A one-item tuple requires a trailing comma to distinguish it from a plain parenthesized expression; more generally, it is the commas — not the parentheses, which can often be omitted — that actually construct a tuple[^3].
- Immutability applies only to the tuple's own top-level structure: a mutable object nested inside a tuple, such as a list, can still be changed in place[^4].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=128&annotation=ILQLT79M)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=128&annotation=GNHPIIXS)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=129&annotation=UYU3CF6L)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=337&annotation=HCTUN2GR)
