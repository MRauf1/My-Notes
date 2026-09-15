---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Complete Binary Tree[^1]
> A [[Binary Tree]] in which every level except possibly the last contains the maximum possible number of nodes, with the last level filled from left to right.

This is the sense of "complete" used throughout algorithms texts (including for a [[Binary Heap]]), and is distinct from the same-titled [[Complete Binary Tree]] elsewhere in this vault, which instead requires every leaf to be at the same height — the property most algorithms texts call a *perfect* binary tree.

# Properties
- Height is $O(\log n)$ for $n$ nodes, since only the last level can be partially filled — every other level is as full as possible.
- Can be represented implicitly as an array via [[Eytzinger's Method]], with no explicit child/parent references.

[^1]: [Morin, p. 207](zotero://select/library/items/HYS8NDAB)
