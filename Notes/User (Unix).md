---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] User (Unix)[^1]
> A user is an entity, identified by a numeric userid rather than a username, that can run processes and own files on a Unix system.

# Properties
- Every [[User Space|user-space]] [[Process (Computing)|process]] has a user owner and is said to run as that owner.
- A user may terminate or modify the behavior of only its own processes, within certain limits, and cannot interfere with other users' processes.
- A user may choose whether to share its files with other users, subject to [[File Permissions (Unix)|file permissions]].
- [[Group (Unix)|Groups]] are sets of users, letting members share file access with one another.
- [[Root User|Root]] is a special user exempt from the ordinary restrictions on affecting other users' processes and files.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
