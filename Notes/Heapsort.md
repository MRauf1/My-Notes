---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Heapsort[^1]
> An in-place [[Comparison-Based Sorting Algorithm]] that converts the input array into a [[Binary Heap]] and then repeatedly extracts the minimum value, using the same single array the input arrived in.

Turning an unsorted array into a heap could be done in $O(n \log n)$ time by calling `add(x)` $n$ times, but a bottom-up construction does better. Since the children of $a[i]$ live at $a[2i+1]$ and $a[2i+2]$, every element from $a[\lfloor n/2 \rfloor]$ onward has no children and is already a valid (size-$1$) sub-heap; working backwards and calling `trickle_down(i)` for each $i \in \{\lfloor n/2 \rfloor - 1, \dots, 0\}$ therefore always finds both of $a[i]$'s children already rooting valid sub-heaps, so `trickle_down(i)` correctly makes $a[i]$ the root of its own.[^2]

This bottom-up construction is more efficient than $n$ calls to `add(x)`: roughly $n/2$ elements need no work at all, $n/4$ need `trickle_down` on a sub-heap of height $1$, $n/8$ on height $2$, and so on, so the total work is $\sum_{i=1}^{\log n} O((i-1)n/2^i) \leq O(n)\sum_{i=1}^\infty i/2^i = O(n)$.[^3]

# Operations
> [!abstract] Theorem 11.4[^4]
> `heap_sort(a, c)` runs in $O(n \log n)$ time and performs at most $2n \log n + O(n)$ comparisons.

| Property | Value |
| --- | --- |
| Time (worst-case) | $O(n \log n)$, at most $2n \log n + O(n)$ comparisons |
| Space (auxiliary) | $O(1)$ |
| In-place | Yes |
| [[Stable Sorting Algorithm\|Stable]] | No |

Heapsort does the most comparisons of the three comparison-based algorithms covered here, but it is both in-place and fully deterministic — unlike [[Quicksort]], its $O(n \log n)$ bound is a worst-case guarantee, not merely an expectation.[^5]

# Properties
- [[Comparison-Based Sorting Algorithm]]
- [[Binary Heap]]

[^1]: [Morin, p. 225](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 226](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 227](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 227](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
