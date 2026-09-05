---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Skiplist
> A probabilistic [[Data Structure]] consisting of a sequence of levels $L_0, \dots, L_h$, each a [[Singly Linked List]], where $L_0$ holds all $n$ elements in sorted order and each higher level $L_r$ holds a random subset of the elements in $L_{r-1}$, obtained by independently including each element with probability $1/2$ (a coin toss), stopping once a level is reached that is empty.[^1]

A Skiplist requires its elements to be kept in sorted order: finding an element relies on comparing against this order to decide whether to move right along a level or step down to the level below.[^2] The height of an element $x$ is the highest level in which $x$ appears, and the height of the skiplist itself is the height of its tallest element.[^1] At the head of every level sits a sentinel (dummy) node, and there is a short search path from the sentinel of $L_h$ down to any element in $L_0$ — this short path is what makes lookups efficient.[^2]

Because element heights are assigned randomly, the running time of skiplist operations is expressed as an *expectation* over these random coin tosses (in practice simulated with a pseudo-random generator), rather than as a worst-case bound.[^1]

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (get(i) / set(i, x)) | $O(\log n)$ expected | $O(1)$ |
| Search (Sorted) (find(x)) | $O(\log n)$ expected | $O(1)$ |
| Insert (by index, add(i, x)) | $O(\log n)$ expected | $O(1)$ |
| Insert (by value, add(x)) | $O(\log n)$ expected | $O(1)$ |
| Remove (by index, remove(i)) | $O(\log n)$ expected | $O(1)$ |
| Remove (by value, remove(x)) | $O(\log n)$ expected | $O(1)$ |

Indexed by position, a Skiplist implements the List interface (get/set/add/remove by index);[^3] indexed by value, it implements a sorted associative container's interface — an SSet, supporting add/remove/find by value.[^4] Unlike a plain [[Doubly Linked List]] or [[Space Efficient Linked List]], these complexities are uniform: they do not depend on whether the index or value is near the beginning, middle, or end.

# Space Usage
A Skiplist storing $n$ elements has expected size $O(n)$.[^5]

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 83](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 84](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 93](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 88](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 97](zotero://select/library/items/HYS8NDAB)
