---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Kernel (Operating System)[^1]
> The kernel is the core of the operating system: software residing in main memory that tells the CPU what to do. It manages the hardware and acts primarily as the interface between the hardware and any running program.

# Properties
- Occupies the middle [[Abstraction Layer|level]] of a Linux system, between the hardware and [[User Space]].
- Runs in [[Kernel Mode]] and resides in [[Kernel Space]].
- Manages four general system areas: [[Process Management]], [[Main Memory]], [[Device Driver|device drivers]], and [[System Call|system calls]].
- Responsible for [[Context Switch|context switching]] between processes.
- Initializes and maintains the [[Page Table|memory address map]] used to implement [[Virtual Memory]].

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
