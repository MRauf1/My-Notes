---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] umask[^1]
> The umask (file-creation mask) is a per-process setting that prevents selected permission bits from being set when that process creates a new filesystem object.

# Properties
- Not a complete default mode: the creating application first requests a mode, and the kernel removes whatever bits the umask prohibits — conceptually, `resulting mode = requested mode AND NOT umask`.[^1]
- Scoped to the shell or process that sets it and its descendants: changing it in one shell does not alter its parent process or unrelated sessions, and files created earlier keep their existing modes.[^2]
- Made persistent by configuring it in the appropriate login, shell, PAM, service-manager, or application configuration for the environment, since the correct location varies and services may set their own umask.[^2]

[^1]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
[^2]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
