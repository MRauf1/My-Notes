---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Random Binary Search Tree
> A [[Binary Search Tree]] of size $n$ obtained by taking a uniformly random [[Permutation|permutation]] $x_0, \dots, x_{n-1}$ of $0, \dots, n-1$ — one where each of the $n!$ possible orderings is equally likely, with probability $1/n!$ — and adding its elements, one by one, into an initially empty tree.[^1]

The values $0, \dots, n-1$ are only a stand-in: they could be replaced by any [[Total Order|ordered set]] of $n$ elements without changing any property of the random binary search tree, since $x \in \{0, \dots, n-1\}$ simply denotes the element of rank $x$ in that set.[^2]

This construction only produces a well-defined "random" tree when the full set of $n$ elements is fixed in advance and permuted all at once; it gives no way to keep adding elements one at a time to a tree that is already built while preserving the same randomness guarantees for future insertions, since there is no notion of a random permutation of an as-yet-unknown or still-growing set. This is precisely the limitation Morin flags next: a random binary search tree is not dynamic, since it supports no `add(x)`/`remove(x)` operations of its own — a [[Treap]] resolves this by achieving the same expected shape through random priorities assigned incrementally as elements are inserted, rather than through a single upfront permutation.[^3]

# Properties
> [!abstract] Lemma 7.1[^4]
> In a random binary search tree of size $n$:
> 1. For any $x \in \{0, \dots, n-1\}$, the expected length of the search path for $x$ is $H_{x+1} + H_{n-x} - O(1)$.
> 2. For any $x \in (-1, n) \setminus \{0, \dots, n-1\}$, the expected length of the search path for $x$ is $H_{\lceil x \rceil} + H_{n - \lceil x \rceil}$.

Both parts bound the [[Expectation|expected]] search-path length by $2\ln n + O(1)$; searching for a value present in the tree is only slightly faster than searching for one that is absent.[^5]

> [!abstract] Theorem 7.1[^6]
> A random binary search tree can be constructed in $O(n \log n)$ time. In a random binary search tree, the `find(x)` operation takes $O(\log n)$ expected time.

- [[Binary Search Tree]]
- [[Harmonic Number]]
- [[Treap]]

[^1]: [Morin, p. 146](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 146](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 151](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 147](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 148](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 151](zotero://select/library/items/HYS8NDAB)
