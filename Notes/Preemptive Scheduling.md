---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Preemptive Scheduling[^1]
> A scheduling discipline in which a running process may be removed from the CPU immediately when a more preferred process becomes ready, rather than only when the running process itself gives up the CPU.

# Types
- Non-preemptive scheduling — a scheduled process keeps the CPU until it terminates (for example, due to a [[Signal (Computing)|signal]]), blocks waiting on a [[Synchronization (Computing)|concurrency primitive]], or exits normally; it runs to one of these points even if a higher-priority process later becomes ready.[^2]

# Properties
- Without preemption, a scheduler can cause [[Starvation (Scheduling)|starvation]], since an already-waiting process may never be scheduled.[^3]
- Distinct from the resource preemption used to break [[Hold and Wait]] in [[Deadlock Detection|deadlock recovery]]: scheduling preemption reclaims the CPU itself, not a resource a process holds.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=237&annotation=GCVDTUQW)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=237&annotation=IMPEJJEX)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=237&annotation=JT85ZZE5)
