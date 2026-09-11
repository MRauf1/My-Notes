---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Heap Allocator[^1]
> A software layer, built around the [[Program Break|system break]], that manages a process's [[Process Memory Layout|heap]] on the program's behalf: it chunks up the memory obtained from the operating system and tracks which parts are currently allocated and which are free, so that most programs never need to move the system break directly.

# Types
- Implicit free list — a minimal-metadata scheme that locates the next block by walking past the current one.
- Explicit free list — a doubly linked list of only the free blocks, for faster search.
- Segregated allocator — divides the heap into size classes, each handled by its own sub-allocator and free list.

# Properties
- Memory freshly obtained from the operating system must be zeroed out, since leaving old physical RAM contents intact could let one process read another process's leftover data — a security leak; as a side effect, a `malloc` request satisfied from this fresh memory (before anything has been freed) is often already zero, which misleads some programmers into assuming allocated memory is always zeroed.
- Must track which regions of the heap are allocated and which are free, since deallocation during a program's execution opens up gaps that later requests can reuse.
- No single allocation scheme is best for every program: memory allocation is a moving target, since different programs do not follow the same distribution of allocation sizes and patterns.
- Central challenges include [[Internal Fragmentation|internal]] and [[External Fragmentation|external fragmentation]], and choosing a [[Placement Strategy]] for satisfying requests from the free list.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=113&annotation=QSSST9PI)
