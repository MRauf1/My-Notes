---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] FUSE (Filesystem in Userspace)[^1]
> FUSE is the Linux feature, inspired by Plan 9's 9P protocol, that lets a [[Filesystem]] be implemented as an ordinary user-space program instead of in the kernel.

# Properties
- The kernel need only act as a conduit for system calls to the user-space implementation, so filesystem support does not need to live in the kernel at all.[^2]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=98&annotation=64H4RGNY)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=116&annotation=38RJMM9E)
