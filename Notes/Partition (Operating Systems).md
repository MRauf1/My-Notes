---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Partition (Operating Systems)[^1]
> A partition is a subdivision of a disk, defined in a small disk region called a [[Partition Table]], that the kernel presents as its own [[Block Device]] just as it would an entire disk.

# Properties
- Denoted on Linux by a number appended to the whole-disk block device's name, e.g. `/dev/sda1`, `/dev/sdb3`.[^1]
- To read a file's data, the kernel must first locate the file's partition via the partition table, then search that partition's filesystem database for the file.[^2]
- Altering a partition table is risky: it changes the point of reference used to locate a partition's filesystem, so deleted partitions become very difficult to recover, and no partition on the target disk should currently be mounted.[^3]
- Not every partition holds a [[Filesystem]] — one may instead serve as [[Swap Space]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=91&annotation=FSJXL3FV)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=91&annotation=EIBDGY96)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=94&annotation=7TZ85MYI)
