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
- Exempt from the ordinary restrictions of [[File Permissions (Unix)|file permissions]] and may read any file on the system.
- Modern Linux can divide up root's traditionally broad power through capabilities, namespaces, mandatory access controls, and service confinement, so treating root as having unlimited power in every context is an oversimplification.[^2]
- Best practice is to work from an unprivileged account for routine tasks and elevate to root, typically via [[Sudo (Command)|sudo]], only for a specific administrative purpose that is understood.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Linux Journey: User Management](https://labex.io/linuxjourney/courses/user-management)
