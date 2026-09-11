---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] First-Come, First-Served (FCFS)[^1]
> A [[CPU Scheduling]] algorithm that runs processes strictly in their order of arrival in the [[Ready Queue|ready queue]], which is maintained as a FIFO queue.

# Properties
- Simple to implement, since it requires no information about a process beyond its arrival order.
- Suffers from the [[Convoy Effect]], since a single long-running process forces every later arrival to wait behind it.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=241&annotation=HAAPWLHH)
