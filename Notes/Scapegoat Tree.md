---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Scapegoat Tree[^1]
> A [[Binary Search Tree]] that keeps itself balanced purely through occasional [[Partial Rebuilding]] operations, rather than through local restructuring on every update: alongside the number $n$ of nodes, it maintains a counter $q$ that upper-bounds $n$, obeying $q/2 \leq n \leq q$ at all times.

The name reflects the rebalancing strategy: when an insertion makes the tree too deep, rather than fixing the structure incrementally, the tree walks up from the offending node to find one badly unbalanced ancestor — the "scapegoat" — and rebuilds only that ancestor's subtree from scratch, leaving the rest of the tree untouched.[^1] A Scapegoat Tree has logarithmic height: at all times, $$\text{height} \leq \log_{3/2} q \leq \log_{3/2} 2n < \log_{3/2} n + 2. \tag{8.1}$$

# Operations
- **`find(x)`**: the standard [[Binary Search Tree]] search; takes time proportional to the height of the tree, which by (8.1) is $O(\log n)$.[^2]
- **`add(x)`**: increment $n$ and $q$, then add $x$ as a new leaf $u$ using the usual BinarySearchTree `add(x)` algorithm. If $\text{depth}(u) \leq \log_{3/2} q$, stop — $u$ is the only node that can possibly violate the height bound, so nothing else needs checking.[^3] Otherwise, walk from $u$ back up to the root to find a **scapegoat** $w$: a node such that $$\frac{\text{size}(w.\text{child})}{\text{size}(w)} > \frac{2}{3}, \tag{8.2}$$ where $w.\text{child}$ is the child of $w$ on the path to $u$. [[Partial Rebuilding|Rebuild]] the entire subtree rooted at $w$ into a perfectly balanced tree; since (8.2) shows $w$'s subtree was not a complete binary tree even before $u$ was added, this rebuild decreases the height by at least $1$, restoring the bound.[^4]
- **`remove(x)`**: search for $x$ and remove it with the usual BinarySearchTree `remove(x)` algorithm — this can never increase the height. Decrement $n$ (leaving $q$ unchanged); if $q > 2n$, [[Partial Rebuilding|rebuild]] the whole tree into a perfectly balanced one and set $q \leftarrow n$.[^5]

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(\log n)$ | $O(1)$ |
| `add(x)` | $O(\log n)$$^*$ | $O(1)$ |
| `remove(x)` | $O(\log n)$$^*$ | $O(1)$ |

$^*$Ignoring the cost of calls to `rebuild(u)`; see below.

> [!abstract] Lemma 8.1[^6]
> Let $u$ be a node of depth $h > \log_{3/2} q$ in a ScapegoatTree. Then there exists a node $w$ on the path from $u$ to the root such that $\dfrac{\text{size}(w)}{\text{size}(\text{parent}(w))} > \dfrac{2}{3}$.

> [!abstract] Lemma 8.2[^7]
> During a call to `add(x)` in a ScapegoatTree, the cost of finding the scapegoat $w$ and rebuilding the subtree rooted at $w$ is $O(\text{size}(w))$.

> [!abstract] Lemma 8.3[^8]
> Starting with an empty ScapegoatTree, any sequence of $m$ `add(x)` and `remove(x)` operations causes at most $O(m \log m)$ total time to be used by `rebuild(u)` operations.

> [!abstract] Theorem 8.1[^9]
> A ScapegoatTree implements the same interface as a [[Binary Search Tree]]. Ignoring the cost of `rebuild(u)` operations, a ScapegoatTree supports `add(x)`, `remove(x)`, and `find(x)` in $O(\log n)$ time per operation. Furthermore, beginning with an empty ScapegoatTree, any sequence of $m$ `add(x)` and `remove(x)` operations results in a total of $O(m \log m)$ time spent during all calls to `rebuild(u)`.

# Space Usage
$O(n)$ words for $n$ elements: one data value and up to three neighbour references per node, plus the constant-size $n$/$q$ counters.

# Properties
- [[Binary Search Tree]]
- [[Partial Rebuilding]]
- Like [[Treap]] and [[Skiplist]], achieves $O(\log n)$-time operations without relying on randomization — instead trading worst-case guarantees on individual `add(x)`/`remove(x)` calls for amortized guarantees across a sequence of operations.
- A [[Red-Black Tree]] improves on exactly this trade-off: it guarantees the same $O(\log n)$ height deterministically, but bounds `add(x)`/`remove(x)` in $O(\log n)$ *worst-case* time rather than only amortized time.

[^1]: [Morin, p. 165](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 167](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 168](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 168](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 169](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 170](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 170](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 171](zotero://select/library/items/HYS8NDAB)
[^9]: [Morin, p. 172](zotero://select/library/items/HYS8NDAB)
