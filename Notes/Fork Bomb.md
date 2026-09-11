---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Fork Bomb[^1]
> An attempt to create an unbounded number of processes by repeatedly calling [[Fork and Exec|fork()]], which brings a system to a near-standstill as it tries to allocate CPU time and memory to all of the resulting runnable processes.

# Properties
- Mitigated by imposing an upper limit on the number of processes a single user may create, for example via `setrlimit()`, or by revoking a user's login rights.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=97&annotation=E6NGBL53)
