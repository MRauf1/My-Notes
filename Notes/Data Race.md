---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Data Race[^1]
> Two memory accesses form a data race if they are from different threads to the same location, at least one of them is a write, and they occur one after another without coordination. The result of a program containing a data race can change depending on how the events happen to occur.

# Properties
- Arises because parallel execution is easiest when tasks are independent, but tasks that cooperate must synchronize so that a reader knows when a writer has finished; see [[Multicore Microprocessor]].
- Avoided by using [[Mutual Exclusion]] and [[Atomic Operation|atomic operations]] to coordinate accesses to shared memory locations.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=144&annotation=8J4N3YAS)
