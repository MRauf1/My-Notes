---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Boundary Tag[^1]
> Knuth's technique for letting a [[Heap Allocator]] coalesce a free block with its previous neighbor as well as its next one: a block's size is stored both at its start and at its end, so a block can look a few bytes behind itself to read its previous neighbor's size and jump backward to it.

# Properties
- Without boundary tags, an allocator can only find its next neighbor (by using its own stored size), since locating a previous neighbor otherwise requires no fixed offset to look up.
- Required by an [[Explicit Free List]] implementation to correctly free and [[Coalescing (Memory Allocation)|coalesce]] a block with both of its neighbors.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=124&annotation=YX59VUM7)
