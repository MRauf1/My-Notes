---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] User Mode[^1]
> User mode is the CPU execution mode that restricts a running program to a small, safe subset of memory and CPU operations.

# Properties
- Used by [[Process (Computing)|user processes]], which are confined to [[User Space]].
- Contrasts with [[Kernel Mode]].
- Limits the damage of a crash: the [[Kernel (Operating System)|kernel]] can clean up after a user-mode process that fails.
- The [[Root User]] runs in user mode despite being able to affect any user's processes or files.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
