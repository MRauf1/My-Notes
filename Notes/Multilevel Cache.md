---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Multilevel Cache[^1]
> A [[Memory Hierarchy]] with several levels of [[Cache Memory|caches]] between the processor and main memory, rather than a single cache.

# Properties
- Closes the growing gap between fast processor clock rates and slower DRAM access times: a miss in the first-level cache that hits in the second-level cache incurs only the second level's access time as its miss penalty, far less than a full main-memory access, while a miss in both levels still requires the larger main-memory miss penalty.
- The local miss rate of a level is the fraction of references to that level which miss; the global miss rate is the fraction of all references that miss at every level of the hierarchy — the two coincide for the first-level cache but diverge for lower levels, since a lower-level cache sees only the references filtered through by misses at the levels above it.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=434&annotation=4KDWZBMP)
