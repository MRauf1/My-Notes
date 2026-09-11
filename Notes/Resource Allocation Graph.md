---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Resource Allocation Graph[^1]
> A [[Directed Graph]] modeling which resources are held by which processes and which processes are waiting on which resources: an edge from a resource node to a process node means the process holds that resource, and an edge from a process node to a resource node means the process is requesting it.

# Properties
- If the graph contains a [[Graph Cycle|cycle]] in which every resource involved has only a single instance, the processes in that cycle are [[Deadlock|deadlocked]].
- A deadlock can be detected by traversing the graph for a cycle, for example with a depth-first search.
- Cycles occur routinely in a running operating system without producing deadlock, since the OS may preempt a process and break the cycle before it becomes permanent.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=196&annotation=VE9577FC)
