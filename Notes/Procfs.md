---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Procfs[^1]
> Procfs is the [[Virtual Filesystem|virtual filesystem]], mounted on `/proc`, that represents each running process as a numbered directory named for its process ID (`/proc/self` for the current process), alongside additional kernel and hardware information such as `/proc/cpuinfo`.

# Properties
- Information not tied to a specific process has increasingly moved out of `/proc` and into [[sysfs|/sys]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=109&annotation=6RPW33C4)
