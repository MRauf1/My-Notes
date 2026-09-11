---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Program Break[^1]
> The boundary marking the current end of a process's data segment / heap region within its [[Process Memory Layout]], which can be moved to grow or shrink that region.

# Properties
- The heap starts at the top of the text segment and grows upward; calling malloc may push the program break upward to enlarge the heap.[^1]
- The data segment's end is also called the program break, and can be extended directly with `brk` / `sbrk`.[^2]
- Called the system break under [[POSIX]], which is moved with `sbrk`; most programs never call `sbrk` directly, instead going through a [[Heap Allocator]] built around it that chunks up the resulting space and tracks what is allocated and what is free.[^3]

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=91&annotation=NM658KME)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=92&annotation=3TUCWADC)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=113&annotation=QSSST9PI)
