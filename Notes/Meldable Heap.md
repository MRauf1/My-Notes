---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Meldable Heap[^1]
> A [[Priority Queue]] implementation whose underlying heap-ordered [[Binary Tree]] has no shape restriction — unlike a [[Binary Heap]], where the tree's shape is completely determined by $n$, a MeldableHeap's tree can be *anything*.

`add(x)` and `remove()` are both implemented in terms of a single primitive, `merge(h1, h2)`, which takes the root nodes of two heaps and returns the root of a single heap containing every element of both.[^2] Because so much is expressed through `merge`, a MeldableHeap can also support `remove(u)` (delete an arbitrary node $u$, not just the minimum) and `absorb(h)` (fold another MeldableHeap $h$'s elements into this one, emptying $h$) using only a constant number of `merge(h1, h2)` calls each.[^3]

# Analysis
> [!abstract] Lemma 10.1[^4]
> The expected length of a random walk in a binary tree with $n$ nodes — repeatedly stepping to a uniformly random child until an external node is reached — is at most $\log(n+1)$.

This follows from an information-theoretic argument: if $d_i$ is the depth of the $i$-th of the $n+1$ external nodes (see [[External Node]]), the [[Random Walk|walk]] reaches it with probability $p_i = 1/2^{d_i}$, so its expected length is $\sum_i p_i d_i = \sum_i p_i \log(1/p_i)$ — the entropy of a distribution over $n+1$ outcomes, which never exceeds $\log(n+1)$.[^5]

> [!abstract] Lemma 10.2[^6]
> If $h_1$ and $h_2$ are the roots of two heaps with $n_1$ and $n_2$ nodes respectively, the expected running time of `merge(h1, h2)` is at most $O(\log n)$, where $n = n_1 + n_2$.

Merging two heaps along a random root-to-external-node walk in each keeps every operation built from `merge` — `add(x)`, `remove()`, `remove(u)`, `absorb(h)` — to $O(\log n)$ expected time.

> [!abstract] Theorem 10.2[^7]
> A MeldableHeap implements the (priority) Queue interface. A MeldableHeap supports `add(x)` and `remove()` in $O(\log n)$ expected time per operation.

# Space Usage
$O(n)$ words for $n$ elements: one data value and a constant number of child references per node, with no restriction on shape.

# Types
- [[Fibonacci Heap]]

# Properties
- [[Heap]]
- [[Priority Queue]]
- [[Binary Heap]]
- [[Random Walk]]

[^1]: [Morin, p. 209](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 209](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 212](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 212](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 213](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 213](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 214](zotero://select/library/items/HYS8NDAB)
