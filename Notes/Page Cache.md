---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Page Cache[^1]
> The region of a system's physical memory used to cache disk data, avoiding slow disk I/O on repeated accesses to the same data.

# Properties
- Linux uses all otherwise-unused memory as page cache, an extreme instance of this general technique.
- Most valuable for random-access workloads on spinning [[Disk|disks]], where read/write latency is dominated by the seek time needed to move the read/write head into position, rather than for sequential access.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=298&annotation=2BAS6MQ7)
