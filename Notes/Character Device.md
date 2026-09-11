---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Character Device[^1]
> A character device is a [[Device File]] that works with a data stream: it can only be read from or written to a character at a time, and it has no size, unlike a [[Block Device]].

# Properties
- The kernel usually performs a direct read or write operation on the underlying device rather than indexing into it.[^1]
- Once the kernel has passed data to a device or process through a character device, it cannot back up and reexamine that data.[^2]
- [[Named Pipe|Named pipes]] and [[Terminal (Unix)|terminals]] are both accessed through character-device semantics.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=71&annotation=9J6H2SPY)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=72&annotation=PSACHZXP)
