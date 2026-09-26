---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Effective User ID[^1]
> The effective user ID (euid) is the [[Process User ID|process user ID]] that defines a process's access rights — the "actor" carrying out the process's actions.

# Properties
- Set to a setuid program's owner during its execution, while the process's original user ID is kept as the [[Real User ID]].[^1]
- [[Sudo (Command)|`sudo`]] and other setuid programs explicitly change both the effective and real user IDs via `setuid()`, since unintended side effects and access problems can arise when a process's user IDs do not all match.[^2]
- The user credential consulted for many [[File Permissions (Unix)|filesystem]] and privilege checks; ordinarily equal to the [[Real User ID|real user ID]], and initialized instead from a setuid program's owner only when the kernel honors that bit during execution.[^3]
- Possessing an elevated effective user ID does not automatically make every requested operation legitimate: a program must still enforce policy based on the caller, the requested account, PAM results, and other context.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=FZNDBBCD)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=188&annotation=SI7EUE5I)
[^3]: [Linux Journey: Permissions](https://labex.io/linuxjourney/courses/permissions)
