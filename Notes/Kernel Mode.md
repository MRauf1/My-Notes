---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Kernel Mode[^1]
> Kernel mode is the CPU execution mode in which running code has unrestricted access to the processor and main memory.

# Properties
- Used exclusively by the [[Kernel (Operating System)|kernel]], which resides in [[Kernel Space]].
- Contrasts with [[User Mode]], which restricts a process to a small, safe subset of memory and CPU operations.
- Its unrestricted access is powerful but dangerous: a mistake in kernel-mode code can crash the entire system.
- The [[Root User]] still runs in [[User Mode]], not kernel mode, despite its elevated privileges.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
