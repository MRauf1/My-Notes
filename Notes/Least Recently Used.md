---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Least Recently Used (LRU)[^1]
> A replacement policy that evicts the block (or page) that has gone unused for the longest time, using the past to predict the future.

# Properties
- Used to choose which way to evict in a [[Set-Associative Cache]] and which page to evict on a [[Virtual Memory|page fault]].
- For a two-way set-associative cache, exact LRU needs only a single bit per set, set whenever one of the two elements is referenced; exact tracking becomes progressively harder to implement as associativity grows, since it otherwise requires updating a full recency ordering on every access.
- Because exact LRU is too expensive for a large page table to maintain on every memory reference, operating systems typically approximate it using a reference bit (use bit) per page, periodically cleared and sampled, rather than tracking a precise access order; see [[Page Table]].

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=432&annotation=JLBQHR5P)
