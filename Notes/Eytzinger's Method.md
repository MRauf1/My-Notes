---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Eytzinger's Method[^1]
> A technique, over four hundred years old, for representing a [[Complete Binary Tree (Data Structures and Algorithms)|complete binary tree]] implicitly as an array: the tree's nodes are laid out in [[Breadth-First Search|breadth-first]] order, so the root is stored at index $0$, the root's left child at index $1$, its right child at index $2$, and so on.

Applied to a sufficiently large tree, this layout yields simple index arithmetic: for a node at index $i$,[^2][^3] $$\text{left}(i) = 2i+1, \qquad \text{right}(i) = 2i+2, \qquad \text{parent}(i) = \left\lfloor \frac{i-1}{2} \right\rfloor.$$

# Properties
- Used by [[Binary Heap]] to represent its underlying tree without storing explicit child or parent references.

[^1]: [Morin, p. 203](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 203](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 204](zotero://select/library/items/HYS8NDAB)
