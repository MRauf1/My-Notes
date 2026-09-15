---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Binary Trie[^1]
> A [[Trie]] encoding a set of $w$-bit integers as root-to-leaf paths in a binary tree: every leaf has depth exactly $w$, and the path to the leaf for $x$ turns left at level $i$ if bit $i$ of $x$ (from the most significant) is $0$, and right if it is $1$.

Since leaves have no children, a node $u$'s child pointers `u.child[0]`/`u.child[1]` (left/right) do double duty at the leaves: there, they instead thread every leaf into a sorted [[Doubly Linked List]] (`u.child[0]` = previous, `u.child[1]` = next), anchored by a dummy sentinel node before the first and after the last leaf.[^2]

## Jump Pointers
Each node $u$ additionally stores `u.jump`: if $u$ is missing its left child, `u.jump` points to the *smallest* leaf in $u$'s subtree; if missing its right child, to the *largest* leaf in $u$'s subtree.[^3]

Their purpose is to let `find(x)` return the correct predecessor or successor in $O(w)$ time even when $x$ itself is absent. Once the search path for $x$ falls off the trie at some node $u$ (i.e. $u$ is missing the child the path would need next), every leaf in $u$'s remaining subtree is either entirely less than $x$ or entirely greater than $x$ — so `u.jump` hands back a pointer straight to the correct extreme leaf, without having to search that subtree or walk the linked list from an endpoint (which could take far longer than $O(w)$). This is what turns a Binary Trie from a bare exact-membership set into a full predecessor/successor structure at no extra asymptotic cost.

# Operations
- **`find(x)`**: follow the search path for $x$. Reaching a leaf means $x$ is found. Reaching a node $u$ missing the needed child means following `u.jump`: if $u$ is missing its left child, `u.jump` already points to the leaf wanted (the smallest value greater than $x$); if missing its right child, `u.jump` points to the largest value less than $x$, and its successor in the doubly-linked list is the wanted leaf.[^4] Dominated by the root-to-leaf walk, this takes $O(w)$ time.[^5]
- **`add(x)`**: walk down the (partial) search path for $x$, then walk back up creating any missing nodes and repairing `jump` pointers and linked-list splices along the way. One down-walk and one up-walk, each $O(w)$ constant-time steps, giving $O(w)$ total.[^6]
- **`remove(x)`**: the mirror of `add(x)`, walking up from the leaf for $x$, removing now-childless nodes, and repairing pointers — also $O(w)$.

> [!abstract] Theorem 13.1[^7]
> A BinaryTrie implements the same interface as a [[Binary Search Tree]], for $w$-bit integers. It supports `add(x)`, `remove(x)`, and `find(x)` in $O(w)$ time per operation. The space used by a BinaryTrie storing $n$ values is $O(n \cdot w)$.

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(w)$ | $O(1)$ |
| `add(x)` | $O(w)$ | $O(1)$ |
| `remove(x)` | $O(w)$ | $O(1)$ |

# Worst-Case Time Complexity
Unlike [[X-Fast Trie]] and [[Y-Fast Trie]], a Binary Trie involves no hashing or randomization: every operation is a deterministic walk of length at most $w$ along the trie (plus, for `add(x)`/`remove(x)`, a second $O(w)$ walk back up). The $O(w)$ bound in Theorem 13.1 is therefore already a true **worst-case** bound, not merely an expected or amortized one.

# Space Usage
$O(n \cdot w)$ words: each of the $n$ root-to-leaf paths contributes up to $w$ internal nodes, and paths only share nodes where their bit-prefixes agree.

# Properties
- [[Trie]]
- [[Doubly Linked List]]
- Superseded in speed by [[X-Fast Trie]] and, for both speed and space, by [[Y-Fast Trie]].

[^1]: [Morin, p. 258](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 258](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 259](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 259](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 260](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 262](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 264](zotero://select/library/items/HYS8NDAB)
