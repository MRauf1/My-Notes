---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] External Fragmentation[^1]
> A condition where a [[Heap Allocator|heap]] holds enough total free memory to satisfy a request, but that free memory is divided up so no single contiguous block of the requested size is available.

# Properties
- Counteracted by [[Coalescing (Memory Allocation)|coalescing]] adjacent free blocks back into larger contiguous ones.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=118&annotation=ZYGBLFN9)
