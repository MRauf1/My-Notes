---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Shortest Job First[^1]
> A [[CPU Scheduling]] algorithm that, assuming all processes arrive at the same time, always runs the ready process with the shortest total CPU time next.

# Types
- Preemptive Shortest Job First (PSJF) — like shortest job first, but a newly arriving process preempts the currently running one if its total runtime is shorter than the current process's total runtime; ties may be broken either way.[^2]
- Shortest Remaining Time First (SRTF) — a variant of PSJF that compares each process's remaining runtime, rather than its total runtime, when deciding whether to preempt.[^2]

# Properties
- Requires knowing each process's total CPU burst time in advance, before it has actually run — information a scheduler cannot generally have.[^1]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=239&annotation=ZG53LUDM)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=240&annotation=YHEJ7VIM)
