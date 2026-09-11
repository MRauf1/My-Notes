---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Virtual File System (VFS)[^1]
> The Virtual File System is the Linux kernel's abstraction layer that gives every [[Filesystem]] implementation a standard interface, so that user-space applications access files and directories in the same manner regardless of which filesystem is mounted.

# Properties
- Has enabled Linux to support an extraordinarily large number of filesystems.[^1]
- Guarantees that system calls such as `stat()` always return inode numbers and link counts, even on filesystems with no real notion of either — retained mainly for backward compatibility, so such numbers may be meaningless on those filesystems.[^2]
- Distinct from a [[Virtual Filesystem|virtual filesystem]] (e.g. [[Procfs|procfs]], [[sysfs]], [[Tmpfs|tmpfs]]): that term names a *kind* of filesystem whose data is not backed by physical storage, whereas the VFS is the interface layer through which every filesystem — physical or virtual — is accessed.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=98&annotation=ZHV36S5Y)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=115&annotation=T4C5PLMZ)
