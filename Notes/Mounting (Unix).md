---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Mounting (Unix)[^1]
> Mounting is the Unix process of attaching a [[Filesystem]] into the running system's directory hierarchy at a mount point, the common terminology being to "mount a device on a mount point."

# Properties
- Requires three things: the filesystem's device (e.g. a disk [[Partition (Operating Systems)|partition]], where the filesystem data actually resides), the filesystem type, and the mount point.[^2]
- The mount point is always an ordinary directory, not necessarily directly below `/`.[^2]
- At boot, the kernel mounts the root filesystem (`/`) itself, based on configuration data it reads.[^1]
- Because device names can change (they depend on the order in which the kernel finds devices), filesystems are commonly identified and mounted by [[Universally Unique Identifier (UUID)|UUID]] instead of by device name.[^3]
- Unmounting with `umount` causes the kernel to automatically synchronize any buffered writes to disk.
- Persistent mount configuration is conventionally kept in [[Fstab|/etc/fstab]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=100&annotation=AC8AGF3E)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=100&annotation=JUPMDNUG)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=101&annotation=XGLXX3JH)
