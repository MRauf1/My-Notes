---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Single-User Mode[^1]
> Single-user mode is a boot mode that brings the system up to a root shell quickly, skipping ordinary service startup — [[System V Init|System V init's]] [[Runlevel|runlevel]] 1, also reachable via an `-s` [[Boot Loader|boot loader]] parameter, typically requiring the root password.

# Properties
- Offers few amenities: networking is generally unavailable or hard to use, there is no GUI, and even the terminal may not work fully correctly.[^2]
- Generally considered inferior to booting a [[Live Image (Linux)|live image]] for system repair, for exactly this reason.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=172&annotation=5BPF5HNH)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=172&annotation=TTDEAWYH)
