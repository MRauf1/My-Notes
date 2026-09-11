---
tags:
  - computer_science
  - theoretical_computer_science
---

# Definition
> [!info] External Node[^1]
> A placeholder that a [[Binary Tree]] is conceptually augmented with wherever a real vertex is missing a child: any vertex without a left child is given an external node as its left child, and likewise for a missing right child.

# Properties
- A [[Binary Tree]] with $n \geq 1$ real (non-external) vertices has exactly $n+1$ external nodes; this can be proven by induction on $n$.[^1]
- A [[Leaf Vertex|leaf]] — a real vertex with no children — has exactly two external node children.

[^1]: [Morin, p. 129](zotero://select/library/items/HYS8NDAB)
