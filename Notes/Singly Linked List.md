---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Singly Linked List
> A [[Linked List]] made up of nodes, each storing a data value and a reference to the next node in the sequence; the last node's next reference is nil.[^1]

For efficiency, a Singly Linked List keeps references to its first (`head`) and last (`tail`) nodes, plus an integer count of its length, so that pushing/popping at the head and adding at the tail can all be done in $O(1)$ time without traversal.[^2] It implements the [[Stack]] interface (push/pop at the head) and the [[Queue]] interface (add at the tail, remove at the head) — see [[Stack (Linked List)]] and [[Queue (Linked List)]].[^3] Multiple levels of singly-linked lists are also the building block of a [[Skiplist]].

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access | $O(n)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| Insert (Beginning) | $O(1)$ | $O(1)$ |
| Insert (Middle) | $O(n)$ | $O(1)$ |
| Insert (End) | $O(1)$ | $O(1)$ |
| Remove (Beginning) | $O(1)$ | $O(1)$ |
| Remove (Middle) | $O(n)$ | $O(1)$ |
| Remove (End) | $O(n)^*$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^\dagger$ | Varies$^\dagger$ |

$^*$Unlike insertion at the end, removing the tail requires finding its predecessor node, which cannot be done in $O(1)$ time without a `prev` reference; see [[Doubly Linked List]] for a variant that supports this in $O(1)$.
$^\dagger$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$2n + O(1)$ words: each of the $n$ nodes stores one data field and one next-reference, plus a constant number of bookkeeping fields (`head`, `tail`, length).

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 61](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 62](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 64](zotero://select/library/items/HYS8NDAB)
