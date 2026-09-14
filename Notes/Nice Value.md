---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Nice Value[^1]
> The nice value (NI) is a hint a process gives the Linux kernel's scheduler, which the kernel adds to the process's current [[Scheduling Priority (Linux)|scheduling priority]] to determine its next time slot.

# Properties
- Defaults to 0.[^2]
- Can be raised, for example to 20 with the `renice` command, to make a background computation take a backseat to other processes and run only when they have nothing else to do.[^2]
- Mattered much more when many users shared a single machine.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=204&annotation=RGILPCRD)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=205&annotation=YZT9KFEE)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=205&annotation=Q6VGYHZP)
