---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] sysfs[^1]
> sysfs is a [[Virtual Filesystem]] through which the Linux kernel provides a uniform view of attached devices, based on their actual hardware attributes, as a system of files and directories rooted at `/sys/devices`.

# Properties
- Addresses the shortcomings of the traditional `/dev` [[Device File|device file]] namespace, whose names reveal little about a device's hardware attributes and can change between reboots.
- Exposed under `/sys` in the [[Linux Directory Hierarchy]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=72&annotation=22MPPRZF)
