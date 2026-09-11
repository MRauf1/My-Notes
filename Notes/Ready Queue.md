---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Ready Queue[^1]
> The queue of processes that are ready to run and are waiting for the [[CPU Scheduling|scheduler]] to allocate them a CPU core.

# Properties
- Organized as a FIFO queue under [[First-Come, First-Served (Scheduling)|first-come, first-served]] scheduling.
- A process removed from the CPU by [[Preemptive Scheduling|preemption]] — for example, at the end of a [[Round Robin (Scheduling)|round robin]] time quantum — is placed back onto the ready queue rather than discarded.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=235&annotation=PV5ZZXRC)
