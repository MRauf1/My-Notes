---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Condition Variable[^1]
> A synchronization primitive that lets a set of threads sleep until woken; a thread wakes others by signaling the condition variable rather than addressing them directly, and the API can wake either a single thread (`pthread_cond_signal`) or all of them (`pthread_cond_broadcast`), with the operating system choosing which thread wakes when only one is requested.

# Properties
- Despite the name, `pthread_cond_signal` / `pthread_cond_broadcast` have nothing to do with a POSIX [[Signal (Computing)|signal]].[^2]
- Used together with a [[Mutex]] and a loop: a woken thread re-checks its condition inside the resulting [[Critical Section]], since waking up alone does not guarantee the condition still holds.[^2]
- A thread waiting on a condition variable may experience a [[Spurious Wakeup]].[^3]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=156&annotation=2ELSJENB)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=156&annotation=7DDI7TWN)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=156&annotation=EDSEYSSB)
