---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Inode[^1]
> The underlying object that constitutes a file on a [[Filesystem]]; a file's name is merely a directory entry pointing to its inode, so a file should be understood to be its inode rather than any of its names.

# Properties
- Keeps a reference count, incremented and decremented as [[Hard Link|hard links]] to it are created and destroyed, so the filesystem can tell whether an inode's contents are still needed once a name referencing it is removed (via `rm` or `unlink`).[^2]
- Only [[Hard Link|hard links]] are tracked by this reference count; a [[Symbolic Link]] is allowed to point to a non-existent target and so is not counted.[^2]
- Identified by number in a filesystem's inode table; a directory inode is itself just a list of filenames paired with the inode numbers they point to.[^3]
- The root inode is unusual in that the filesystem's [[Superblock]] itself holds a reference to it — since the superblock is how the root inode is located — counting as an additional link beyond its directory entries.[^4]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=281&annotation=76897CTD)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=286&annotation=DLQ8AGVD)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=112&annotation=58AU8LMG)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=115&annotation=QHH5XGSH)
