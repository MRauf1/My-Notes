---
tags:
  - computer_science
  - theoretical_computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] 2-4 Tree[^1]
> A rooted tree obeying:
> - **Property 9.1 (height)**: all leaves have the same depth.
> - **Property 9.2 (degree)**: every internal node has 2, 3, or 4 children.

A 2-4 tree is **not** a [[Binary Tree]] or [[Binary Search Tree]]: its internal nodes may have up to four children rather than at most two, making it an [[m-ary Tree|m-ary tree]] with $m = 4$, further constrained to a minimum degree of 2 and perfectly equal leaf depth. Its role in this chapter is purely as a conceptual scaffold: the [[Red-Black Tree]] is a genuine binary search tree that simulates a 2-4 tree's shape via node colouring, inheriting its logarithmic height guarantee while remaining binary.

> [!abstract] Lemma 9.1[^2]
> A 2-4 tree with $n$ leaves has height at most $\log n$.

# Operations
- **Add a leaf**: add the new leaf $u$ as a child of some node $w$ on the second-last level. This preserves Property 9.1 but may violate Property 9.2 if $w$ already had four children (leaving it with five); if so, **split** $w$ into two nodes with two and three children respectively, and recursively add the new node as a child of $w$'s parent, propagating upward. If this reaches the root, split it too and create a new root with the two split halves as children — increasing every leaf's depth by one and so preserving Property 9.1.[^3] Since height is never more than $\log n$, this takes at most $O(\log n)$ steps.[^4]
- **Remove a leaf**: remove the leaf $u$ from its parent $w$. If this leaves $w$ with only one child, violating Property 9.2, look at $w$'s sibling $w'$ (guaranteed to exist): if $w'$ has three or four children, transfer one of them to $w$; otherwise, **merge** $w$ and $w'$ into a single three-child node and recursively remove $w'$ from its parent, propagating upward.[^5] This ends once some node (or its sibling) has more than two children, or at the root, where a root left with a single child is deleted and replaced by that child — decreasing every leaf's depth by one and so preserving Property 9.1.[^6] This also takes at most $O(\log n)$ steps.[^7]

# Properties
- [[m-ary Tree]]
- [[Red-Black Tree]]
- Generalized by [[B-Tree]] to allow $B$-to-$2B$ children per node for any $B \geq 2$; a 2-4 tree is exactly the $B=2$ case.

[^1]: [Morin, p. 178](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 178](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 179](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 179](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 179](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 179](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 182](zotero://select/library/items/HYS8NDAB)
