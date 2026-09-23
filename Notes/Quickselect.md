---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Quickselect[^1]
> An algorithm (also called *one-armed quicksort*, due to Hoare, 1961) for the **selection problem**: given an $n$-element array and an integer $k$, find the $k$-th smallest element. It chooses a pivot, partitions the array with the same partition subroutine as [[Quicksort]], and then recurses on *only one* of the two subarrays — the one containing the $k$-th smallest element.[^2]

Finding the [[Median]] is the special case $k = \lceil n/2 \rceil$.[^1]

# Types
- [[Median of Medians]] (deterministic pivot choice, worst-case $O(n)$)

# Properties
- A [[Divide and Conquer]] algorithm with a single recursive call.
- With a bad pivot, the recurrence is $T(n) = T(n-1) + O(n)$, giving $O(n^2)$ worst-case time; the quality of the pivot determines the running time.

[^1]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=53&annotation=GEBADQW3)
[^2]: [Algorithms (Erickson)](zotero://open-pdf/library/items/XT26IR4C?page=53&annotation=8ZSIBQXJ)
