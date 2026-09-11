---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Multiplicative Hashing
> An efficient method for generating hash values for a [[Hash Table]] of size $2^d$, based on [[Modular Arithmetic]] and integer division: for $x \in \{0, \dots, 2^w - 1\}$, $$\text{hash}(x) = \left((z \cdot x) \bmod 2^w\right) \operatorname{div} 2^{w-d},$$ where $z$ is a randomly chosen odd integer in $\{1, \dots, 2^w - 1\}$ and, for integers $a \geq 0$, $b \geq 1$, $a \operatorname{div} b = \lfloor a/b \rfloor$.[^1]

This can be computed very efficiently: integer operations are, by default, already carried out modulo $2^w$ (where $w$ is the number of bits in a machine integer), so the $\bmod\ 2^w$ step is free; and dividing by $2^{w-d}$ is the same as dropping the rightmost $w - d$ bits of the binary representation, i.e. a right bit-shift by $w - d$.[^2]

# Properties
> [!abstract] Lemma 5.1[^3]
> Let $x$ and $y$ be any two values in $\{0, \dots, 2^w-1\}$ with $x \neq y$. Then $\Pr\{\text{hash}(x) = \text{hash}(y)\} \leq 2/2^d$.

> [!abstract] Lemma 5.2[^4]
> For any data value $x$, the expected length of the list $t[\text{hash}(x)]$ in a [[Chained Hash Table]] is at most $n_x + 2$, where $n_x$ is the number of occurrences of $x$ in the hash table.

The proof of these bounds relies on the fact that, if $z$ is chosen uniformly at random from a set $S$, then $z \cdot t$ is again uniformly distributed over $S$.[^5]

[^1]: [Morin, p. 104](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 104](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 104](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 105](zotero://select/library/items/HYS8NDAB)
[^5]: [Morin, p. 107](zotero://select/library/items/HYS8NDAB)
