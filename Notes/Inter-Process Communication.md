---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Inter-Process Communication[^1]
> Any mechanism that deliberately breaks the default isolation between processes so that two or more of them can exchange data.

# Properties
- Achieved along two general avenues: asking the kernel for a dedicated communication interface, or asking the kernel to map the same physical pages into multiple processes' virtual address spaces (for example, via [[mmap (System Call)|mmap]]) and handling any resulting synchronization directly.
- Necessary precisely because a [[Process (Computing)|process]] is isolated by default and cannot otherwise read or modify another process's memory.
- Applications using network facilities don't have to involve two separate hosts: client-server or peer-to-peer processes on the same machine can use IPC instead to negotiate which of them does the work.[^2]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=216&annotation=X6ZGRFD3)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=272&annotation=WIYG6JZI)
