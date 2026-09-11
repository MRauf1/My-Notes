---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Terminal (Unix)[^1]
> A terminal is a [[Character Device|device]] for moving characters between a user process and an I/O device, tracing back to typewriter-based physical terminals.

# Properties
- `/dev/tty` denotes the controlling terminal of the current process: a synonym for whichever terminal it is currently reading from and writing to, if any, since a process need not be attached to a terminal at all.[^2]

# Types
- [[Virtual Console|Virtual consoles]] — e.g. `/dev/tty1`, the first virtual console.
- [[Pseudoterminal|Pseudoterminals]] — e.g. `/dev/pts/0`, the first entry of the dedicated `/dev/pts` filesystem.
- Serial-port terminal devices, such as `/dev/ttyS0`.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=76&annotation=QD2FQXDY)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=76&annotation=NAG9EH8V)
