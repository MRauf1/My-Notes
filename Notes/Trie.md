---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Trie[^1]
> A tree that encodes a set of fixed-length sequences as root-to-leaf paths, so that a sequence's search cost is proportional to its *length* rather than to $O(\log n)$ comparisons against other stored elements.

In the structures covered here, the sequences are the $w$-bit binary representations of integers $x \in \{0, \dots, 2^w-1\}$: at level $i$, the search path turns left if bit $i$ of $x$ is $0$ and right if it is $1$, so every root-to-leaf path has length exactly $w$.[^2] This is a genuinely different strategy from a comparison-based [[Binary Search Tree]]: rather than comparing $x$ against other stored keys, a trie decomposes $x$ into its bits and uses each bit to choose a branch, the same idea that lets [[Radix Sort]] beat the comparison-sorting lower bound.

## Why use this instead of a comparison-based Binary Search Tree?
Since any $n$-element subset of $\{0, \dots, 2^w-1\}$ satisfies $\log n \leq w$, a plain [[Binary Trie]]'s $O(w)$ operations are never asymptotically faster than a comparison-based [[Binary Search Tree]]'s $O(\log n)$ — by itself it is mostly of pedagogical interest.[^3] The real payoff comes from [[X-Fast Trie]] and [[Y-Fast Trie]], which use hashing (and, for Y-Fast, secondary [[Treap|treaps]]) to bring the cost down to $O(\log w)$ *instead of* $O(w)$. Since $w$ is fixed by the machine's word size (typically $32$ or $64$) while $n$ can grow without bound, $O(\log w)$ is effectively a constant once $n$ is large enough to make $\log n > \log w$ — at that point, these tries asymptotically beat *any* comparison-based [[Binary Search Tree]], since $\log(\log n)$-style bounds are impossible for comparisons but $\log w$ is a genuine constant for fixed-width keys.

This makes the trie family the right tool specifically when: (1) keys are, or can be mapped to, fixed-width machine integers (or bit-strings) rather than arbitrary comparable objects; (2) $n$ is large enough that $\log n$ noticeably exceeds $\log w$; and (3) expected (randomized, hash-based) time bounds are acceptable rather than strict worst-case guarantees. When $n$ is modest, keys aren't naturally integer-valued, or a guaranteed (not just expected) worst case is required, a traditional balanced [[Binary Search Tree]] variant remains the simpler and often better default.

Only [[Binary Trie]] carries a true worst-case bound ($O(w)$, since it uses no hashing or randomization at all); [[X-Fast Trie]] and [[Y-Fast Trie]] speed this up only in *expectation*, and have no proven sub-linear worst case (see each note's Worst-Case Time Complexity section) — the price paid for using hash tables and randomized [[Treap|treaps]] instead of the direct array indexing a (higher-space) van Emde Boas tree would use.

# Types
- [[Binary Trie]]
- [[X-Fast Trie]]
- [[Y-Fast Trie]]

[^1]: [Morin, p. 258](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 258](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 257](zotero://select/library/items/HYS8NDAB)
