---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Set-Associative Cache[^1]
> A [[Cache Memory|cache]] with a fixed number $n \ge 2$ of locations where each block may be placed, called an $n$-way set-associative cache. The cache is organized into sets of $n$ blocks each; a memory block maps to exactly one set (by its index field) but can occupy any of the $n$ ways within that set, so all tags in the selected set must be searched — in parallel, for speed — to determine a hit.

# Types
- Fully associative cache — the limiting case where a block may be placed anywhere in the cache, requiring every entry to be searched (in parallel, via a comparator per entry) on every access; practical only for caches with few blocks because of the hardware cost of the comparators, though Content Addressable Memory (CAM) — a circuit combining storage and comparison in one device — makes much higher associativity affordable.
- [[Direct-Mapped Cache]] — the opposite limiting case, a "one-way" set-associative cache.

# Properties
- Combines direct-mapped and fully associative placement: a block is directly mapped into a set, then searched associatively within that set, so it sits on a continuum between the two extremes as $n$ varies.
- Increasing associativity generally decreases the miss rate but can increase the hit time, since more tags must be compared (and, for hardware built from SRAM and comparators, an $n$-to-1 multiplexor is needed to select the matching way).
- Requires a block replacement policy — most commonly [[Least Recently Used]] — to choose which of the $n$ ways to evict on a miss.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=426&annotation=R69FECF7)
