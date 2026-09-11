---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Hash Table
> An efficient [[Data Structure]] for storing a small number, $n$, of integers from a large universe $U = \{0, \dots, 2^w - 1\}$, by mapping each item to an index of an underlying table via a hash function.[^1]

The term hash table encompasses a broad range of data structures that all rely on this idea;[^1] [[Chained Hash Table]] and [[Linear Hash Table]] are the two described here. Both implement the USet interface (`add(x)`, `remove(x)`, `find(x)`) over a table $t$ whose length is kept within a constant factor of $n$. Very often a hash table stores data that is not itself an integer — in that case, an integer [[Hash Code|hash code]] is computed for each data item and used in place of the item itself.[^2] The performance of any hash table depends critically on the choice of hash function: a good one spreads elements evenly across the table so that the expected number of elements sharing a table location is $O(n / \text{length}(t)) = O(1)$.[^3]

# Operations
| Operation | [[Chained Hash Table]] | [[Linear Hash Table]] |
| --- | --- | --- |
| `find(x)` | $O(1)$ expected$^*$ | $O(1)$ expected$^*$ |
| `add(x)` | $O(1)$ expected$^*$ | $O(1)$ expected$^*$ |
| `remove(x)` | $O(1)$ expected$^*$ | $O(1)$ expected$^*$ |

$^*$Expected time under a good hash function, ignoring the amortized cost of occasional table resizing; that resizing cost is itself only $O(1)$ amortized per operation, so any sequence of $m$ operations spends a total of $O(m)$ time resizing.

# Space Usage
Both variants maintain $\text{length}(t) = \Theta(n)$, so both use $n + O(n)$ words to store $n$ elements; see [[Chained Hash Table]] and [[Linear Hash Table]] for the exact accounting.

# Types
- [[Chained Hash Table]]
- [[Linear Hash Table]]

# Properties
- [[Hash Code]]
- [[Multiplicative Hashing]]
- [[Tabulation Hashing]]

[^1]: [Morin, p. 101](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 101](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 103](zotero://select/library/items/HYS8NDAB)
