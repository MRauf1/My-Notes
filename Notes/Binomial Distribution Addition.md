---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Binomial Distribution Addition[^1]
> Let $X_1, \dots, X_m$ be [[Mutually Independent Random Variables|independent]] with $X_i \sim b(n_i, p)$. Then
> $$
> \begin{align}
> Y = \sum_{i=1}^m X_i \sim b\left(\sum_{i=1}^m n_i, p\right)
> \end{align}
> $$

Proof: by the [[Moment Generating Function Technique]], $M_Y(t) = \prod_i [(1-p) + pe^t]^{n_i} = [(1-p) + pe^t]^{\sum n_i}$. Intuitively, concatenating independent runs of Bernoulli trials with the same $p$ gives one longer run.

# Properties
- Requires a common $p$; with different $p_i$ the sum is not binomial (it is a Poisson-binomial distribution).
- Analogous to [[Poisson Distribution Addition]] and [[Gamma Distribution Addition]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=175)
