---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Implicit Free List[^1]
> A [[Heap Allocator]] scheme in which blocks are not linked by explicit pointers; instead, the allocator reaches the next block by using the current block's own stored size to compute where it ends.

# Properties
- Metadata can be minimal, needing to record only the size of each block.
- Search must walk over both allocated and free blocks in sequence, since there is no separate list of only the free ones (contrast with an [[Explicit Free List]]).

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=121&annotation=CIELJWRQ)
