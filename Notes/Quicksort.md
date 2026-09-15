---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Quicksort[^1]
> A divide-and-conquer [[Comparison-Based Sorting Algorithm]] that, unlike [[Merge Sort]], does all of its work *before* recursing: pick a random pivot $x$ from the array, partition the array into elements less than, equal to, and greater than $x$, then recursively sort the first and third parts.

The partitioning is done in place, without allocating extra space: the algorithm sorts only the subarray $a[i], \dots, a[i+n-1]$ by swapping elements while advancing an index $p$ from the front and $q$ from the back, maintaining $a[i] < x$ for $i \leq p$ and $a[i] > x$ for $i \geq q$, until every element has been classified.[^2]

Quicksort is closely related to the [[Random Binary Search Tree]]: if the input consists of $n$ distinct elements, the recursion tree traced out by quicksort's pivot choices *is* a random binary search tree.[^3]

# Operations
> [!abstract] Lemma 11.1[^4]
> When quicksort sorts an array containing the integers $0, \dots, n-1$, the expected number of times element $i$ is compared to a pivot is at most $H_{i+1} + H_{n-i}$.

> [!abstract] Theorem 11.2[^5]
> When quicksort sorts an array of $n$ distinct elements, the expected number of comparisons performed is at most $2n\ln n + O(n) \approx 1.38 n \log n + O(n)$.

> [!abstract] Theorem 11.3[^6]
> `quick_sort(a, c)` runs in $O(n \log n)$ expected time, performing at most $2n \ln n + O(n)$ comparisons in expectation.

| Property | Value |
| --- | --- |
| Time (expected) | $O(n \log n)$, $\approx 1.38 n\log n + O(n)$ comparisons |
| Time (worst-case) | $O(n^2)$ |
| Space (auxiliary) | $O(\log n)$ expected, for the recursion stack |
| In-place | Yes |
| [[Stable Sorting Algorithm\|Stable]] | No |

Quicksort is an in-place algorithm and a close second to [[Merge Sort]] in number of comparisons, but its randomized pivot means its running time is only guaranteed in expectation, not in the worst case.[^7]

# Properties
- [[Comparison-Based Sorting Algorithm]]
- [[Random Binary Search Tree]]
- [[Harmonic Number]]

[^1]: [Morin, p. 222](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 223](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 223](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 224](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 224](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 225](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
