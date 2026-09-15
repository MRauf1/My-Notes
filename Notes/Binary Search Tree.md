---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Binary Search Tree
> A [[Binary Tree]] in which every vertex $u$ also stores a data value $u.x$ drawn from some [[Total Order]], obeying the binary search tree property: every value stored in the subtree rooted at $u.\text{left}$ is less than $u.x$, and every value stored in the subtree rooted at $u.\text{right}$ is greater than $u.x$.[^1]

This property lets a value $x$ be located quickly: starting at the root $r$ and examining a vertex $u$, if $x < u.x$ the search proceeds to $u.\text{left}$; if $x > u.x$, to $u.\text{right}$; if $x = u.x$, $u$ is the answer. The search terminates either by finding $x$ or by reaching nil, in which case $x$ is absent.[^2] This is the same less-than/greater-than/found trichotomy that drives [[Binary Search]] over a sorted array, only walking down a tree instead of repeatedly halving an index range.

# Operations
- **`find(x)`**: follow the search procedure above; costs time proportional to the depth of the vertex where the search ends.
- **`add(x)`**: search for $x$ first — if found, there is nothing to do; otherwise store $x$ as a new leaf child of the last vertex, $p$, encountered during the search, as $p$'s left or right child depending on how $x$ compares to $p.x$.[^3]
- **`remove(x)`**: locate the vertex $u$ storing $x$.
	- If $u$ is a leaf, simply detach it from its parent.
	- If $u$ has only one child, splice $u$ out by having $u.\text{parent}$ adopt that child directly.[^4]
	- If $u$ has two children, find the vertex $w$ holding the smallest value greater than $u.x$ — i.e. the smallest value in the subtree rooted at $u.\text{right}$, which is guaranteed to have no left child — copy $w.x$ into $u.x$, then remove $w$ (which now falls into one of the two simpler cases above).[^5]

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(h)$, $h$ = height of the tree | $O(1)$ |
| `add(x)` | $O(h)$ | $O(1)$ |
| `remove(x)` | $O(h)$ | $O(1)$ |

Because a BinarySearchTree is not kept balanced, its height $h$ — and so the cost of every operation — can degrade to $O(n)$: repeatedly adding values in sorted order, for instance, produces a degenerate tree that is just a chain of $n$ vertices, all but the last having exactly one child.[^6] Achieving $O(\log n)$ time regardless of insertion order requires actively rebalancing the tree, e.g. via randomization (as in a [[Treap]] or a [[Skiplist]]), amortized [[Partial Rebuilding|partial rebuilding]] (as in a [[Scapegoat Tree]]), by simulating a non-binary tree whose vertices can have up to four children (as in a [[Red-Black Tree]], which simulates a [[2-4 Tree]]), or by enforcing a strict height-balance condition at every node (as in an [[AVL Tree]]).[^6]

# Space Usage
$O(n)$ words for $n$ elements: one data value and up to three neighbour references (`left`, `right`, `parent`) per vertex.

# Properties
- [[Binary Tree]]
- [[Total Order]]
- Contrast with a [[Heap]], Morin's "disorganized pile": a heap only orders each node relative to its parent, whereas a BinarySearchTree fully orders left and right subtrees relative to every node.
- A [[B-Tree]] generalizes this same ordered interface to nodes with many children, trading tree height for larger nodes that better exploit block-based transfer in the [[External Memory Model]].

[^1]: [Morin, p. 133](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 134](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 135](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 137](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 138](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 140](zotero://select/library/items/HYS8NDAB)
