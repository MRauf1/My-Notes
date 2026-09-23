---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Merge Sort[^1]
> A classic recursive divide-and-conquer [[Comparison-Based Sorting Algorithm]]: an array of length at most $1$ is already sorted; otherwise, split the array into two halves, recursively sort each half, and merge the two now-sorted halves back into one sorted array.

Merging two sorted arrays $a_0$ and $a_1$ into $a$ is done by repeatedly taking the smaller of the next unconsumed element of $a_0$ and $a_1$ (or, once one is exhausted, simply draining the other); this performs at most $n-1$ comparisons before one side runs out.[^2]

# Operations
> [!abstract] Theorem 11.1[^3]
> The `merge_sort(a)` algorithm runs in $O(n \log n)$ time and performs at most $n \log n$ comparisons.

| Property | Value |
| --- | --- |
| Time (worst-case) | $O(n \log n)$, at most $n \log n$ comparisons |
| Space (auxiliary) | $O(n)$ |
| In-place | No |
| [[Stable Sorting Algorithm\|Stable]] | Yes |

Unlike [[Quicksort]] and [[Heapsort]], merge sort needs an auxiliary array of size $O(n)$ during merging — it is not in-place, which can matter when memory is limited or allocation is expensive.[^4] It does, however, do the fewest comparisons of the three comparison-based algorithms and does not rely on randomization.[^4] It is the clear winner when sorting a linked list: two sorted linked lists can be merged into one by pure pointer manipulation, with no auxiliary array needed at all.[^5]

# Properties
- [[Comparison-Based Sorting Algorithm]]
- [[Divide and Conquer]]
- [[Stable Sorting Algorithm]]

[^1]: [Morin, p. 218](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 219](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 221](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
