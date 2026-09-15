---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] B-Tree[^1]
> A generalization of a [[2-4 Tree]] — indeed, a 2-4 tree is exactly the special case $B=2$[^2] — efficient in the [[External Memory Model]]: for an integer $B \geq 2$, all leaves have the same depth, and every non-root internal node has between $B$ and $2B$ children (the root, between $2$ and $2B$).[^3]

The height of a B-tree is proportional to $\log_B(\text{number of leaves})$ — a much shallower tree than a [[Binary Search Tree]] once $B$ is large.[^4] Each node $u$ stores its children in an array `u.children` and its keys in an array `u.keys[0..2B-1]`; a node with $k$ children stores exactly $k-1$ keys, in `u.keys[0..k-2]`, with the remaining entries set to nil (a non-root leaf holds between $B-1$ and $2B-1$ keys).[^5] The keys obey an order generalizing the [[Binary Search Tree]] property: within a node, `u.keys[0] < u.keys[1] < ... < u.keys[k-2]`, and for each $i$, `u.keys[i]` is larger than every key in the subtree rooted at `u.children[i]` and smaller than every key in the subtree rooted at `u.children[i+1]`.[^6]

Since a node's data has size $O(B)$, $B$ is chosen, in an [[External Memory Model|external-memory]] setting, so that one node fits exactly into one [[BlockStore]] block — making the running time of a B-tree operation, in that model, proportional to the number of nodes it accesses.[^7]

# Operations
- **`find(x)`**: at each node $u$, check whether $x \in$ `u.keys`; if not, find the smallest $i$ with `u.keys[i] > x` and recurse into `u.children[i]` (or the rightmost child, if no such key exists), tracking the most recently seen key larger than $x$ to return as the successor if $x$ is never found.[^8] This search-within-a-node is implemented by `find_it(a, x)`, a [[Binary Search]] over the nil-padded sorted array `a = u.keys`, running in $O(\log(\text{length}(a))) = O(\log B)$ time.[^9][^10]
- **`add(x)`**: since B-tree nodes store no parent pointers, `add(x)` is implemented recursively.[^11] After the downward search locates where $x$ belongs, rebalancing is done by **splitting**: a node $u$ with $2B$ keys and $2B+1$ children is split by creating a new node $w$ that adopts $u$'s $B$ largest children and $B$ largest keys, leaving $u$ with $B$ children and $B$ keys; the one remaining "middle" key is passed up to $u$'s parent, which adopts $w$ as a new child.[^12] A split touches only three nodes ($u$, $w$, and their parent) — exactly why B-tree nodes omit parent pointers: maintaining them would force updating a parent pointer in each of $w$'s newly adopted $B+1$ children, inflating a split from $3$ external memory accesses to $B+4$.[^13]
- **`remove(x)`**: the mirror image of `add(x)`, using **merge** and **borrow** operations (analogous to those of a [[2-4 Tree]]) to fix a node left with too few keys after deletion; like a split, each merge or borrow touches only three nodes.[^14]

> [!abstract] Lemma 14.1[^15]
> Starting with an empty B-tree, any sequence of $m$ `add(x)`/`remove(x)` operations performs at most $3m/2$ splits, merges, and borrows in total.

## Two Models, Two Running Times
Because a B-tree's branching factor $B$ trades node count for node size, its cost differs sharply between the [[External Memory Model]] (which counts only nodes accessed) and the word-RAM model (which counts every instruction, including the $O(\log B)$ `find_it` search within each node):[^16]

| Operation | External Memory Model | Word-RAM Model |
| --- | --- | --- |
| `find(x)` | $O(\log_B n)$ | $O(\log_B n) \times O(\log B) = O(\log n)$ |
| `add(x)` | $O(\log_B n)$ | $O(\log n)$ downward $+$ $O(B \log n)$ upward (splitting)$^*$ |
| `remove(x)` | $O(\log_B n)$ | $O(\log n)$ downward $+$ $O(B \log_B n)$ upward (merging/borrowing)$^*$ |

$^*$By Lemma 14.1, only $O(1)$ splits/merges/borrows occur per operation amortized, each costing $O(B)$ in the word-RAM model to move keys and children between nodes — giving an amortized word-RAM cost of $O(B + \log n)$ for `add(x)`.[^17]

> [!abstract] Theorem 14.1 (External Memory B-Trees)[^18]
> A BTree implements the same interface as a [[Binary Search Tree]]. In the external memory model, a BTree supports `add(x)`, `remove(x)`, and `find(x)` in $O(\log_B n)$ time per operation.

> [!abstract] Theorem 14.2 (Word-RAM B-Trees)[^19]
> A BTree implements the same interface as a [[Binary Search Tree]]. In the word-RAM model, and ignoring the cost of splits, merges, and borrows, a BTree supports `add(x)`, `remove(x)`, and `find(x)` in $O(\log n)$ time per operation. Furthermore, beginning with an empty BTree, any sequence of $m$ `add(x)`/`remove(x)` operations spends a total of $O(Bm)$ time performing splits, merges, and borrows.

# Space Usage
$O(n)$ words: spread across $O(n/B)$ nodes of size $O(B)$ each, rather than the $O(n)$ single-key nodes of a plain [[Binary Search Tree]] — the same total data volume, but far fewer, much larger nodes, which is what makes each one worth a full block transfer.

# Properties
- [[2-4 Tree]]
- [[Binary Search Tree]]
- [[External Memory Model]]
- [[Binary Search]]

[^1]: [Morin, p. 277](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 278](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 278](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 278](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 278](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 278](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 279](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 280](zotero://select/library/items/HYS8NDAB)
[^9]: [Morin, p. 281](zotero://select/library/items/HYS8NDAB)
[^10]: [Morin, p. 281](zotero://select/library/items/HYS8NDAB)
[^11]: [Morin, p. 282](zotero://select/library/items/HYS8NDAB)
[^12]: [Morin, p. 282](zotero://select/library/items/HYS8NDAB)
[^13]: [Morin, p. 282](zotero://select/library/items/HYS8NDAB)
[^14]: [Morin, p. 293](zotero://select/library/items/HYS8NDAB)
[^15]: [Morin, p. 293](zotero://select/library/items/HYS8NDAB)
[^16]: [Morin, p. 282](zotero://select/library/items/HYS8NDAB)
[^17]: [Morin, p. 287](zotero://select/library/items/HYS8NDAB)
[^18]: [Morin, p. 295](zotero://select/library/items/HYS8NDAB)
[^19]: [Morin, p. 296](zotero://select/library/items/HYS8NDAB)
