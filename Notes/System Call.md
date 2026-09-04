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

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
