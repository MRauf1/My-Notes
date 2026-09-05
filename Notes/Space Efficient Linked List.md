---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Space Efficient Linked List
> A [[Doubly Linked List]] of blocks (arrays) of size $b$ instead of individual elements, reducing the pointer overhead of a plain [[Doubly Linked List]] while keeping efficient operations near either end.[^1]

Except possibly for the last block, every block holds between $b-1$ and $b+1$ elements, so storing $n$ elements requires only $O(n/b)$ blocks, wasting only $O(b + n/b)$ space in total — for $b = \Theta(\sqrt{n})$, this approaches the $\Theta(\sqrt{n})$ lower bound also achieved by a [[RootishArrayList]].[^2] Rebalancing a block that becomes too empty or too full is handled by `spread()`/`gather()` operations, each costing $O(b^2)$, but a sequence of $m$ insertions/removals triggers only $O(m/b)$ such rebalances, so their total cost is $O(bm)$ — i.e. $O(b)$ amortized per operation.[^3]

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| Access (Beginning) | $O(1)$ | $O(1)$ |
| Access (Middle) | $O(n/b)$ | $O(1)$ |
| Access (End) | $O(1)$ | $O(1)$ |
| [[Linear Search\|Search (Unsorted)]] | $O(n)$ | $O(1)$ |
| Insert (Beginning) | $O(b)^*$ | $O(1)$ |
| Insert (Middle) | $O(b + n/b)^*$ | $O(1)$ |
| Insert (End) | $O(b)^*$ | $O(1)$ |
| Remove (Beginning) | $O(b)^*$ | $O(1)$ |
| Remove (Middle) | $O(b + n/b)^*$ | $O(1)$ |
| Remove (End) | $O(b)^*$ | $O(1)$ |
| [[Sorting Algorithm\|Sort]] | Varies$^\dagger$ | Varies$^\dagger$ |

$^*$Amortized, accounting for the cost of `spread()`/`gather()` rebalancing (see above).[^4]
$^\dagger$Depends on the sorting algorithm used; see [[Sorting Algorithm]].

# Space Usage
$n + O(b + n/b)$ words, which approaches $n + O(\sqrt{n})$ when $b = \Theta(\sqrt{n})$ — the same order as a [[RootishArrayList]].[^2]

# Properties
- [[Linear Data Structure]]

[^1]: [Morin, p. 68](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 69](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 76](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 77](zotero://select/library/items/HYS8NDAB)
