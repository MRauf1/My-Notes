---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Race Condition[^1]
> Occurs whenever a program's outcome depends on its particular sequence of events as scheduled by the processor, making execution non-deterministic: the same program can run multiple times and, depending on how the kernel happens to schedule its threads, produce different or incorrect results.

# Properties
- Need not originate in a program's own code — it can also arise from calling into provided or library code that is not [[Thread Safety|thread-safe]].[^2]
- A [[Data Race]] is one specific, well-defined case of a race condition: unsynchronized concurrent memory accesses, from different threads, at least one of which is a write.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=136&annotation=VF4D4KGS)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=139&annotation=3IN4TLJL)
