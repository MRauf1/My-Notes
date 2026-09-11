---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Placement Strategy[^1]
> The rule a [[Heap Allocator]] uses to pick which free block satisfies an allocation request.

# Types
- First fit — returns the first sufficiently large free block encountered while traversing the free list.[^1]
- Worst fit — arises when the free list is kept ordered from largest to smallest block, so the largest available block is always chosen first.[^2]

# Properties
- A strategy need not split the block it returns down to the requested size; returning it unbroken can waste the entire size difference as [[Internal Fragmentation]].[^1]
- Under an [[Explicit Free List|explicit free list]], the list's traversal order directly determines the placement strategy in effect, since reordering the list changes which block is found first.[^2]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=118&annotation=52UYKNYT)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=125&annotation=87TEWKDJ)
