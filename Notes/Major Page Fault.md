---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Major Page Fault[^1]
> A major page fault is a [[Page Fault|page fault]] that occurs when the desired memory page is not in main memory at all, so the kernel must load it from disk or some other slow storage mechanism.

# Properties
- Many major page faults bog the system down, since the kernel must do substantial work to provide the pages, robbing normal processes of their chance to run.[^1]
- Some are unavoidable, such as those incurred loading a program's code from disk the first time it runs; the worst problems arise when memory runs low and the kernel starts swapping working-memory pages out to disk to make room for new pages.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=207&annotation=R2RJZP5B)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=208&annotation=HSKRBUDE)
