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

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=281&annotation=76897CTD)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=286&annotation=DLQ8AGVD)
