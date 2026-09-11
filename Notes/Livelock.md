---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Livelock[^1]
> A state in which processes remain active and appear to be working, yet the system as a whole still fails to make forward progress, because the processes keep responding to one another in a repeating pattern without ever resolving their conflict.

# Properties
- Harder to detect than [[Deadlock]]: livelocked processes look busy to the operating system, whereas a deadlocked process is visibly waiting on a system-wide resource.
- Unlike deadlock, only necessary conditions for livelock are known, not sufficient ones — there is no fixed set of rules guaranteed to produce it.
- Ruled out formally by proving an invariant: if every step of the system, after some finite number of steps, is shown to lead to forward progress, the system provably cannot livelock.
- A stronger, bounded-wait property additionally proves that the system can be livelocked for at most $n$ cycles, which matters for systems such as stock exchanges.
- Can arise as a side effect of a deadlock-recovery strategy that repeatedly breaks [[Hold and Wait|hold and wait]].

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=199&annotation=UXNQ892T)
