---
tags:
  - computer_science
  - data_structures_and_algorithms
---

# Definition
> [!info] Tabulation Hashing
> A method of generating [[Hash Table]] hash values that approximates fully independent, uniformly distributed hashing without the prohibitive memory cost of storing one random value per key.[^1]

The ideal (but impractical) approach would store a giant array `tab` of length $2^w$, with each entry an independent random $w$-bit integer, and compute $\text{hash}(x)$ by looking up `tab[x.hashCode()]` — but an array of size $2^w$ is far too much memory.[^1] Tabulation hashing instead treats a $w$-bit integer as $w/r$ separate $r$-bit pieces, and uses only $w/r$ tables, each of length $2^r$ and filled with independent random $w$-bit integers. To compute $\text{hash}(x)$, `x.hashCode()` is split into its $w/r$ constituent $r$-bit pieces, each piece indexes into its corresponding table, and the $w/r$ looked-up values are combined with the bitwise exclusive-or operator.[^2]

# Properties
- For any $x$, $\text{hash}(x)$ is uniformly distributed over $\{0, \dots, 2^d - 1\}$, and any *pair* of values has independent hash values — so tabulation hashing can be used in place of [[Multiplicative Hashing]] wherever a [[Chained Hash Table]] needs a hash function.[^3]
- It is not true that any set of $n$ distinct values yields $n$ mutually independent hash values; nevertheless, the $O(1)$-expected-time bound for a [[Linear Hash Table]] (Theorem 5.2) still holds under tabulation hashing.[^4]

[^1]: [Morin, p. 115](zotero://select/library/items/HYS8NDAB)
[^2]: [Morin, p. 116](zotero://select/library/items/HYS8NDAB)
[^3]: [Morin, p. 116](zotero://select/library/items/HYS8NDAB)
[^4]: [Morin, p. 116](zotero://select/library/items/HYS8NDAB)
