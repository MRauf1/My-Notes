---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Theorem 1 (Computational Formula)[^1]
> For a [[Random Variable]] $X$ with finite mean $\mu$ and variance, by linearity of [[Expectation]],
> $$
> \begin{align}
> \sigma^2 = E(X^2) - 2\mu E(X) + \mu^2 = E(X^2) - \mu^2
> \end{align}
> $$

> [!abstract] Theorem 2 (Variance of an Affine Transformation)[^2]
> Let $X$ have finite mean $\mu$ and [[Variance]] $\sigma^2$. Then for all constants $a, b$,
> $$
> \begin{align}
> \text{Var}(aX + b) = a^2 \text{Var}(X)
> \end{align}
> $$

Variance is not a linear operator: shifts do not change it and scalings enter squared.

# Properties
- $E(X^2) \geq (E X)^2$, with equality iff $X$ is a [[Degenerate Distribution|constant]]; a special case of [[Jensen's Inequality]] with $\varphi(x) = x^2$.
- $\text{SD}(aX + b) = |a|\,\text{SD}(X)$ for the [[Standard Deviation]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=84)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=85)
