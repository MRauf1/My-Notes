---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Critical Section[^1]
> A region of code that accesses a shared resource and must not be executed by more than one thread (or process) at a time.

# Properties
- Protected using [[Mutual Exclusion]], typically enforced with a [[Mutex]]: a thread already inside the critical section keeps running, while any other thread that tries to enter must wait until the first thread leaves.
- A [[Condition Variable]] wait is placed inside a critical section, together with its guarding [[Mutex]] and a loop, so the woken thread can safely re-check its condition.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=147&annotation=DK9GYGQM)
