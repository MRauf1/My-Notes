---
tags:
  - computer_science
  - operating_systems
---

# Definition
> [!definition] Page Table[^1]
> A page table is the implementation of the memory address map used to translate a process's memory accesses into physical memory locations.

# Properties
- Initialized, maintained, and altered by the [[Kernel (Operating System)|kernel]].
- Used by the [[Memory Management Unit]] to support [[Virtual Memory]].
- Stored in memory itself and indexed by the virtual page number, which forms the upper portion of a virtual address; each entry gives the physical page number for that virtual page if it currently resides in main memory, while the low-order page offset bits carry through unchanged from virtual to physical address.[^2]
- Because a page table lookup is itself a memory access, every reference could take twice as long as necessary; a [[Translation-Lookaside Buffer]] caches recent translations to exploit the same temporal and spatial locality that makes the page table's own entries reusable.
- A reference (use) bit is set whenever a page is accessed, letting the operating system approximate [[Least Recently Used|LRU]] replacement without the cost of updating an exact recency ordering on every access; a dirty bit is set whenever a word in the page is written, indicating whether the page (a "dirty page") must be written back to secondary storage before its frame can be reused (write-back is the only practical write policy for virtual memory, since writing every store through to disk immediately would be far too slow).
- A range of techniques — including multi-level page tables and other compression schemes — reduce the memory a page table itself must occupy, since one entry per virtual page can otherwise be enormous.

[^1]: [How Linux Works: What Every Superuser Should Know](zotero://open-pdf/library/items/B4TILA8A?page=27&annotation=NBSDE75L)
[^2]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=455&annotation=XSCFGPWI)
