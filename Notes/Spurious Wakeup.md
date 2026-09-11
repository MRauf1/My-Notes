---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Spurious Wakeup[^1]
> A thread waiting on a [[Condition Variable]] appearing to wake up with no signal having actually been sent.

# Properties
- Exists for performance: on a multi-CPU system, a race condition could otherwise let a wake-up (signal) request go unnoticed by the kernel; rather than closing this gap directly, the kernel wakes the thread whenever the loss might have occurred, relying on the program re-testing its condition to recover safely.[^2]
- Analogous to the spurious failure of a weak [[Atomic Operation|atomic]] instruction, which may report failure even though the operation actually succeeded.[^1]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=156&annotation=EDSEYSSB)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=156&annotation=32EWT6MG)
