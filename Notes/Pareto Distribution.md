---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Pareto Distribution[^1]
> $X$ has the Pareto distribution (in the Lomax, or type II, form) with parameters $\alpha, \beta > 0$ if
> $$
> \begin{align}
> h(x) = \alpha\beta(1 + \beta x)^{-(\alpha + 1)}, \qquad H(x) = 1 - (1 + \beta x)^{-\alpha}, \quad 0 < x < \infty
> \end{align}
> $$

> [!info] Generalized Pareto Distribution[^1]
> If $X | \theta \sim \Gamma(k, 1/\theta)$ and the rate $\theta \sim \Gamma(\alpha, \beta)$, then the [[Mixture Distribution|compound]] pdf of $X$ is
> $$
> \begin{align}
> h(x) = \frac{\Gamma(\alpha + k)\,\beta^k\,x^{k-1}}{\Gamma(\alpha)\Gamma(k)(1 + \beta x)^{\alpha + k}}, \quad 0 < x < \infty
> \end{align}
> $$
> the generalized Pareto distribution, a generalization of the [[F-Distribution]]. The case $k = 1$ (a conditionally [[Exponential Distribution|exponential]] $X$) is the Pareto distribution above.

Mixing an exponential or [[Gamma Distribution|gamma]] waiting time over a random, gamma-distributed rate produces a much thicker tail than any single gamma: the tail decays polynomially, $1 - H(x) \sim (\beta x)^{-\alpha}$, instead of exponentially.

# Types
- [[Burr Distribution]] (transformed Pareto): the distribution of $X^{1/\tau}$.

# Properties
- Only moments of order $< \alpha$ exist; e.g. $E(X) = \frac{1}{\beta(\alpha - 1)}$ for $\alpha > 1$.
- The generalized Pareto cdf has no simple closed form.
- The classical (type I) Pareto with minimum $x_m$ has $P(X > x) = (x_m/x)^\alpha$ for $x \geq x_m$; the Lomax form is it shifted to start at $0$. Such power laws model incomes, city sizes, and insurance losses.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=238)
