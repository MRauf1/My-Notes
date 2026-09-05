---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] RootishArrayList
> A [[Data Structure]] that implements the full list interface while wasting only $O(\sqrt{n})$ space when storing $n$ elements, instead of the $O(n)$ an [[ArrayList]] can waste.

A RootishArrayList stores its elements across $r$ arrays, called blocks, numbered $0, 1, \dots, r-1$, where block $b$ holds exactly $b+1$ elements.[^1] Since all $r$ blocks together hold $1 + 2 + \cdots + r = r(r+1)/2$ elements, storing $n$ elements requires $r = \Theta(\sqrt{n})$ blocks. Growing or shrinking the structure (via `grow()`/`shrink()`) only allocates or frees a single new block of size $r$ — no existing data is copied — so this cost, amortized over the operations that must occur before the next `grow()`/`shrink()`, is $O(1)$ per operation.[^2]

This $O(\sqrt{n})$ bound is asymptotically optimal: for any data structure that starts empty and supports adding elements one at a time by allocating new memory blocks, some moment during the addition of $n$ elements must waste at least $\Omega(\sqrt{n})$ space.[^3] If, at the end, the elements are held in $r \geq \sqrt{n}$ blocks, the $r$ pointers/references needed to track those blocks are themselves $\Omega(\sqrt{n})$ words of overhead. If instead $r < \sqrt{n}$, some block must (by the pigeonhole principle) hold more than $n/r > \sqrt{n}$ elements; since each block's capacity is fixed when it is allocated, that block must have had capacity greater than $\sqrt{n}$ from the moment of its creation, when it held zero elements — wasting more than $\sqrt{n}$ space at that instant.

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (get/set) | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| [[Binary Search\|Search (Sorted)]] | $O(\log n)$ | $O(1)$ |
| Add (End) | $O(1)^*$ | $O(1)$ |
| Insert (Beginning) | $O(n)$ | $O(1)$ |
| Insert (Middle) | $O(n)$ | $O(1)$ |
| Remove (End) | $O(1)^*$ | $O(1)$ |
| Remove (Beginning) | $O(n)$ | $O(1)$ |
| Remove (Middle) | $O(n)$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^\dagger$ | Varies$^\dagger$ |

$^*$Amortized; per above, `grow()`/`shrink()` cost $O(1)$ per operation when amortized over a sequence of operations.
$^\dagger$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$n + O(\sqrt{n})$ words, compared to up to $n + O(n)$ for a standard doubling [[ArrayList]].

# Properties
- [[Linear Data Structure]]
- [[Contiguous Data Structure]]

[^1]: [Morin, p. 50](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 55](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 56](zotero://select/library/items/HYS8NDAB)
