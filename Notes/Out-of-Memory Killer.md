---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Out-of-Memory Killer[^1]
> The out-of-memory (OOM) killer is the [[Kernel (Operating System)|kernel]] mechanism that kills a running process to reclaim memory once a system has exhausted both real memory and [[Swap Space]].

# Properties
- Undesirable on general-purpose machines, since it can kill arbitrary desktop applications.
- High-performance servers instead avoid the situation entirely through monitoring and load-balancing systems that keep them from ever running out of memory.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=111&annotation=B8LJLJLU)
