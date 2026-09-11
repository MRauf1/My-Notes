---
tags:
  - computer_science
  - systems_programming
---

# Definition
> [!info] Multi-Level Page Table[^1]
> A [[Page Table]] design that addresses the size problem of a single flat page table on a large address space (such as a 64-bit one) by splitting it into multiple levels: a top-level table of pointers to second-level sub-tables, which in turn hold the frame numbers for a program's pages, letting entirely unused regions of the address space omit their sub-tables altogether.

# Properties
- To translate an address, the MMU indexes into the top-level table to find a pointer to the appropriate sub-table, then indexes into that sub-table to obtain the frame number, and finally adds the address's offset bits to locate the byte within that frame.[^2]
- Sharply reduces the memory a page table must occupy compared to a single-level table, since sub-tables covering entirely unused regions of the address space can be omitted.[^3]
- Trades this space savings for time: each additional level adds one more memory access to a translation, so a two-level page table makes an otherwise-uncached memory reference three times as slow as a direct access, versus twice as slow for a single-level table.[^4]
- The added latency from walking multiple levels is part of why hardware relies on a [[Translation-Lookaside Buffer]] to cache recent translations and avoid repeating the walk.

[^1]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=212&annotation=UT4SWNV4)
[^2]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=213&annotation=VRYFRBZ5)
[^3]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=214&annotation=S974WZ8J)
[^4]: [Systems Programming](zotero://open-pdf/library/items/8Y3AE875?page=214&annotation=9BPQARK3)
