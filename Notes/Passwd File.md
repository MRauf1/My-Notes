---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Passwd File[^1]
> `/etc/passwd` is the plaintext file that maps [[User (Unix)|usernames]] to numeric user IDs on a Unix system.

# Properties
- On most modern Linux systems, the password itself is not stored here but in the [[Shadow File|shadow file]], since normal users lack read permission for shadow, whereas `/etc/passwd` is world-readable.[^2]
- A user entry here, together with its corresponding home directory, is collectively known as an [[Account (Unix)|account]].[^3]
- Contains a few special users: the [[Root User|superuser]] (root) always has UID 0 and GID 0, while others, such as `daemon`, have no login privileges (see [[Pseudo-User]]).[^4]
- Lives in [[System Configuration Directory|/etc]] alongside other single-machine configuration, such as network details.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=178&annotation=F6FBQ9W9)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=179&annotation=K4E5EGUI)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=5V9EFH5C)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=DVAG39F5)
