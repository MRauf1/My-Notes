---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Page Fault[^1]
> A page fault is the event in which a process triggers the kernel to intervene because a [[Page Table|memory page]] it wants to use is not ready, so the kernel takes control of the CPU from the process to get the page ready.

# Types
- [[Minor Page Fault]]
- [[Major Page Fault]]

# Properties
- Arises naturally under [[Demand Paging]], since a process's pages are not all loaded in advance.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=207&annotation=3DKSMFL3)
