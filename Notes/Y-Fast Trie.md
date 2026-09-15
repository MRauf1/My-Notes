---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Y-Fast Trie[^1]
> An [[X-Fast Trie|X-Fast Trie]], `xft`, that stores only a sample of roughly $1$ out of every $w$ elements, with the rest held in $O(n/w)$ secondary [[Treap|treaps]] (one per sampled element, extended to support `split`/`merge`) — fixing both of X-Fast Trie's remaining weaknesses: `add(x)`/`remove(x)` drop to $O(\log w)$ expected time, and total space drops to $O(n)$.

Sampling only $O(n/w)$ elements keeps `xft` itself at $O(n)$ space, and since only roughly one out of every $w$ `add(x)`/`remove(x)` calls needs to touch `xft` (an $O(w)$-time operation) at all, its amortized/expected contribution to every update is only $O(1)$.[^2] The elements *not* sampled into `xft` live in secondary treaps, roughly $n/w$ of them, each expected to hold $O(w)$ elements — small enough that a [[Treap]]'s $O(\log(\text{size}))$ operations cost only $O(\log w)$.[^3]

> [!abstract] Lemma 13.1[^4]
> Let $x$ be an integer stored in a YFastTrie and let $n_x$ denote the number of elements in the treap $t$ containing $x$. Then $E[n_x] \leq 2w - 1$.

# Operations
- **`find(x)`**: first `find(x)` in `xft` ($O(\log w)$ expected) to locate the sampled predecessor/successor and its treap $t$, then `find(x)` in $t$ itself — by Lemma 13.1, $E[|t|] = O(w)$, so this second search also costs $O(\log w)$ expected.[^5]
- **`add(x)`**: add $x$ to its treap $t$ in $O(\log w)$ expected time; splitting $t$ around $x$ can also be done in $O(\log w)$ expected time. Only with probability $1/w$ does $x$ also need to be added to `xft` itself, at $O(w)$ cost — giving an overall expected cost of $O(\log w) + \frac{1}{w}O(w) = O(\log w)$.[^6]
- **`remove(x)`**: locate $x$ in `xft` in $O(\log w)$ expected time, remove it from its treap in $O(\log w)$ expected time (merging as needed), and, only with probability $1/w$, remove it from `xft` at $O(w)$ cost — again $O(\log w)$ expected overall.[^7]

> [!abstract] Theorem 13.3[^8]
> A YFastTrie implements the same interface as a [[Binary Search Tree]], for $w$-bit integers. It supports `add(x)`, `remove(x)`, and `find(x)` in $O(\log w)$ expected time per operation. The space used by a YFastTrie storing $n$ values is $O(n + w)$.

| Operation | Time Complexity | Space Complexity |
| --- | --- | --- |
| `find(x)` | $O(\log w)$ expected | $O(1)$ |
| `add(x)` | $O(\log w)$ expected | $O(1)$ |
| `remove(x)` | $O(\log w)$ expected | $O(1)$ |

# Worst-Case Time Complexity
Every bound above is an *expected* bound, and a Y-Fast Trie has no proven sub-linear worst-case guarantee. Two independent sources of randomness are involved, and both can fail simultaneously: the [[X-Fast Trie]] layer inherits its own lack of a worst-case guarantee (see [[X-Fast Trie#Worst-Case Time Complexity]]), and Lemma 13.1 only bounds the *expected* size $E[n_x] \leq 2w-1$ of the [[Treap]] holding a given element — not its worst-case size. An unlucky sequence of random priorities (or an adversarially chosen input, if the priorities were ever predictable) could leave a single treap holding close to all $n$ elements, at which point a [[Treap]] operation on it costs $O(n)$, not $O(\log w)$. Combining this with the $O(w)$ (or worse) fallback in `xft`, no bound better than $O(n)$ is proven for a Y-Fast Trie's worst case.

This is the fundamental trade-off that distinguishes X-Fast/Y-Fast Tries from a van Emde Boas tree: a van Emde Boas tree achieves a genuine *worst-case* $O(\log w)$ per operation by recursively splitting the universe and indexing directly into arrays rather than hash tables or randomized trees, at the cost of $O(2^w)$ space unless combined with further (again hashing-based) space-reduction tricks.

# Space Usage
$O(n+w)$: $O(n)$ across the sampled `xft` and the secondary treaps combined, plus an extra $O(w)$ purely because the implementation always keeps the sentinel value $2^w - 1$ in `xft`; a version that special-cased away this sentinel would use $O(n)$ space outright.[^9]

## How does this compare to a traditional balanced BST, and which should I use?
A Y-Fast Trie's $O(\log w)$ bound genuinely beats a [[Treap]]'s or [[Red-Black Tree]]'s $O(\log n)$ once $n$ is large enough that $\log n$ exceeds $\log w$ — and since $w$ is fixed by the key width (e.g. $32$ or $64$ for machine integers) while $n$ can grow arbitrarily, this eventually always happens, making a Y-Fast Trie asymptotically the better choice at large scale for fixed-width integer keys. In practice, though, several things favor a traditional balanced BST as the default: (1) a Y-Fast Trie only works for integer (or integer-encodable) keys, not arbitrary comparable objects; (2) its bounds are all *expected*, resting on hashing and randomized treaps, not the worst-case guarantee a [[Red-Black Tree]] or [[AVL Tree]] provides; and (3) it carries far higher implementation complexity and constant factors — multiple hash tables, a doubly-linked leaf list, and augmented split/merge treaps, versus a single self-balancing tree. Reach for a Y-Fast (or X-Fast) Trie specifically when working with fixed-width integer keys at a scale large enough that $\log w$ vs. $\log n$ actually matters in practice (e.g. IP routing tables); otherwise, a traditional [[Binary Search Tree]] remains the simpler and often perfectly adequate choice.

# Properties
- [[X-Fast Trie]]
- [[Treap]]
- [[Trie]]

[^1]: [Morin, p. 267](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 267](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 267](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 271](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 269](zotero://select/library/items/HYS8NDAB)
[^6]: [Morin, p. 269](zotero://select/library/items/HYS8NDAB)
[^7]: [Morin, p. 271](zotero://select/library/items/HYS8NDAB)
[^8]: [Morin, p. 272](zotero://select/library/items/HYS8NDAB)
[^9]: [Morin, p. 272](zotero://select/library/items/HYS8NDAB)
