---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Segregated Allocator[^1]
> A [[Heap Allocator]] design that divides the heap into separate areas handled by different sub-allocators depending on the size of the allocation request, typically grouping sizes into powers of two, with each size class maintaining its own free list.

# Properties
- Narrows each sub-allocator's search to requests of a single size class, rather than searching across all block sizes at once.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=126&annotation=4UZ6PRD7)
