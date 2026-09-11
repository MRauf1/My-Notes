---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Translation-Lookaside Buffer (TLB)[^1]
> A small [[Cache Memory|cache]] of recently used virtual-to-physical address mappings, used to avoid a full [[Page Table]] access on every memory reference.

# Properties
- Exploits the same temporal and spatial locality that makes page table entries themselves reusable: once a virtual page's translation is used, it is likely to be needed again soon.
- On a hit, the cached physical page number is used directly and the corresponding reference bit (and, on a write, dirty bit) is updated; on a miss, the processor must determine whether the translation is merely absent from the TLB (reloaded from the page table and retried) or the page itself is genuinely absent from memory (a true [[Virtual Memory|page fault]], handled via an [[Exception (Computer Architecture)|exception]]). TLB misses are far more frequent than true page faults, since the TLB holds far fewer entries than the page table has pages.
- Uses write-back for its own maintenance: reference and dirty bits accumulated in a TLB entry are copied back to the corresponding page table entry only when that TLB entry is evicted, rather than on every update, since TLB misses are expected to be rare.
- Enforces the write-access bit that lets the operating system mark a page read-only, a key mechanism for [[Virtual Memory|protection]] between processes.
- Caches on modern processors may be virtually addressed (accessed with the virtual address) or physically addressed (accessed only after TLB translation); aliasing — two different virtual addresses mapping to the same physical page — is a hazard specific to virtually addressed caches.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=461&annotation=GDFFUAJW)
