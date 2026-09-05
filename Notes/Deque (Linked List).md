---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Deque (Linked List)
> An implementation of the [[Deque]] interface as a [[Doubly Linked List]], using its `next` and `prev` references to support insertion and removal at both ends in constant time.[^1]

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Beginning) | $O(1)$ | $O(1)$ |
| Access (End) | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| Add (Beginning) | $O(1)$ | $O(1)$ |
| Add (End) | $O(1)$ | $O(1)$ |
| Remove (Beginning) | $O(1)$ | $O(1)$ |
| Remove (End) | $O(1)$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^*$ | Varies$^*$ |

$^*$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$3n + O(1)$ words, the same as a [[Doubly Linked List]] (one data field, one next-pointer, and one prev-pointer per node).

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 64](zotero://select/library/items/HYS8NDAB)
