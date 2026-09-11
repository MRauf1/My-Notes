---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] AVL Tree[^1]
> A height-balanced [[Binary Search Tree]]: at every node $u$, the heights of the subtrees rooted at $u.\text{left}$ and $u.\text{right}$ differ by at most one.

This balance condition bounds the height very tightly. If $F(h)$ denotes the minimum number of leaves in an AVL tree of height $h$, then the balance condition forces $F(h)$ to obey the Fibonacci recurrence $$F(h) = F(h-1) + F(h-2), \qquad F(0) = F(1) = 1,$$ so $F(h)$ grows approximately as $\varphi^h / \sqrt{5}$, where $\varphi = (1+\sqrt{5})/2 \approx 1.61803399$ is the golden ratio (more precisely, $|\varphi^h/\sqrt{5} - F(h)| \leq 1/2$). Inverting this relationship, as in the proof that a [[2-4 Tree|2-4 tree]] with $n$ leaves has height at most $\log n$, gives an AVL tree storing $n$ elements a height of at most $$h \leq \log_\varphi n \approx 1.440420088 \log n,$$ smaller than the $2\log n$ bound of a [[Red-Black Tree]].[^1]

Balance is restored during `add(x)` and `remove(x)` by walking back up the path to the root and performing a rebalancing operation — a single or double [[Tree Rotation]] — at each node $u$ where the heights of $u$'s left and right subtrees now differ by two.[^1]

# Operations
| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(\log n)$ worst-case | $O(1)$ |
| `add(x)` | $O(\log n)$ worst-case | $O(1)$ |
| `remove(x)` | $O(\log n)$ worst-case | $O(1)$ |

Each operation first walks a search path of length $O(\log n)$, per the height bound above. Restoring balance after `add(x)` requires at most one single or double rotation at the lowest unbalanced ancestor to rebalance the *entire* tree; `remove(x)` is less forgiving; a rotation may be required at every ancestor up the path to the root, so up to $O(\log n)$ rotations can occur in the worst case, one per level.

# Space Usage
$O(n)$ words for $n$ elements: one data value and up to three neighbour references per node, plus a constant-size balance factor (or subtree height) field used to detect when a rotation is needed.

# Properties
- [[Binary Search Tree]]
- [[Tree Rotation]]
- Shorter worst-case height than a [[Red-Black Tree]] ($\log_\varphi n$ vs. $2\log n$), at the cost of potentially $O(\log n)$ rather than $O(1)$-amortized rotations per `remove(x)`.

[^1]: [Morin, p. 198](zotero://select/library/items/HYS8NDAB)
