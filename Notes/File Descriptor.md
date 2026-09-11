---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] File Descriptor[^1]
> A per-process handle that points to a [[File Description]]. File descriptors may be reused between different processes, but within a single process each one is unique.

# Properties
- May carry a notion of position within the underlying file, making it a seekable stream; the [[Operating System]] tracks this position as an attribute of the owning process.
- When a process is forked, only the file descriptor is cloned, not the [[File Description]] it points to, so the two resulting descriptors end up sharing the same underlying description.
- The operating system's file descriptor table can be treated as a [[Resource Allocation Graph]]; a directed cycle within it signals a [[Deadlock]] between processes contending over files.[^2]
- On Linux, this fd-level interface is one of two file-access abstractions available to a C program: C's standard I/O library additionally provides a portable wrapper around files that works across operating systems, implemented on Linux in terms of the fd-level calls themselves.[^3]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=90&annotation=GMJSCFCD)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=199&annotation=Y522WCUD)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=230&annotation=WBESRVPU)
