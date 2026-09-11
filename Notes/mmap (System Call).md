---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] mmap (System Call)[^1]
> A general system call for mapping a file, or POSIX shared memory, directly into a process's virtual address space; most commonly used as the general interface for creating memory shared between processes, such as between a parent and a child.

# Properties
- One of the two general avenues for [[Inter-Process Communication]]: rather than exchanging data through a kernel-provided API, mmap lets cooperating processes map the same underlying pages into their own address spaces and coordinate access to them directly.[^2]
- Must eventually be released with `munmap`, which tells the operating system the mapped pages are no longer in use, letting it write any changes back to disk and free the address range for reuse.[^3]
- `msync` can be used to flush changes in an mmap'ed region back to the underlying file without unmapping it.[^3]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=217&annotation=799RHI2D)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=216&annotation=X6ZGRFD3)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=218&annotation=NG48JDSN)
