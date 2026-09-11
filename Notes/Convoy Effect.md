---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Convoy Effect[^1]
> A situation in which a process that occupies the CPU for a long time forces all subsequent processes — even ones with much smaller resource needs — to queue up and wait behind it, like vehicles behind a slow lead car in a convoy.

# Properties
- A weakness of [[First-Come, First-Served (Scheduling)|first-come, first-served]] scheduling, whose FIFO [[Ready Queue]] enforces strict arrival order regardless of how long each process needs the CPU.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=238&annotation=L248ESFJ)
