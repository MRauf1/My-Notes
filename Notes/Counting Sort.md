---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Counting Sort[^1]
> A non-comparison-based [[Sorting Algorithm]] for an array $a$ of $n$ integers each in $\{0, \dots, k-1\}$: for each $i \in \{0, \dots, k-1\}$, count the occurrences of $i$ in $a$ into an auxiliary array $c[i]$, then write out the sorted output $b$ as $c[0]$ copies of $0$, followed by $c[1]$ copies of $1$, and so on up to $k-1$.[^2]

It sorts non-comparatively by using elements of $a$ directly as array indices (`c[a[i]] = ...`) — a constant-time statement with $k$ possible outcomes that cannot be modelled as a single binary comparison, which is exactly what lets it beat the $\Omega(n \log n)$ lower bound that applies to any [[Comparison-Based Sorting Algorithm]].[^3]

# Operations
> [!abstract] Theorem 11.7[^4]
> `counting_sort(a, k)` sorts an array of $n$ integers in $\{0, \dots, k-1\}$ in $O(n+k)$ time.

| Property | Value |
| --- | --- |
| Time (worst-case) | $O(n+k)$ |
| Space (auxiliary) | $O(n+k)$ |
| In-place | No |
| [[Stable Sorting Algorithm\|Stable]] | Yes |

Counting sort is stable: equal elements retain their relative order in the output, since $c[i]$'s occurrences of value $i$ are written out in the same order they were counted.[^5] With straightforward modification, it sorts integers in any interval $\{a, \dots, b\}$ in $O(n + b - a)$ time, and — since IEEE 754 floating-point numbers compare correctly as signed-magnitude integers — it can sort floating-point numbers this way too.[^6]

# Properties
- [[Comparison-Based Sorting Algorithm]]
- [[Stable Sorting Algorithm]]
- Used as the per-digit subroutine of [[Radix Sort]].

[^1]: [Morin, p. 231](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 231](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 231](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 233](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 233](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 236](zotero://select/library/items/HYS8NDAB)
