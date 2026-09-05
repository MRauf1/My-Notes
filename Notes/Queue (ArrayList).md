---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Queue (ArrayList)
> An implementation of the [[Queue]] interface using a fixed-size [[Array]] treated as a circular buffer: the array is indexed using [[Modular Arithmetic|modular arithmetic]] ($i \bmod \text{length}(a)$), so that indices "wrap around" to the beginning of the array once they exceed its length, simulating an infinite array with a finite one.[^1]

When the underlying array fills up, it is reallocated to a larger block using the same resizing strategy as an [[ArrayList]]; consequently, a Queue (ArrayList) can waste up to $O(n)$ space at any given moment, just like an [[ArrayList]].

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Front) | $O(1)$ | $O(1)$ |
| Add (End) / Enqueue | $O(1)^*$ | $O(1)$ |
| Remove (Beginning) / Dequeue | $O(1)$ | $O(1)$ |
| Add (Beginning / Middle) | N/A$^\dagger$ | N/A |
| Remove (Middle / End) | N/A$^\dagger$ | N/A |

$^*$Amortized, since the underlying array must occasionally reallocate to a larger block once it is full.
$^\dagger$A Queue's FIFO discipline only exposes insertion at the end and removal at the beginning.

# Space Usage
$n + O(n)$ words, the same as an [[ArrayList]].

# Properties
- [[Linear Data Structure]]
- [[Contiguous Data Structure]]

[^1]: [Morin, p. 38](zotero://select/library/items/HYS8NDAB)
