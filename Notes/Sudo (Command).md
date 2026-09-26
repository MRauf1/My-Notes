---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] sudo (Command)[^1]
> `sudo` is the command that asks its configured policy whether the invoking user may run a command as a target user, most often [[Root User|root]].

# Properties
- The target account defaults to root, but a policy or the `-u USER` option can select another account.[^1]
- Authentication prompts and logging both depend on configuration.[^1]
- Best practice is to work from an unprivileged account for routine tasks and elevate with `sudo` only for a specific administrative purpose that is understood.[^1]

[^1]: [Linux Journey: User Management](https://labex.io/linuxjourney/courses/user-management)
