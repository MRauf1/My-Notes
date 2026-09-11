---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Internal Fragmentation[^1]
> Wasted space inside a block that a [[Heap Allocator]] has handed out, arising when a [[Placement Strategy]] returns a free block without splitting it down to the requested size.

# Properties
- Can occur even under a simple strategy like first fit, if the allocator chooses to return an oversized block unbroken rather than carving off the requested amount.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=118&annotation=52UYKNYT)
