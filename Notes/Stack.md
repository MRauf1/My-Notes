---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Stack
> A LIFO (last-in-first-out) [[Data Structure]] that removes the most recently added element first.

A Stack restricts access to a single end (the "top"): elements are only pushed onto and popped off that end. It can be implemented as an [[ArrayList]] restricted to one end (see [[Stack (ArrayList)]]) or as a [[Singly Linked List]] restricted to its head (see [[Stack (Linked List)]]).

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Top / Peek) | $O(1)$ | $O(1)$ |
| Push (Add, End) | $O(1)^*$ | $O(1)$ |
| Pop (Remove, End) | $O(1)$ | $O(1)$ |

$^*$Amortized in the array-based implementation, worst-case in the linked-list-based implementation; see [[Stack (ArrayList)]] and [[Stack (Linked List)]] for exact complexities.

# Space Usage
$\Theta(n)$, with the exact constant factor depending on the implementation; see [[Stack (ArrayList)]] and [[Stack (Linked List)]].

# Preferred Implementation
In practice, the array-based implementation ([[Stack (ArrayList)]]) is generally preferred: it stores elements contiguously with no per-element pointer overhead, giving better cache locality than the linked-list-based implementation while matching it asymptotically. For example, Java's `java.util.ArrayDeque` (array-based) is recommended over the legacy `java.util.Stack` for stack usage.

# Properties
- [[Linear Data Structure]]

[^1]: [Morin](zotero://select/library/items/HYS8NDAB)
