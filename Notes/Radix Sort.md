---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Radix Sort[^1]
> A non-comparison-based [[Sorting Algorithm]] that sorts $w$-bit integers using $w/d$ passes of [[Counting Sort]], each sorting by $d$ bits at a time: first by the least significant $d$ bits, then the next $d$ bits, and so on up to the most significant $d$ bits.[^2]

This digit-by-digit strategy is only correct because [[Counting Sort]] is stable: each pass must preserve the relative order established by every previous, less-significant pass, or the final result would not be fully sorted.[^3]

# Operations
> [!abstract] Theorem 11.8[^4]
> For any integer $d > 0$, `radix_sort(a, k)` sorts an array of $n$ $w$-bit integers in $O\!\left(\frac{w}{d}(n + 2^d)\right)$ time.

> [!abstract] Corollary 11.1[^5]
> `radix_sort(a, k)` sorts an array of $n$ integers in $\{0, \dots, n^c - 1\}$ in $O(cn)$ time.

| Property | Value |
| --- | --- |
| Time (worst-case) | $O\!\left(\frac{w}{d}(n+2^d)\right)$; $O(cn)$ for $n^c$-range integers |
| Space (auxiliary) | $O(n + 2^d)$ per pass |
| In-place | No |
| [[Stable Sorting Algorithm\|Stable]] | Yes |

By choosing $d$ so that each pass's [[Counting Sort]] range $2^d$ stays close to $n$, radix sort sorts a set of $n$ integers drawn from $\{0, \dots, n^c-1\}$ in just $O(cn)$ time — beating any [[Comparison-Based Sorting Algorithm]]'s $\Omega(n\log n)$ lower bound by using array indexing instead of comparisons.[^6] Like [[Counting Sort]], straightforward modifications extend it to any interval $\{a, \dots, b\}$ (in $O(n \log_n(b-a))$ time) and to IEEE 754 floating-point numbers.[^7]

# Properties
- [[Counting Sort]]
- [[Comparison-Based Sorting Algorithm]]
- [[Stable Sorting Algorithm]]

[^1]: [Morin, p. 233](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 233](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 234](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 234](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 235](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 218](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 236](zotero://select/library/items/HYS8NDAB)
