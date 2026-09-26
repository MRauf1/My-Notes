---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Access Control List (Unix)[^1]
> An access control list (ACL) is an additional Linux mechanism, beyond the traditional owner/group/other [[File Permissions (Unix)|permission triplets]], that can grant more finely grained file or directory access.

# Properties
- Can affect the resulting mode of a newly created object alongside the requested mode and the [[umask]].[^1]
- Along with mount options, capabilities, and mandatory access controls, can further affect the kernel's final access decision beyond the single matched permission triplet.[^1]

[^1]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
