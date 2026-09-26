---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Sticky Bit[^1]
> The sticky bit is a directory-mode bit that restricts removing or renaming the directory's entries to a suitably privileged process, the directory owner, or the entry's own owner, even though the directory is otherwise writable by other authorized users.

# Properties
- Without it, a writable directory normally lets any authorized user remove or rename entries within it, even ones they do not themselves own.[^1]
- Ordinary directory write and search permissions are still required regardless; the bit does not itself grant write or search access, only restricts removal and rename once those permissions already allow directory modification.[^1]
- Concerns directory entries only: it does not prevent a file's owner from editing that file's contents when the file's own permissions otherwise allow it, and it does not make the directory private.[^1]

[^1]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
