---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Coalescing (Memory Allocation)[^1]
> The merging of adjacent free blocks in a [[Heap Allocator|heap]] into a single larger free block, performed when a block being freed finds that a neighboring block is also free.

# Properties
- Requires checking both the next block, if one exists, and the previous block, if one exists; whichever of these is free gets merged with the block being freed.
- Finding the previous neighbor (rather than just the next one) requires a [[Boundary Tag]], since the current block's own size only reveals where the next block begins.
- Counteracts [[External Fragmentation]] by recombining smaller free blocks into larger contiguous ones.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=124&annotation=IC9IP4QH)
