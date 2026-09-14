---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Minor Page Fault[^1]
> A minor page fault is a [[Page Fault|page fault]] that occurs when the desired page is actually already in main memory, but the [[Memory Management Unit|MMU]] does not know where it is.

# Properties
- Can happen when a process requests more memory, or when the MMU lacks enough space to store all of a process's page locations.[^1]
- Resolved cheaply: the kernel tells the MMU about the page and lets the process continue.[^1]
- Common and generally not a concern, except for programs demanding maximum memory performance.[^1]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=207&annotation=MQF3JD8G)
