---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] clone (System Call)[^1]
> The system call used to create a new [[Thread]]. It resembles [[Fork and Exec|fork()]], but performs no [[Copy-on-Write|copying]], letting the new thread share the calling process's address space, variables, heap, and file descriptors instead of receiving its own copy.

# Properties
- Invoked by the [[POSIX Threads (pthread)|pthread library]] rather than called directly by most programs: the library allocates stack space for the new thread and uses `clone` to start it executing at that stack address.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=131&annotation=U7Q4DELF)
