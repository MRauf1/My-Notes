---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Time Slice[^1]
> A time slice is the small fraction of a second for which a process is allowed to use the CPU before a context switch occurs.

# Properties
- Short enough that humans cannot perceive the switching between processes, yet long enough for significant computation — a process often finishes its current task within a single time slice.
- Ends with a [[Context Switch]] to another process.
- Enables [[Multitasking]] through repeated context switches.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
