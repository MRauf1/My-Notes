---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Semaphore[^1]
> A synchronization primitive initialized to some value, on which threads call `sem_wait` to decrement it and `sem_post` to increment it; if the value reaches zero, a further `sem_wait` blocks the calling thread until a `sem_post` is called.

# Properties
- Unlike a [[Mutex]], its wait and post calls can be made from different threads, since incrementing and decrementing are not tied to a single owner.[^2]
- A [[Mutex]] can be implemented as a semaphore that always waits before it posts (a "binary semaphore"), provided its value is never allowed to exceed one, since exceeding one breaks the mutual-exclusion guarantee; conversely, a semaphore can be implemented using a mutex.[^3]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=153&annotation=V3IHCDMU)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=154&annotation=CLLHASUW)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=154&annotation=7GMHEWIH)
