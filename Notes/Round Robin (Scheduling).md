---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Round Robin (Scheduling)[^1]
> A [[CPU Scheduling]] algorithm that runs ready processes in order of arrival, like [[First-Come, First-Served (Scheduling)|first-come, first-served]], but forcibly returns the running process to the [[Ready Queue|ready queue]] after a fixed [[Time Slice|time quantum]] if it has not already finished or blocked.

# Properties
- Prevents long-running processes from starving the rest of the ready queue, since every process is guaranteed to be revisited after at most one time quantum's wait for each of its competitors.
- Reduces to [[First-Come, First-Served (Scheduling)|first-come, first-served]] as the time quantum approaches infinity, since no process is ever forced back onto the ready queue before finishing.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=242&annotation=7CKVXW2T)
