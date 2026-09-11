---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] POSIX[^1]
> Portable Operating System Interface: a standard (or family of standards) that an [[Operating System]] must implement to be POSIX compliant, giving software a uniform way to interact with any compliant operating system.

# Properties
- Specifies the semantics that system calls such as [[Fork and Exec|fork() and exec()]] must satisfy.[^2]
- A process is only strictly required to have a thread and an address space, although real kernels provide substantially more per process.[^3]
- Every process has exactly one parent process.[^4]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=89&annotation=6DH98T3R)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=99&annotation=8FUXNT2U)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=93&annotation=KUQKMS4J)
[^4]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=95&annotation=Z28UCRY5)
