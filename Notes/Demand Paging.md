---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Demand Paging[^1]
> Demand paging (on-demand paging) is the scheme by which the kernel loads and allocates a process's [[Page Table|memory pages]] only as the process actually needs them, rather than all at once.

# Properties
- A user process does not need all of its pages immediately available in order to run.[^1]
- When starting a program, the kernel first loads only the beginning of its instruction code into memory pages, and may allocate some working-memory pages to the new process.[^2]
- If the process reaches an instruction not in any page already loaded, or needs more working memory than initially allocated, the kernel loads or allocates the necessary pages and lets the process resume, triggering a [[Page Fault]] when the needed page is not yet ready.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=207&annotation=NPZD7E2J)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=207&annotation=9SF966SU)
