---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] File Description[^1]
> The struct that a [[File Descriptor]] points to. For a file on a filesystem, it holds information such as the file's path and how far into the file it has been read.

# Properties
- A single file description can be pointed to by more than one [[File Descriptor|file descriptor]], such as after a [[Fork and Exec|fork()]], since forking clones only the descriptor, not the description it points to.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=100&annotation=3JREYF43)
