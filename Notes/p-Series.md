---
tags:
  - mathematics
  - real_analysis
---

# Definition

> [!abstract] Theorem 1 (p-Series Convergence)[^1]
> For real $p$, the series $\sum_{n=1}^{\infty} \frac{1}{n^p}$ converges if $p > 1$ and diverges if $p \leq 1$.

> [!abstract] Theorem 2 (Related Logarithmic Series)[^2]
> For real $p$, the series $\sum_{n=2}^{\infty} \frac{1}{n (\log n)^p}$ converges if $p > 1$ and diverges if $p \leq 1$.

Both follow from the [[Cauchy Condensation Test]] applied to the non-increasing, non-negative terms $a_n = 1/n^p$ (resp. $a_n = 1/(n (\log n)^p)$); the condensed series reduces to a [[Geometric Series]].

# Properties
- [[Infinite Series Integral Test]] gives an alternative proof of Theorem 1.

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=72)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/3BD27IHF?page=72)
