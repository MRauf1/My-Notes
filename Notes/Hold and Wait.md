---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Hold and Wait[^1]
> One of the [[Coffman Conditions]]: a process already holding at least one resource is simultaneously waiting to acquire one or more additional resources.

# Properties
- A common [[Deadlock Detection|deadlock-recovery]] technique breaks this condition by having the operating system preempt (forcibly reclaim) one of a deadlocked process's held resources, freeing it for another process to use.[^2]
- Repeatedly preempting resources to break hold-and-wait can itself produce a [[Livelock]] if the same pattern of preemption keeps recurring; choosing the resource to preempt at random makes this unlikely in practice, or short-lived when it does occur.[^2]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=199&annotation=UXNQ892T)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=200&annotation=VDSQR39K)
