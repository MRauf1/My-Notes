---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Orphan Process[^1]
> A process whose parent has terminated before waiting on it. Its parent process ID is reassigned to the [[Init Process|init process]] (PID 1), so a subsequent call to `getppid()` returns 1.

# Properties
- A parent need not wait on a child immediately and may continue executing other code; it orphans its children only if it exits before waiting on them.
- Briefly becomes a [[Zombie Process|zombie]] upon terminating, until the [[Init Process|init process]], which automatically waits on all of its children, removes it.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=104&annotation=V7GV7GSN)
