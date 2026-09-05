---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Contiguous Data Structure
> A [[Data Structure]] whose elements are stored in adjacent memory locations, so that the memory address of any element can be computed directly from a base address and an index, e.g. $\text{address}(i) = \text{base} + i \times \text{size}$.

Storing elements contiguously lets the address of the $i$-th element be computed in $O(1)$ time via pointer arithmetic, giving constant-time random access without following pointers. Contiguous storage also improves cache performance: since modern CPUs load memory in cache lines and prefetch sequential addresses, iterating over a contiguous block incurs far fewer cache misses than traversing structures whose elements are scattered across memory, such as pointer-linked structures.

# Examples
- [[Array]]
- [[ArrayList]]
- [[RootishArrayList]]

[^1]: [Introduction to Algorithms](zotero://select/library/items/X422WTMW)
