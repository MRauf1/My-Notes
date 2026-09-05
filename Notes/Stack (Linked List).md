---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Stack (Linked List)
> An implementation of the [[Stack]] interface as a [[Singly Linked List]], where both pushing and popping operate on the head of the list.[^1]

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Top / Peek) | $O(1)$ | $O(1)$ |
| Push / Add (Beginning) | $O(1)$ | $O(1)$ |
| Pop / Remove (Beginning) | $O(1)$ | $O(1)$ |
| Add (Middle / End) | N/A$^\dagger$ | N/A |
| Remove (Middle / End) | N/A$^\dagger$ | N/A |

$^\dagger$A Stack's LIFO discipline only exposes insertion and removal at a single end; arbitrary-position access is not part of the interface.

# Space Usage
$2n + O(1)$ words, the same as a [[Singly Linked List]] (one data field and one next-pointer per node).

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 64](zotero://select/library/items/HYS8NDAB)
