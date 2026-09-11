---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Deadlock Detection[^1]
> A [[Deadlock]]-handling strategy that lets the system enter a deadlocked state and then uses information about the deadlock to break it, rather than trying to prevent deadlock from occurring in the first place.

# Properties
- For example, the operating system can track which resources (such as files, via [[File Descriptor|file descriptors]]) each process holds, detect a cycle in that tracking structure — a [[Resource Allocation Graph]] — and break one process's hold on a resource, for instance through scheduling, to let the system proceed.
- Favored over static prevention because it is generally impossible to know in advance which resources a program will request without actually running it, an instance of [[Rice's Theorem]].
- Repeatedly preempting resources to resolve detected deadlocks risks [[Livelock]]; systems address this by choosing which resource to preempt at random, which in practice keeps livelock rare or short-lived.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=199&annotation=Y522WCUD)
