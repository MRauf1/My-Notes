---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Treap[^1]
> A [[Binary Search Tree]] in which every node $u$, besides its data value $u.x$, also stores a unique numerical priority $u.p$ assigned at random, and which additionally obeys the **heap property**: for every node $u$ other than the root, $u.\text{parent}.p < u.p$ — every node's priority is smaller than that of its two children.

Because priorities are unique, the heap and binary search tree properties together completely determine the shape of a Treap once each node's key and priority are fixed: the heap property forces the minimum-priority node to be the root $r$, and the binary search tree property then forces every key smaller than $r.x$ into the subtree rooted at $r.\text{left}$ and every key larger than $r.x$ into the subtree rooted at $r.\text{right}$, recursively.[^2] Equivalently, since priorities are unique and random, a Treap can be viewed as a [[Binary Search Tree]] whose nodes were added in increasing order of priority[^3] — i.e. inserted according to a random permutation of the priorities. This makes the shape of a Treap identical in distribution to that of a [[Random Binary Search Tree]]: replacing each key by its rank recovers exactly the setting of Lemma 7.1.[^4]

> [!abstract] Lemma 7.2[^5]
> In a Treap storing a set $S$ of $n$ keys:
> 1. For any $x \in S$, the expected length of the search path for $x$ is $H_{r(x)+1} + H_{n-r(x)} - O(1)$.
> 2. For any $x \notin S$, the expected length of the search path for $x$ is $H_{r(x)} + H_{n-r(x)}$.
>
> Here $r(x)$ denotes the rank of $x$ in the set $S \cup \{x\}$.

# Operations
- **`find(x)`**: the ordinary [[Binary Search Tree]] search, made efficient by Lemma 7.2.
- **`add(x)`**: create a new leaf node $u$ with $u.x \leftarrow x$ and a freshly chosen random priority $u.p$, and insert it with the usual BinarySearchTree `add(x)` algorithm. This satisfies the binary search tree property but may violate the heap property; while $u.\text{parent}.p > u.p$, perform a [[Tree Rotation]] at $w = u.\text{parent}$ so that $u$ becomes $w$'s parent, repeating until $u$ is the root or the heap property holds.[^6]
- **`remove(x)`**: locate the node $u$ storing $x$, then repeatedly [[Tree Rotation|rotate]] at $u$ to walk it downward until it becomes a leaf, then splice it out. At each step the direction is chosen by the first applicable rule: (1) if both children are nil, $u$ is already a leaf; (2) if only one child is nil, rotate toward the non-nil side; (3) otherwise rotate so that the child with the smaller priority replaces $u$. These rules keep the Treap connected and restore the heap property.[^7]

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(\log n)$ expected | $O(1)$ |
| `add(x)` | $O(\log n)$ expected | $O(1)$ |
| `remove(x)` | $O(\log n)$ expected | $O(1)$ |

The cost of `add(x)` is the length of the search path for $x$ (at most $2\ln n + O(1)$ expected, by Lemma 7.2) plus the number of rotations needed to restore the heap property; each rotation decreases $u$'s depth by one and stops once $u$ reaches the root, so the expected rotation count cannot exceed the expected search-path length — giving $O(\log n)$ expected total.[^8] The `remove(x)` operation exactly reverses `add(x)`: reinserting $x$ with the same priority would perform the same rotations in reverse and restore the prior Treap state, so `remove(x)` on a Treap of size $n$ costs the same, in expectation, as `add(x)` on a Treap of size $n-1$ — also $O(\log n)$ expected.[^9]

> [!abstract] Theorem 7.2[^10]
> A Treap implements the SSet interface. A Treap supports the operations `add(x)`, `remove(x)`, and `find(x)` in $O(\log n)$ expected time per operation.

# Space Usage
$O(n)$ words for $n$ elements: one data value, one priority, and up to three neighbour references per node.

# Properties
- [[Binary Search Tree]]
- [[Random Binary Search Tree]]
- [[Tree Rotation]]
- [[Total Order]]
- Unlike a [[Scapegoat Tree]], which restores balance amortized via occasional [[Partial Rebuilding|partial rebuilds]], a Treap restores balance on every `add(x)`/`remove(x)` via local rotations.

[^1]: [Morin, p. 151](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 151](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 152](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 152](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 152](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 155](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 157](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 155](zotero://select/library/items/HYS8NDAB)
[^9]: [Morin, p. 158](zotero://select/library/items/HYS8NDAB)
[^10]: [Morin, p. 158](zotero://select/library/items/HYS8NDAB)
