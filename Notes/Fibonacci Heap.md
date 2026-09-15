---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Fibonacci Heap[^1]
> A [[Meldable Heap]] implemented as a forest of heap-ordered trees rather than a single tree, which merges lazily — simply concatenating forests on `merge`/`add(x)` and only doing the work of consolidating trees during `remove()` — so that most operations are cheap and the cost of consolidation is spread (amortized) across the sequence of operations.

Unlike the single heap-ordered binary tree behind a plain [[Meldable Heap]], a Fibonacci Heap keeps a *collection* of trees, one of whose roots holds the minimum and is tracked directly. `decrease-key` is supported directly (something neither a [[Binary Heap]] nor a generic [[Meldable Heap]] offers without a full `remove`+`add`): a node whose key is decreased is cut out, together with its subtree, and reattached as a new root; to keep this cheap over many operations, each node tracks whether it has already lost a child this way, and cascades the cut up to its parent if it has ("marking"), which is what keeps the trees from degenerating and preserves the amortized bounds below.

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find-min` | $O(1)$ | $O(1)$ |
| `add(x)` / `insert(x)` | $O(1)$ amortized | $O(1)$ |
| `merge(h1, h2)` | $O(1)$ amortized | $O(1)$ |
| `decrease-key(u, x)` | $O(1)$ amortized | $O(1)$ |
| `remove()` / `extract-min` | $O(\log n)$ amortized | $O(1)$ |
| `remove(u)` / `delete(u)` | $O(\log n)$ amortized | $O(1)$ |

`remove(u)` is implemented as `decrease-key(u, -\infty)` followed by `remove()`.

# Space Usage
$O(n)$ words for $n$ elements: each node stores one data value, a degree, a mark bit, and a constant number of child/sibling/parent references.

# Properties
- [[Meldable Heap]]
- [[Priority Queue]]
- Its $O(1)$-amortized `decrease-key`, far cheaper than a [[Binary Heap]]'s $O(\log n)$, is what makes it the classical choice for graph algorithms that repeatedly lower priorities, such as Dijkstra's shortest-path algorithm and Prim's minimum-spanning-tree algorithm.

[^1]: [Morin, p. 214](zotero://select/library/items/HYS8NDAB)
