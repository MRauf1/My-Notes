---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Deque (ArrayList)
> An implementation of the [[Deque]] interface using a fixed-size [[Array]] treated as a circular buffer, indexed with [[Modular Arithmetic|modular arithmetic]] so that indices wrap around to the beginning of the array once they exceed its length.[^1]

When the underlying array fills up, it is reallocated to a larger block using the same resizing strategy as an [[ArrayList]]; consequently, a Deque (ArrayList) can waste up to $O(n)$ space at any given moment, just like an [[ArrayList]].

## Alternative Implementation
An alternative implementation avoids modular arithmetic entirely: elements are kept in order in one consecutive block of an array, and a `rebuild()` operation (which reallocates and re-centers the elements) is triggered only when the data overruns the beginning or the end of the array.[^2] This achieves the same amortized $O(1)$ time per operation at either end as the modular/circular-array approach, since `rebuild()` costs $O(n)$ but can be charged to the $\Theta(n)$ operations performed since the last rebuild.

The two approaches are asymptotically identical, so the choice comes down to constant factors: the modular approach requires a `mod` (or, when the capacity is a power of two, a cheap bitmask) on every access, while the rebuild-based approach avoids that per-operation cost entirely but pays for periodic re-centering. In practice, the circular-array approach is more common — e.g., Java's `java.util.ArrayDeque` uses a circular array sized to a power of two specifically so that the modular index can be computed with a bitmask instead of true division, eliminating the modular approach's main disadvantage.

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| [[Binary Search\|Search (Sorted)]] | $O(\log n)$ | $O(1)$ |
| Add (Beginning) | $O(1)^*$ | $O(1)$ |
| Add (End) | $O(1)^*$ | $O(1)$ |
| Insert (Middle) | $O(n)$ | $O(1)$ |
| Remove (Beginning) | $O(1)$ | $O(1)$ |
| Remove (End) | $O(1)$ | $O(1)$ |
| Remove (Middle) | $O(n)$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^\dagger$ | Varies$^\dagger$ |

$^*$Amortized, since the underlying array must occasionally reallocate to a larger block once it is full.
$^\dagger$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$n + O(n)$ words, the same as an [[ArrayList]].

# Properties
- [[Linear Data Structure]]
- [[Contiguous Data Structure]]

[^1]: [Morin, p. 42](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 58](zotero://select/library/items/HYS8NDAB)
