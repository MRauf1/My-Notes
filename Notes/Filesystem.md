---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Filesystem[^1]
> An implementation of the file interface: anything that satisfies the API of a filesystem, backed by a storage medium such as a [[Disk|hard disk drive or solid-state drive]], or RAM.

# Properties
- Under the Unix "everything is a file" philosophy, file operations abstract many different kinds of objects — network sockets, hardware devices, and on-disk data are all represented as file-like objects that follow the same conventions.[^2]
- Composed of files that are internally identified by their [[Inode]] rather than by name; a name is merely a directory entry pointing to an inode.
- Its directory structure is modeled as a graph rather than a strict tree once [[Hard Link|hard links]] are allowed, since a single inode can then be reachable from more than one directory path.[^3]
- A [[Virtual Filesystem]] can be mounted alongside on-disk filesystems, exposing dynamically generated or RAM-resident files through the same interface.
- Caches significant amounts of disk data in physical memory (its [[Page Cache]]), since disk I/O is comparatively slow.
- Sits atop a [[Partition (Operating Systems)|partition]] (or other block device); to reach a file's data, the kernel first locates the file's partition via the partition table, then searches that partition's filesystem database.[^4]
- Standardized across implementations by the [[Virtual File System (VFS)|Virtual File System]] abstraction layer, so user-space applications access any mounted filesystem type identically.[^5]
- Traditionally kernel-resident, but can instead be implemented as an ordinary user-space program via [[FUSE (Filesystem in Userspace)|FUSE]].
- Its data-pool bookkeeping rests on a [[Superblock]] (filesystem-wide metadata) and a [[Block Bitmap]] (free/used block tracking), alongside the per-file [[Inode|inode table]].
- Attached into the running system through [[Mounting (Unix)|mounting]], and checked for internal consistency by [[Filesystem Check (fsck)|fsck]], especially after an unclean shutdown.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=277&annotation=UTTQBSTA)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=278&annotation=CEK9U5HZ)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=284&annotation=GCKTGVN2)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=91&annotation=EIBDGY96)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=98&annotation=ZHV36S5Y)
