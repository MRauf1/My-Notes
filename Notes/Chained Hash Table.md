---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Chained Hash Table
> A [[Hash Table]] that resolves collisions with hashing with chaining: it stores data as an array, $t$, of lists, where the $i$-th list holds every element $x$ with $\text{hash}(x) = i$, alongside an integer $n$ tracking the total number of items across all lists.[^1]

The hash value $\text{hash}(x)$ lies in $\{0, \dots, \text{length}(t) - 1\}$, and the invariant $n \leq \text{length}(t)$ is maintained so that the average number of elements per list is $n / \text{length}(t) \leq 1$.[^2] The buckets $t[i]$ are most commonly implemented as [[Singly Linked List|singly linked lists]] rather than as [[ArrayList|ArrayLists]]: since most buckets are expected to hold only $O(1)$ elements, a linked list avoids the wasted capacity that an ArrayList's doubling scheme would incur independently in each of the $\text{length}(t)$ buckets, while still supporting $O(1)$-time append and removal without needing random access into the bucket.

# Operations
- **`add(x)`**: first grows $t$ if necessary, then hashes $x$ to $i = \text{hash}(x)$ and appends $x$ to the list $t[i]$; appending takes only constant time in any of the standard list implementations.[^3]
- **`remove(x)`**: iterates over the list $t[\text{hash}(x)]$ to find and remove $x$, taking $O(n_{\text{hash}(x)})$ time, where $n_i$ denotes the length of the list stored at $t[i]$.[^4]
- **`find(x)`**: performs a [[Linear Search]] on the list $t[\text{hash}(x)]$, taking time proportional to the length of that list.[^5]
- **Growing**: if $t$ needs to grow, its length is doubled and every element is reinserted into the new table;[^6] this cost is only constant when amortized over a sequence of insertions.[^7]

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(1)$ expected$^*$ | $O(1)$ |
| `add(x)` | $O(1)$ expected$^*$ | $O(1)$ |
| `remove(x)` | $O(1)$ expected$^*$ | $O(1)$ |
| Grow | $O(m)$ total$^\dagger$ | $O(n)$ |

$^*$Ignoring the cost of calls to `grow()`, and assuming a good hash function makes $n_{\text{hash}(x)} = O(n/\text{length}(t)) = O(1)$ in expectation.
$^\dagger$Beginning from an empty table, any sequence of $m$ `add(x)`/`remove(x)` operations spends a total of $O(m)$ time across all calls to `grow()`.

> [!abstract] Theorem 5.1[^8]
> A ChainedHashTable implements the USet interface. Ignoring the cost of calls to `grow()`, a ChainedHashTable supports `add(x)`, `remove(x)`, and `find(x)` in $O(1)$ expected time per operation. Furthermore, beginning with an empty ChainedHashTable, any sequence of $m$ `add(x)` and `remove(x)` operations results in a total of $O(m)$ time spent during all calls to `grow()`.

# Space Usage
$n + O(n)$ words: the invariant $n \leq \text{length}(t)$ together with doubling keeps $\text{length}(t) = \Theta(n)$, and the $n$ stored elements are spread across the $\text{length}(t)$ list headers.

# Properties
- [[Multiplicative Hashing]]
- [[Tabulation Hashing]]

[^1]: [Morin, p. 101](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 102](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 102](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 103](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 103](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 102](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 103](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 108](zotero://select/library/items/HYS8NDAB)
