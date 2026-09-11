---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Init Process[^1]
> The first process created directly by the kernel during booting (traditionally named init.d, or systemd on more modern systems). It is the only process the system creates explicitly; every other process is instantiated from it via [[Fork and Exec|fork() and exec()]].

# Properties
- Boots up user-facing programs such as graphical interfaces and terminals.
- Has a process ID (PID) of 1, and is the ultimate ancestor of every other process on the system.
- Adopts [[Orphan Process|orphaned processes]] whose original parent has terminated, and automatically waits on them so they do not linger as [[Zombie Process|zombies]].

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=90&annotation=58T785F7)
