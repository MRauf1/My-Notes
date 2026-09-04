---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Context Switch[^1]
> A context switch is the act of one process giving up control of the CPU so that another process can use it.

# Properties
- Performed by the [[Kernel (Operating System)|kernel]] as part of [[Process Management]].
- On a single-core CPU, only one process can actually use the CPU at any given moment, so context switches must occur frequently.
- Each process runs for a [[Time Slice]] before a context switch occurs.
- Repeated context switching produces the illusion of [[Multitasking]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
