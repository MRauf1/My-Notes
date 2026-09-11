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

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=277&annotation=UTTQBSTA)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=278&annotation=CEK9U5HZ)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=284&annotation=GCKTGVN2)
