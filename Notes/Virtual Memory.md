---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Virtual Memory[^1]
> Virtual memory is a memory access scheme in which a process accesses memory as if it had an entire machine to itself, rather than by the memory's actual physical location.

# Properties
- Enabled by the [[Memory Management Unit]] (MMU), CPU hardware that intercepts a process's memory accesses.
- The MMU translates a process's memory accesses into physical memory locations using a [[Page Table|memory address map]].
- The [[Kernel (Operating System)|kernel]] initializes and continuously maintains and alters this address map.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
