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
- `sudo` and other setuid programs explicitly change both the effective and real user IDs via `setuid()`, since unintended side effects and access problems can arise when a process's user IDs do not all match.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=187&annotation=FZNDBBCD)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=188&annotation=SI7EUE5I)
