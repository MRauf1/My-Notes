---
tags:
  - computer_science
  - computer_architecture
---

# Definition
> [!info] Cache Blocking (Loop Tiling)[^1]
> A program transformation that restructures a computation over an array — such as matrix multiplication — to operate on submatrices (blocks) small enough to fit in the cache, rather than sweeping over entire rows or columns, so as to maximize the number of accesses made to data while it remains in the cache before being replaced.

# Properties
- Improves [[Principle of Locality|temporal locality]] directly, reducing cache misses without changing the algorithm's asymptotic operation count.
- Distinct from, and complementary to, storing arrays so that accesses are sequential in memory, which instead exploits spatial locality; standard algorithmic analysis often ignores both effects even though memory-hierarchy behavior is critical to real performance (e.g. quicksort incurring far fewer misses per element than alternative sorts with the same asymptotic complexity).
- Choosing a small enough block size can additionally aid register allocation, by minimizing the loads and stores a [[Compiler]] must issue to move data between memory and [[Register (Computer Architecture)|registers]].
- Pitfall: ignoring memory-system behavior when writing programs, or when a compiler generates code, can leave large, easily reclaimed performance on the table relative to a blocked implementation.

[^1]: [Computer Organization and Design: The Hardware/Software Interface](zotero://open-pdf/library/items/YWPB5EDC?page=436&annotation=WY9868L8)
