---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Superblock[^1]
> The superblock is the [[Filesystem]]-wide structure that records a filesystem's metadata, including where to find its root [[Inode]].

# Properties
- Its reference to the root inode counts as one of that inode's links, alongside the directory entries pointing to it.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=115&annotation=QHH5XGSH)
