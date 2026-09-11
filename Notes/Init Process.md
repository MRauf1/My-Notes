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
- Marks the user space start of the [[Boot Process (Linux)|boot process]]: once the kernel starts init, it sets the rest of the system's processes in motion, and near the end of booting starts a process that allows login.[^2]
- A user-space program like any other, conventionally found in `/sbin`; its main purpose is to start and stop the system's essential service processes, though modern implementations take on more responsibilities.[^3]
- Three major Linux implementations exist: [[System V Init|System V init]] (strictly sequential), [[Systemd|systemd]] (goal-oriented, the emerging standard), and [[Upstart]] (event-driven, historically used by Ubuntu).[^4]
- Also controls how the system shuts down and reboots, regardless of which implementation is running — see [[Shutdown Process (Linux)]].

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=90&annotation=58T785F7)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=119&annotation=P7KDIEIF)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=4PUCVZPJ)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=137&annotation=CGQGRP2G)
