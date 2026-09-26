---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Account (Unix)[^1]
> An account is a user entry in [[Passwd File|/etc/passwd]] together with its corresponding home directory.

# Properties
- Distinct from a [[User (Unix)|user]] alone, since it additionally requires a home directory.
- The home directory's path varies by system, and some accounts use an unconventional path or have no ordinary home at all — particularly service accounts, which exist to run software under a limited identity rather than to support interactive login (see [[Pseudo-User]]).[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=180&annotation=5V9EFH5C)
[^2]: [Linux Journey: User Management](https://labex.io/linuxjourney/courses/user-management)
