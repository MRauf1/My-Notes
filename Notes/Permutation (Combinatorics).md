---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] $k$-Permutation[^1]
> For a [[Set]] $A$ with $n$ elements and $k \leq n$, a $k$-permutation is a $k$-tuple of distinct elements of $A$ (order matters, no repeats). By the [[Cartesian Product Set Cardinality|mn-rule]], their number is
> $$
> \begin{align}
> P^n_k = n(n-1)\cdots(n-(k-1)) = \frac{n!}{(n-k)!}
> \end{align}
> $$

# Properties
- $P^n_n = n!$, the number of orderings of $A$; each is a [[Permutation]] (bijection) of $A$ in the algebraic sense.
- Without the distinctness requirement, the number of $k$-tuples from $A$ is $n^k$.
- $P^n_k = \binom{n}{k} k!$: every $k$-permutation arises from exactly one $k$-element [[Combination]] ordered in one of $k!$ ways.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=32)
