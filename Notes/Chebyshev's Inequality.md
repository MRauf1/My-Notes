---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 (Chebyshev's [[Inequality]])[^1]
> Let $X$ be a [[Random Variable]] with finite [[Variance]] $\sigma^2$. Then for every $k > 0$
> $$
> \begin{align}
> P(|X - \mu| \geq k \sigma) &\leq \frac{1}{k^2} \\
> P(|X - \mu| < k \sigma) &\geq 1 - \frac{1}{k^2}
> \end{align}
> $$

The finite variance implies that $\mu = E(X)$ exists ([[mth Moment Existence Theorem]]). It is the special case of [[Markov's Inequality]] with $u(X) = (X - \mu)^2$ and $c = k^2 \sigma^2$.

For a particular distribution the bound $1/k^2$ is often far from the actual probability, but it cannot be improved as a bound valid for every $k$ and every distribution with finite variance: for $k \geq 1$, the distribution with $P(X = \mu \pm k\sigma) = \frac{1}{2k^2}$ each and $P(X = \mu) = 1 - \frac{1}{k^2}$ has mean $\mu$, variance $\sigma^2$, and $P(|X - \mu| \geq k\sigma) = \frac{1}{k^2}$ exactly. For $k \leq 1$ the bound is trivial.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=95)