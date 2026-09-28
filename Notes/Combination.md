---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Combination[^1]
> For a [[Set]] $A$ with $n$ elements and $0 \leq k \leq n$, a $k$-combination is a $k$-element [[Subset]] of $A$ (order does not matter). Their number, the binomial coefficient, is
> $$
> \begin{align}
> \binom{n}{k} = C^n_k = \frac{n!}{k!(n-k)!}
> \end{align}
> $$

Derivation: each $k$-subset generates $P^k_k = k!$ distinct [[Permutation (Combinatorics)|$k$-permutations]], different subsets generate disjoint sets of permutations, and every $k$-permutation arises from some subset. Hence $P^n_k = \binom{n}{k} k!$.

# Properties
- $\binom{n}{k} = \binom{n}{n-k}$, $\binom{n}{0} = \binom{n}{n} = 1$.
- $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$ (Pascal's rule).
- $\sum_{k=0}^n \binom{n}{k} = 2^n = |\mathcal{P}(A)|$, the size of the [[Power Set]].
- Called the binomial coefficient because it is the coefficient in the [[Binomial Theorem]] $(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$: choose the $k$ factors of $(a+b)$ that contribute $a$.
- $\binom{n}{k} \leq P^n_k$, with equality only for $k \in \{0, 1\}$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=33)
