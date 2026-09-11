---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Synchronization (Computing)[^1]
> Coordinates multiple concurrent tasks, such as [[Thread|threads]], so that they all finish in a correct, agreed-upon state.

# Properties
- Needed even between separate [[Process (Computing)|processes]] that share no memory and so have no internal [[Race Condition|race conditions]], whenever those processes must interact with shared resources in the surrounding system.[^2]
- Implemented using synchronization primitives such as [[Mutex|mutexes]], [[Semaphore|semaphores]], [[Condition Variable|condition variables]], and [[Barrier (Synchronization)|barriers]].

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=145&annotation=CXQNCFHY)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=186&annotation=XP8VBBI4)
