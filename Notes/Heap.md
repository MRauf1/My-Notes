---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Heap[^1]
> A special kind of [[Binary Tree]] that is heap-ordered: the value stored at a node is never smaller than the value stored at its parent (excepting the root). Morin describes a heap as "a disorganized pile," in contrast to a [[Binary Search Tree]], "a highly organized pile."

A heap only constrains each node relative to its immediate parent — it says nothing about how a node's left and right subtrees compare to each other — which is a much weaker structural invariant than the full binary search tree property. This weaker constraint is exactly what a [[Priority Queue]] needs: it guarantees the minimum element is always at the root, cheap to find, without requiring the rest of the elements to be kept in any particular sorted order. A heap therefore *implements* the Priority Queue interface, trading the ability to efficiently search for an arbitrary value (which a Binary Search Tree provides) for a cheaper, less constrained way to always expose the current minimum.

# Types
- [[Binary Heap]]
- [[Meldable Heap]]

# Properties
- [[Priority Queue]]
- [[Binary Search Tree]]

[^1]: [Morin, p. 203](zotero://select/library/items/HYS8NDAB)
