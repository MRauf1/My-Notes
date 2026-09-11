---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Explicit Free List[^1]
> A [[Heap Allocator]] scheme that maintains a [[Doubly Linked List]] of only the currently free blocks, letting the allocator jump directly to the next and previous free blocks instead of scanning every block in the heap.

# Properties
- Reduces search time relative to an [[Implicit Free List]], since allocated blocks are skipped entirely.
- Gives the allocator control over the free list's ordering, which in turn determines its [[Placement Strategy]] — for instance, ordering blocks from largest to smallest produces a worst-fit strategy.
- The next/previous pointers are typically stored inside the free block itself, so every free block must be large enough to hold two pointers.
- Still requires [[Boundary Tag|boundary tags]] to correctly free a block and coalesce it with both of its neighbors, so it needs more code and complexity than an implicit free list.
- Its default search is a fast, simple find-first algorithm, corresponding to a first-fit placement strategy unless the list's ordering is changed.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=125&annotation=5FG37L5E)
