---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] File Permissions (Unix)[^1]
> Every Unix file has a set of permissions that determine whether a [[User (Unix)|user]] can read, write, or run the file.

# Properties
- The [[Root User]] is exempt from these ordinary restrictions and may read any file on the system.
- A file with its setuid permission bit set runs as its owner rather than as the invoking user when executed; see [[Setuid]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=58&annotation=A4TEJCNV)
