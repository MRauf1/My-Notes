---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Direct-Mapped Cache[^1]
> A [[Cache Memory|cache]] structure in which each memory location is mapped to exactly one location in the cache, typically by low-order address bits (the index).

# Properties
- Since each block has only one possible location, there is only one candidate to evict on a miss, and only a single tag comparator is needed to check for a hit — simplicity that comes at the cost of a higher miss rate than an equally sized associative cache; see [[Set-Associative Cache]].
- The block, tag, and valid bit for each entry (see [[Cache Memory]]) together determine the total number of bits required to build a direct-mapped cache of a given data capacity.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=407&annotation=J59786QX)
