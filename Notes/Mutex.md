---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Mutex[^1]
> Short for "mutual exclusion": an abstract data type providing lock and unlock operations that enforce [[Mutual Exclusion]] over a [[Critical Section]], so that only one thread may hold the lock at a time.

# Properties
- Not a primitive in the strictest sense, but one of the smallest building blocks with a useful threading API; also not a data structure in the sense of storing data, since it works with code rather than data — a mutex does not itself lock a variable.[^2]
- While a mutex is locked, other threads keep running normally; only a thread that specifically attempts to lock that same mutex is made to wait, and it acquires the lock as soon as the holding thread unlocks it.[^2]
- Can be implemented as a [[Semaphore|binary semaphore]] that always waits before it posts, and a semaphore can conversely be implemented from a mutex; some textbooks call a mutex a binary semaphore.[^3]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=147&annotation=DK9GYGQM)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=149&annotation=D9A4JY7T)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=154&annotation=7GMHEWIH)
