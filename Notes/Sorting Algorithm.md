---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition

[[Algorithm]] for sorting some list.[^1]

# Types
## [[Comparison-Based Sorting Algorithm]]
- [[Merge Sort]]
- [[Quicksort]]
- [[Heapsort]]

## Non-Comparison-Based
- [[Counting Sort]]
- [[Radix Sort]]

# Comparison
| Algorithm | Comparisons | Space (auxiliary) | In-Place | [[Stable Sorting Algorithm\|Stable]] |
| --- | --- | --- | --- | --- |
| [[Merge Sort]] | $n\log n$, worst-case | $O(n)$ | No | Yes |
| [[Quicksort]] | $\approx 1.38n\log n + O(n)$, expected | $O(\log n)$ expected | Yes | No |
| [[Heapsort]] | $2n\log n + O(n)$, worst-case | $O(1)$ | Yes | No |
| [[Counting Sort]] | — (non-comparison) | $O(n+k)$ | No | Yes |
| [[Radix Sort]] | — (non-comparison) | $O(n+2^d)$ | No | Yes |
[^2]

No single one of [[Merge Sort]], [[Quicksort]], and [[Heapsort]] dominates the others: merge sort does the fewest comparisons and needs no randomization, but is not in-place; quicksort is in-place and a close second on comparisons, but its guarantee is only in expectation; heapsort does the most comparisons, but is both in-place and fully deterministic.[^3] In practice, **quicksort is the most commonly used** of the three for arrays — its in-place partitioning gives excellent cache behaviour and its expected running time is rarely a practical concern, which is why it (or a hybrid built around it, e.g. introsort) underlies most general-purpose library sort routines. The one setting where **merge sort is the clear winner** is sorting a linked list, where its auxiliary array becomes unnecessary altogether, since two sorted linked lists merge by pure pointer manipulation.[^4] When the input is known to be small integers (or floats) drawn from a limited range, [[Counting Sort]] or [[Radix Sort]] beats all three comparison-based algorithms asymptotically, running in $O(cn)$ time for $n$ values in $\{0, \dots, n^c-1\}$.[^5]

# Properties
- [[Comparison-Based Sorting Algorithm]]
- [[Stable Sorting Algorithm]]

[^1]: [Introduction to Algorithms](zotero://open-pdf/library/items/X422WTMW?page=28)
[^2]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 218](zotero://select/library/items/HYS8NDAB)