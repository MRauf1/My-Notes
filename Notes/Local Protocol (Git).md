---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Local Protocol[^1]
> The Local protocol is a [[Git Transfer Protocol]] in which the remote repository is simply another directory on the same host, typically reached through a shared filesystem.

# Properties
- When the remote is given as a plain filesystem path rather than a `file://` URL, Git copies or hard-links the needed files directly instead of running the process it normally uses to transfer data over a network, which makes a plain path generally faster.
- Its performance depends entirely on how fast the underlying filesystem can be accessed; a repository reached through a shared network filesystem can end up slower than the same repository accessed over a network protocol running on local disks.
- Because every user with access to the shared directory has full, unrestricted access to its files, this protocol offers no protection against a user accidentally corrupting the repository by altering or removing its internal Git files.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=111&annotation=GETQANWU)
