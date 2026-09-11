---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Universally Unique Identifier (UUID)[^1]
> A UUID is a software serial-number standard, each instance of which should be distinct, used to identify and [[Mounting (Unix)|mount]] a [[Filesystem]] or [[Device File|device]] independent of its possibly-changing device name.

# Properties
- Solves the instability of name-based mounting, since device names depend on the order in which the kernel discovers devices and so can change between boots.
- The preferred way to automatically mount filesystems from [[Fstab|/etc/fstab]] at boot time.[^2]
- Many distributions also use a device's UUID as its mount point when removable media is inserted.[^2]
- A filesystem's UUID can be changed, for example after duplicating a filesystem, to distinguish the copy from the original.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=101&annotation=XGLXX3JH)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=102&annotation=GCJF28Y3)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=102&annotation=GYASYJ7T)
