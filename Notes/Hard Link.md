---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Hard Link[^1]
> A directory entry that points directly to an existing file's [[Inode]] rather than to another name; creating one increments the target inode's reference count, distinguishing it from a [[Symbolic Link]], which merely names a path.

# Properties
- Filesystems generally forbid hard-linking directories: since a directory conventionally has only one parent (referenced by `..`), allowing more than one hard link to a directory would turn the directory structure into an arbitrary graph rather than an acyclic tree reachable from the root, breaking assumptions that filesystem integrity tools and recursive searches rely on — a recursive search could fail to terminate, and an integrity tool could become unable to repair the filesystem.[^2]
- Symbolic links are exempt from this restriction because filesystem integrity tools simply ignore them, which is why they, unlike hard links, can safely reference directories.[^2]
- Used to implement efficient incremental backups: once an archive holds a copy of a file, a later archive can hard-link to that same copy instead of duplicating it, so only files that actually changed consume new storage.[^3]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=286&annotation=DLQ8AGVD)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=286&annotation=EQBBIR6C)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=286&annotation=FQXZDHA6)
