---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Comparison-Based Sorting Algorithm[^1]
> A [[Sorting Algorithm]] that touches its input only through a `compare(a, b)` call — returning negative if $a < b$, positive if $a > b$, and zero if $a = b$ — and so never depends on the specific type of data being sorted.

Any deterministic comparison-based algorithm can be modelled as a rooted binary **comparison tree**: each internal node is a comparison, and each leaf is a possible sorted output, so the number of comparisons the algorithm performs on some input is the depth of the leaf that input reaches.[^2]

# Properties
> [!abstract] Theorem 11.5[^3]
> For any deterministic comparison-based sorting algorithm $A$ and any integer $n \geq 1$, there exists an input array of length $n$ such that $A$ performs at least $\log(n!) = n\log n - O(n)$ comparisons sorting it.

This extends to randomized algorithms too, by treating a randomized algorithm as a deterministic one that takes a second input — an infinite sequence of random reals used to make every random choice. Fixing that sequence turns it into an ordinary deterministic algorithm with its own comparison tree, and sorting a uniformly random permutation is then equivalent to selecting a uniformly random leaf of that tree.[^4]

> [!abstract] Theorem 11.6[^5]
> For any integer $n \geq 1$ and any (deterministic or randomized) comparison-based sorting algorithm $A$, the expected number of comparisons done by $A$ sorting a random permutation of $\{1, \dots, n\}$ is at least $\log(n!) = n\log n - O(n)$.

So $\Omega(n \log n)$ comparisons are unavoidable for *any* comparison-based algorithm, in the worst case and even in the average case — [[Merge Sort]], [[Quicksort]], and [[Heapsort]] are all asymptotically optimal in this sense.[^6] Any [[Binary Search Tree]] or [[Priority Queue]] implementation studied elsewhere in this vault can likewise be turned into an $O(n \log n)$-time sort (insert every element, then remove them in order), though the three algorithms above are typically faster in practice.[^7] Only by abandoning comparisons entirely — e.g. by using array indexing, as [[Counting Sort]] and [[Radix Sort]] do — can this lower bound be beaten.[^8]

# Types
- [[Merge Sort]]
- [[Quicksort]]
- [[Heapsort]]

[^1]: [Morin, p. 218](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 228](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 229](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 230](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 230](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 217](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 217](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 231](zotero://select/library/items/HYS8NDAB)
