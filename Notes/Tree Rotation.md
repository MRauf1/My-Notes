---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Tree Rotation
> A local modification of a [[Binary Search Tree]] that takes a parent $u$ of a node $w$ and makes $w$ the parent of $u$ instead, while preserving the binary search tree property.[^1]

A rotation is a **left rotation** or a **right rotation** depending on whether $w$ was $u$'s right or left child, respectively, before the rotation.[^1]

# Properties
- The depth of $w$ decreases by one while the depth of $u$ increases by one; every other node's depth (and every node's relative order) is unchanged.[^2]
- Used by a [[Treap]] to restore the heap property after `add(x)`/`remove(x)` without violating the binary search tree property.

[^1]: [Morin, p. 153](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 154](zotero://select/library/items/HYS8NDAB)
