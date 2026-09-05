---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Deque
> A double-ended [[Data Structure]] that implements the full list interface while supporting efficient addition and removal at both the beginning and the end.

A Deque can be implemented as a circular-buffer [[Array]] (see [[Deque (ArrayList)]]) or as a [[Doubly Linked List]] (see [[Deque (Linked List)]]).

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

$^*$Amortized in the array-based implementation, worst-case in the linked-list-based implementation; see [[Deque (ArrayList)]] and [[Deque (Linked List)]].
$^\dagger$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$\Theta(n)$, with the exact constant factor depending on the implementation; see [[Deque (ArrayList)]] and [[Deque (Linked List)]].

# Preferred Implementation
As with [[Stack]] and [[Queue]], the array-based implementation is generally preferred in practice for its better cache locality and lower per-element memory overhead — e.g. Java's `ArrayDeque` (array-based) is preferred over `LinkedList` for deque usage.

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 42](zotero://select/library/items/HYS8NDAB)
