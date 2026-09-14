---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Kernel (Operating System)[^1]
> The kernel is the core of the [[Operating System]]: software residing in main memory that tells the CPU what to do. It manages the hardware and acts primarily as the interface between the hardware and any running program.

# Properties
- Occupies the middle [[Abstraction Layer|level]] of a Linux system, between the hardware and [[User Space]].
- Runs in [[Kernel Mode]] and resides in [[Kernel Space]].
- Manages four general system areas: [[Process Management]], [[Main Memory]], [[Device Driver|device drivers]], and [[System Call|system calls]].
- Arbitrates fairly among the three basic kinds of hardware resources processes vie for — CPU, memory, and I/O — and is itself a software resource that processes use, for example to create new processes or communicate with one another.[^3]
- Responsible for [[Context Switch|context switching]] between processes.
- Initializes and maintains the [[Page Table|memory address map]] used to implement [[Virtual Memory]].
- Its first task after booting is to create the [[Init Process]], the only process the kernel creates directly; every other process descends from it via [[Fork and Exec|fork() and exec()]].[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=90&annotation=58T785F7)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=196&annotation=AKJU4RCC)
