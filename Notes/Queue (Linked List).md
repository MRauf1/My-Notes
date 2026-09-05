---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Queue (Linked List)
> An implementation of the [[Queue]] interface as a [[Singly Linked List]], adding new elements at the tail and removing them from the head.[^1]

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Front) | $O(1)$ | $O(1)$ |
| Add (End) / Enqueue | $O(1)$ | $O(1)$ |
| Remove (Beginning) / Dequeue | $O(1)$ | $O(1)$ |
| Add (Beginning / Middle) | N/A$^\dagger$ | N/A |
| Remove (Middle / End) | N/A$^\dagger$ | N/A |

$^\dagger$A Queue's FIFO discipline only exposes insertion at the end and removal at the beginning.

# Space Usage
$2n + O(1)$ words, the same as a [[Singly Linked List]] (one data field and one next-pointer per node).

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 63](zotero://select/library/items/HYS8NDAB)
