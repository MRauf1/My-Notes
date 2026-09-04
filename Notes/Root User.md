---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Root User[^1]
> The root user (superuser) is the Unix user privileged to terminate or alter any other user's processes and read any file on the local system.

# Properties
- Exempt from the ordinary restriction that a [[User (Unix)|user]] may affect only its own processes and files.
- A person who can operate as root has root access and is an administrator on a traditional Unix system.
- Still runs in [[User Mode]], not [[Kernel Mode]], despite its elevated privileges.
- System designers try to minimize the need for root access, since operating as root makes mistakes difficult to identify or correct.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
