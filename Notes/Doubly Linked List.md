---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Doubly Linked List
> A [[Linked List]] similar to a [[Singly Linked List]], except that each node additionally stores a reference to the node that precedes it.[^1]

Because each node has both a `next` and a `prev` reference, the $i$-th node can be found by walking forward from the head or backward from the tail, whichever is closer, taking $O(1 + \min\{i, n-i\})$ time; `get(i)`/`set(i,x)` and `add(i,x)`/`remove(i)` are all dominated by this node-finding cost.[^2] Consequently, operations at either end run in $O(1)$ time, while operations near the middle run in $O(n)$ time in the worst case.

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Beginning) | $O(1)$ | $O(1)$ |
| Access (Middle) | $O(n)$ | $O(1)$ |
| Access (End) | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| Insert (Beginning) | $O(1)$ | $O(1)$ |
| Insert (Middle) | $O(n)$ | $O(1)$ |
| Insert (End) | $O(1)$ | $O(1)$ |
| Remove (Beginning) | $O(1)$ | $O(1)$ |
| Remove (Middle) | $O(n)$ | $O(1)$ |
| Remove (End) | $O(1)$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^*$ | Varies$^*$ |

$^*$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$3n + O(1)$ words: each of the $n$ nodes stores one data field, one next-reference, and one prev-reference — only one of the three fields holds actual data.[^3]

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 64](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 65](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 68](zotero://select/library/items/HYS8NDAB)
