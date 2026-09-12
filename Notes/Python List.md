---
tags:
  - computer_science
  - python
---

# Definition
> [!info] Python List[^1]
> The most general [[Sequence (Python)|sequence]] type in Python: a positionally ordered, mutable collection of arbitrarily typed objects with no fixed size.

# Properties
- Unlike an [[Array|array]] in lower-level languages, a Python list has no fixed type constraint — a single list can mix an integer, a string, and a float — and no fixed size, growing and shrinking on demand as items are added or removed[^2].
- Still cannot be indexed or assigned past its current end: referencing or assigning an out-of-range offset is always an error, since Python does not pre-allocate unused slots[^3].
- Supports arbitrary nesting with other core object types — a list can contain a dictionary that contains another list, and so on, as deeply as needed[^4].
- CPython implements the list as a resizable array, making it the practical equivalent of an [[ArrayList]] rather than a fixed-size [[Array]].

[^1]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=114&annotation=22XKVRIY)
[^2]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=114&annotation=RB36D79C)
[^3]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=115&annotation=XKGQA3BC)
[^4]: [Learning Python](zotero://open-pdf/library/items/C6PDA59I?page=116&annotation=7S788A8S)
