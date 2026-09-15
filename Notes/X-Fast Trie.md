---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] X-Fast Trie[^1]
> A [[Binary Trie]] augmented with $w+1$ [[Hash Table|hash tables]] $t[0], \dots, t[w]$ — one per level — used to speed up `find(x)` to $O(\log w)$ expected time by binary-searching for the last node on $x$'s search path instead of walking down to it one level at a time.

`find(x)` in a Binary Trie is essentially complete once it locates the node $u$ where the search path falls off the trie: the missing-child case then resolves in $O(1)$ via `u.jump`. Each node at level $i$ can be labelled by the $i$-bit prefix of its search path, so $u$ lies at or below level $i$ if and only if some node at level $i$ is labelled with $x$'s highest-order $i$ bits — and $t[i]$, storing exactly the nodes at level $i$, answers that question (and finds the node) in $O(1)$ expected time.[^2] Binary-searching over $i \in \{0, \dots, w\}$ using $t[0], \dots, t[w]$ therefore locates $u$ directly.[^3]

# Operations
- **`find(x)`**: binary search for the level $\ell$ of the last node $u$ on $x$'s search path, maintaining bounds $\ell \leq (\text{answer}) < h$ and probing $t[i]$ for $i = \lfloor (\ell+h)/2 \rfloor$ at each step; each iteration roughly halves $h - \ell$, so $u$ is found after $O(\log w)$ iterations, each doing $O(1)$ work plus one $O(1)$-expected hash table lookup. Once $u$ is found, `u.jump` and the doubly-linked list of leaves finish the operation exactly as in a [[Binary Trie]].[^4] Total: $O(\log w)$ expected time.[^5]
- **`add(x)`** / **`remove(x)`**: identical to the [[Binary Trie]] algorithms, with the addition that every node created at level $i$ is added to $t[i]$ (respectively removed from $t[i]$ when deleted) — an $O(1)$-expected-time hash table operation per level touched, which does not change the overall $O(w)$ asymptotic cost.[^6]

> [!abstract] Theorem 13.2[^7]
> An XFastTrie implements the same interface as a [[Binary Search Tree]], for $w$-bit integers. It supports `add(x)` and `remove(x)` in $O(w)$ expected time and `find(x)` in $O(\log w)$ expected time per operation. The space used by an XFastTrie storing $n$ values is $O(n \cdot w)$.

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(\log w)$ expected | $O(1)$ |
| `add(x)` | $O(w)$ expected | $O(1)$ |
| `remove(x)` | $O(w)$ expected | $O(1)$ |

# Worst-Case Time Complexity
The $O(\log w)$ bound for `find(x)` is inherently an *expected*-time bound: it relies on each of the $O(\log w)$ probes into $t[0], \dots, t[w]$ taking $O(1)$ expected time, which is only guaranteed under the usual [[Hash Table]] assumptions (e.g. [[Multiplicative Hashing|multiplicative]] or [[Tabulation Hashing|tabulation]] hashing giving a low collision probability). Under adversarial or merely unlucky input, a single hash lookup can degrade to time proportional to the number of nodes sharing that bucket, so no better *worst-case* bound than the underlying [[Binary Trie]]'s $O(w)$ is proven for this construction — and since an XFastTrie still contains a complete BinaryTrie, $O(w)$ remains available as a deterministic fallback regardless of how badly the hash tables behave. `add(x)` and `remove(x)` are already stated as $O(w)$ (not $O(\log w)$) even in expectation, and since their cost is dominated by the deterministic trie walk, $O(w)$ is their worst case too.

A genuine worst-case $O(\log w)$ bound for `find(x)` *is* achievable, but not with ordinary hash tables — it requires replacing them with a dictionary that guarantees $O(1)$ worst-case lookups (e.g. via dynamic perfect hashing), or abandoning hashing entirely in favour of direct array indexing, as a van Emde Boas tree does, at the cost of much higher space.

# Space Usage
$O(n \cdot w)$ words: same asymptotic space as the underlying [[Binary Trie]], plus $O(1)$ additional overhead per node for its entry in the appropriate level's hash table.

# Properties
- [[Binary Trie]]
- [[Hash Table]]
- Still pays $O(w)$ for `add(x)`/`remove(x)` and $O(n \cdot w)$ space — both fixed by [[Y-Fast Trie]].

[^1]: [Morin, p. 264](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 265](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 265](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 265](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 266](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 266](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 267](zotero://select/library/items/HYS8NDAB)
