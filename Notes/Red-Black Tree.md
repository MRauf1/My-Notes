---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Red-Black Tree[^1]
> A [[Binary Search Tree]] in which every node $u$ carries a colour, red ($0$) or black ($1$), obeying:
> - **Property 9.3 (black-height)**: every root-to-leaf path passes through the same number of black nodes.
> - **Property 9.4 (no-red-edge)**: no two red nodes are adjacent — for any node $u$ other than the root, $u.\text{colour} + u.\text{parent}.\text{colour} \geq 1$.

The root can always be coloured black without violating either property, so it is taken to always be black; treating every [[External Node|external node]] (nil) as black as well means every real node has exactly two children, each with a well-defined colour.[^2] Red-black trees are one of the most widely used data structures in practice — e.g. as the primary sorted-set/map implementation in the Java Collections Framework, several C++ Standard Template Library implementations, and the Linux kernel — because, compared to a [[Skiplist]], [[Treap]], or [[Scapegoat Tree]], they guarantee $O(\log n)$ *worst-case* time for `add(x)`/`remove(x)` (rather than only expected or amortized time) while also performing only $O(1)$ *amortized* rotations per update.[^3]

## Correspondence with the 2-4 Tree
These properties seem arbitrary until connected to the [[2-4 Tree]]: removing every red node $u$ from a red-black tree $T$ and connecting $u$'s two children directly to $u$'s (black) parent leaves a tree $T'$ with only black nodes.[^4] Every internal node of $T'$ ends up with two, three, or four children, according to whether it started with two black children, one red and one black child, or two red children, respectively — and the black-height property guarantees every root-to-leaf path in $T'$ has equal length. So $T'$ is exactly a 2-4 tree: a red-black tree is precisely an efficient binary simulation of a 2-4 tree.[^5]

> [!abstract] Lemma 9.2[^6]
> The height of a red-black tree with $n$ nodes is at most $2\log n$.

This follows because the corresponding 2-4 tree $T'$ has $n+1$ leaves (the $n+1$ external nodes of $T$) and so height at most $\log(n+1)$ (Lemma 9.1); each root-to-external-node path in $T$ has at most $\log(n+1)$ black nodes and, since no two red nodes are adjacent, at most $\log(n+1) - 1$ red nodes, giving a longest root-to-node path of at most $2\log(n+1) - 2 \leq 2\log n$.

# Operations
- **`find(x)`**: the standard [[Binary Search Tree]] search; $O(\log n)$ by Lemma 9.2.
- **`add(x)`**: add $x$ as a new leaf using the usual BinarySearchTree `add(x)`, then simulate the 2-4 tree's node **split**: a 2-4 node with five children corresponds to a black node with two red children, one of which itself has a red child; this is "split" by recolouring that black node red and its two (formerly red) children black.[^7]
- **`remove(x)`**: remove $x$ with the usual BinarySearchTree `remove(x)`, then simulate the 2-4 tree's **merge** (the inverse of a split — colour two black siblings red and their red parent black) and, where needed, **borrow a child from a sibling**, the most complex of the procedures, requiring both [[Tree Rotation|rotations]] and recolouring.[^8]

> [!abstract] Theorem 9.1[^9]
> A RedBlackTree implements the same interface as a [[Binary Search Tree]] and supports `add(x)`, `remove(x)`, and `find(x)` in $O(\log n)$ worst-case time per operation.

# Space Usage
$O(n)$ words for $n$ elements: one data value, up to three neighbour references, and one bit of colour per node.

# Properties
- [[Binary Search Tree]]
- [[2-4 Tree]]
- [[Tree Rotation]]
- [[External Node]]
- Guarantees strictly stronger bounds than [[Treap]] and [[Skiplist]] (expected time only) and [[Scapegoat Tree]] (amortized time only) for `add(x)`/`remove(x)`.
- [[AVL Tree]] is an older, related height-balanced binary search tree with even smaller worst-case height, at the cost of potentially more rotations per `remove(x)`.
- Restricted to fixed-width integer (or integer-encodable) keys, a [[Y-Fast Trie]] can beat a Red-Black Tree's $O(\log n)$ with $O(\log w)$ expected time, where $w$ is the key width.

[^1]: [Morin, p. 182](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 182](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 177](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 183](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 184](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 184](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 184](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 184](zotero://select/library/items/HYS8NDAB)
[^9]: [Morin, p. 196](zotero://select/library/items/HYS8NDAB)
