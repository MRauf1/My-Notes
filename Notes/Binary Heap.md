---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Binary Heap[^1]
> A [[Priority Queue]] implementation that uses [[Eytzinger's Method]] to represent a heap-ordered [[Complete Binary Tree (Data Structures and Algorithms)|complete binary tree]] implicitly as an array $a$: the value at index $i$ is never smaller than the value at index $\text{parent}(i)$, except at the root ($i=0$) — so the minimum element is always $a[0]$.

# Operations
- **`add(x)`**: grow $a$ if it is full, place $x$ at $a[n]$, and increment $n$; then repeatedly swap $x$ with its parent — "bubbling up" — until $x$ is no longer smaller than its parent, restoring the heap property.[^2]
- **`remove()`**: replace the root with $a[n-1]$, delete that slot, and decrement $n$; the new root is now probably not the smallest, so it is repeatedly compared to its two children and swapped with the smaller of the two — "bubbling down" — until it is no larger than either child.[^3]

Both operations take time proportional to the height of the implicit tree; since that tree is complete, every level except the last is fully populated, giving a height of $O(\log n)$ — so both `add(x)` and `remove()` run in $O(\log n)$ time.[^4][^5]

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find-min` (peek $a[0]$) | $O(1)$ | $O(1)$ |
| `add(x)` | $O(\log n)$$^*$ | $O(1)$ |
| `remove()` | $O(\log n)$ | $O(1)$ |

$^*$Ignoring the occasional cost of growing $a$, which — as with any doubling [[ArrayList]] — is only $O(1)$ amortized per operation.

> [!abstract] Theorem 10.1[^6]
> A BinaryHeap implements the (priority) Queue interface. Ignoring the cost of calls to `resize()`, a BinaryHeap supports `add(x)` and `remove()` in $O(\log n)$ time per operation. Furthermore, beginning with an empty BinaryHeap, any sequence of $m$ `add(x)` and `remove()` operations results in a total of $O(m)$ time spent during all calls to `resize()`.

# Space Usage
$n + O(n)$ words: the array $a$ stores exactly the $n$ elements with no per-node pointer overhead, growing/shrinking by doubling/halving like an [[ArrayList]].

# Properties
- [[Heap]]
- [[Priority Queue]]
- [[Eytzinger's Method]]
- [[Complete Binary Tree (Data Structures and Algorithms)|Complete Binary Tree]]
- This array-based representation underlies [[Heapsort]], one of the fastest known in-place [[Sorting Algorithm|sorting algorithms]].
- Unlike a [[Meldable Heap]], its shape is completely determined by $n$; there is no `merge`/`meld` operation.

[^1]: [Morin, p. 204](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 205](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 205](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 207](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 209](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 209](zotero://select/library/items/HYS8NDAB)
