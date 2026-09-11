---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Symbolic Link[^1]
> A symbolic link is a file that points to another file or directory, effectively creating an alias, similar to a shortcut in Windows.

# Properties
- Offers quick access to obscure directory paths.
- Unlike a [[Hard Link]], may point to a target that does not exist, and is not tracked by its target [[Inode|inode's]] reference count.[^2]
- Ignored by filesystem integrity tools, which is why, unlike a hard link, it can safely reference a directory without threatening the directory structure's acyclic-tree assumption.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=60&annotation=UZNYJZP9)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=286&annotation=DLQ8AGVD)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=286&annotation=EQBBIR6C)
