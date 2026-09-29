---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Burr Distribution (Transformed Pareto)[^1]
> If $X$ has the [[Pareto Distribution]] with cdf $H(x) = 1 - (1 + \beta x)^{-\alpha}$ and $Y = X^{1/\tau}$ for $\tau > 0$ (so $X = Y^\tau$), then
> $$
> \begin{align}
> G(y) = H(y^\tau) = 1 - (1 + \beta y^\tau)^{-\alpha}, \qquad g(y) = \frac{\alpha\beta\tau\,y^{\tau - 1}}{(1 + \beta y^\tau)^{\alpha + 1}}, \quad 0 < y < \infty
> \end{align}
> $$

Derived by the [[Cumulative Distribution Function Method]]: $G(y) = P(X^{1/\tau} \leq y) = P(X \leq y^\tau)$.

# Properties
- A flexible thick-tailed family: $\tau$ controls the shape near $0$ and, together with $\alpha$, the polynomial tail $1 - G(y) \sim (\beta y^\tau)^{-\alpha}$, so moments exist only for order $< \alpha\tau$.
- $\tau = 1$ recovers the Pareto distribution.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=238)
