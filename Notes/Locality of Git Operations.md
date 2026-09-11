---
tags:
  - computer_science
  - tools
---

# Definition
> [!info] Locality of Git Operations[^1]
> Because a client in a [[Distributed Version Control System]] such as [[Git]] holds a full local mirror of a repository's data and history, nearly every operation in Git needs only local files and resources to run, without contacting a remote server.

# Properties
- Since the entire project history already resides on the local disk, most operations complete almost instantaneously.
- Because so little depends on network access, there is very little that cannot be done while offline or disconnected from a network.

[^1]: [Pro Git](zotero://open-pdf/library/items/Y53JUJJW?page=21&annotation=YBQXRGNG)
