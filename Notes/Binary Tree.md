---
tags:
  - computer_science
  - theoretical_computer_science
  - data_structures_and_algorithms
---

# Definition

> [!info] Definition 1 (Binary [[Tree]])[^1]
> [[Tree]] where every [[Vertex]] can have at most 2 [[Child Vertex]].

Equivalently, a binary tree is a connected, undirected, finite graph with no cycles and no vertex of degree greater than three.[^2] The "three" accounts for a non-root vertex's edge to its [[Parent Vertex]] in addition to its at most two children, while the [[Root Vertex]] itself has degree at most two (no parent). For most computer science applications the tree is rooted *and* ordered, so a distinction is drawn between a vertex's left child and right child.[^2] The simplest representation of a vertex $u$ explicitly stores its (at most three) neighbours — `u.left`, `u.right`, and `u.parent` — set to nil when absent, so both a missing child and the parent of the root correspond to nil; the tree itself is then represented by a single reference to its root.[^3] If the parent field is omitted from this representation, non-recursive traversal is still possible, but it must use a list or [[Stack]] to track the path back to the root.[^4]

# Types
- [[Full Binary Tree]]
- [[Complete Binary Tree]]
- [[Full and Complete Binary Tree]]
- [[Binary Search Tree]]

# Properties
- Augmenting the tree with an [[External Node]] in place of every missing child gives a binary tree with $n \geq 1$ real vertices exactly $n+1$ external nodes.[^5]
- Traversed via [[Breadth-First Search|breadth-first]] or [[Depth-First Search|depth-first]] traversal.

[^1]: [Building Blocks for Theoretical Computer Science](zotero://open-pdf/library/items/5IGT8C55?page=165)
[^2]: [Morin, p. 127](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 129](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 132](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 129](zotero://select/library/items/HYS8NDAB)