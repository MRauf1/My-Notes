---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] System Call[^1]
> A system call (syscall) is an interaction between a process and the kernel that performs a specific task a user process alone cannot do well, or at all.

# Properties
- One of the [[Kernel (Operating System)|kernel's]] four general responsibility areas, alongside [[Process Management]], memory, and [[Device Driver|device drivers]].
- Process creation via [[Fork and Exec|fork() and exec()]] is implemented as system calls.
- Distinct from [[Pseudodevice|pseudodevices]], which provide kernel-supported features to user processes without being traditional system calls.
- Comparatively expensive to perform.[^2]
- The only way a program running in [[User Space|user space]] can reach [[Kernel Space|kernel-space]] power; since the kernel itself carries out the call, this adds a layer of security that keeps ordinary user programs from being able to destroy the system.[^3]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=65&annotation=2FHVWR5S)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=89&annotation=MU5CZM96)
