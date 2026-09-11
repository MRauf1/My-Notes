---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Devtmpfs[^1]
> Devtmpfs is a [[Virtual Filesystem]], a simplified successor to the older devfs, that lets the kernel itself create [[Device File|device files]] as needed rather than requiring [[Udev|udevd]] to create them.

# Properties
- Was developed to solve a startup ordering problem: device files are needed early in boot, but udevd cannot depend on the devices it would otherwise be responsible for creating.[^2]
- Still notifies udevd whenever a new device becomes available; udevd then performs device initialization and process notification instead of creating the device file itself.[^1]
- udevd additionally creates symbolic links in `/dev` to further identify devices, such as the entries under `/dev/disk/by-id`.[^1]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=79&annotation=ZCJIRKGB)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=79&annotation=PCCI5NUF)
