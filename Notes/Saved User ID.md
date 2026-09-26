---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Saved User ID[^1]
> The saved user ID is the [[Process User ID|process user ID]] that stores a previous user ID a process can switch its [[Effective User ID|effective user ID]] back to during execution.

# Properties
- Lets a process temporarily drop and later reclaim elevated privileges without a further setuid program invocation.[^1]
- Subject to the rules of the credential-changing system calls: a privileged program can temporarily switch its effective user ID to a less privileged value, perform ordinary work under that reduced authority, and later restore the saved identity only for a narrowly scoped operation.[^2]
- Safer than retaining elevated authority for a program's entire run, but only when implemented correctly: privilege should be permanently discarded once no longer needed, and every credential-changing call should be checked for failure.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=188&annotation=5YQX3BKU)
[^2]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
