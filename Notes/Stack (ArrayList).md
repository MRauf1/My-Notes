---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Stack (ArrayList)
> An implementation of the [[Stack]] interface as a thin wrapper around an [[ArrayList]] that restricts access to a single end: pushing and popping both operate on the same end (the "top") of the underlying array.

Since it is backed by an [[ArrayList]], a Stack (ArrayList) inherits the same worst-case $O(n)$ wasted space as an [[ArrayList]], caused by doubling/halving the underlying array.

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Top / Peek) | $O(1)$ | $O(1)$ |
| Push / Add (End) | $O(1)^*$ | $O(1)$ |
| Pop / Remove (End) | $O(1)$ | $O(1)$ |
| Add (Beginning / Middle) | N/A$^\dagger$ | N/A |
| Remove (Beginning / Middle) | N/A$^\dagger$ | N/A |

$^*$Amortized, since the underlying array must occasionally reallocate to a larger block once it is full.
$^\dagger$A Stack's LIFO discipline only exposes insertion and removal at a single end; arbitrary-position access is not part of the interface.

# Space Usage
$n + O(n)$ words, the same as an [[ArrayList]].

# Properties
- [[Linear Data Structure]]
- [[Contiguous Data Structure]]

[^1]: [Morin](zotero://select/library/items/HYS8NDAB)
