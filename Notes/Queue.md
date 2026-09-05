---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Queue
> A FIFO (first-in-first-out) [[Data Structure]] that removes elements in the same order they were added: elements are added at one end and removed from the other.

A Queue can be implemented as a circular-buffer [[Array]] (see [[Queue (ArrayList)]]) or as a [[Singly Linked List]] (see [[Queue (Linked List)]]).

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Front) | $O(1)$ | $O(1)$ |
| Add (End) / Enqueue | $O(1)^*$ | $O(1)$ |
| Remove (Beginning) / Dequeue | $O(1)$ | $O(1)$ |
| Add (Beginning / Middle) | N/A$^\dagger$ | N/A |
| Remove (Middle / End) | N/A$^\dagger$ | N/A |

$^*$Amortized in the array-based implementation, worst-case in the linked-list-based implementation; see [[Queue (ArrayList)]] and [[Queue (Linked List)]].
$^\dagger$A Queue's FIFO discipline only exposes insertion at the end and removal at the beginning; see [[Deque]] for a structure supporting efficient operations at both ends.

# Space Usage
$\Theta(n)$, with the exact constant factor depending on the implementation; see [[Queue (ArrayList)]] and [[Queue (Linked List)]].

# Preferred Implementation
As with [[Stack]], the array-based implementation is generally preferred in practice for its better cache locality and lower per-element memory overhead — e.g. Java's documentation recommends `ArrayDeque` over `LinkedList` for queue usage.

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 38](zotero://select/library/items/HYS8NDAB)
