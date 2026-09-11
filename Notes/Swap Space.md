---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!info] Swap Space[^1]
> Swap space is the disk area that the Linux [[Virtual Memory|virtual memory]] system uses to hold pages moved out of RAM ("swapped out") when real memory runs low, extending effective memory with disk storage.

# Properties
- Can be a dedicated [[Partition (Operating Systems)|partition]] or, to avoid repartitioning, an ordinary file.[^2]
- Traditional Unix guidance recommended reserving at least twice as much swap as real memory, but today's large, variable disk and memory capacities have undermined that rule of thumb.[^3]
- Heavy reliance on swap causes serious performance problems, since disk I/O is far slower than main memory; the only remedies are more memory, fewer active processes, or tolerating the slowdown.[^4]
- The kernel may swap out a process's memory simply to grow the disk cache, which is why some administrators (e.g. of high-performance servers) disable swap entirely on systems that should never incur disk I/O.[^5]
- If both real memory and swap are exhausted, the kernel invokes the [[Out-of-Memory Killer|out-of-memory (OOM) killer]] to reclaim memory.[^6]

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=110&annotation=5KYIPGRA)
[^2]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=110&annotation=D64CKF4F)
[^3]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=111&annotation=USBH4FRD)
[^4]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=111&annotation=SJBLEJ76)
[^5]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=111&annotation=THYEV2UF)
[^6]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=111&annotation=B8LJLJLU)
