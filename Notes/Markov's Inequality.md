---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 (Markov's [[Inequality]])[^1]
> Let $u(X)$ be a non-negative [[Function]] of [[Random Variable]] $X$. If $E[u(X)]$ exists, then for every positive constant c
> $$
> \begin{align}
> P(u(X) \geq c) \leq \frac{E[u(X)]}{c}
> \end{align}
> $$

# Types
- [[Chebyshev's Inequality]]

# Questions
> [!question]- Trigger: you need an upper bound on a tail probability $P[u(X) \ge c]$, and all you know is an expectation. What pointwise bound produces it?
> Bound below, pointwise, by a function whose expectation you know: $u(x) \ge c\,\mathbb{1}\{u(x) \ge c\}$ for $u \ge 0$. Taking $E$ (monotone) gives $E[u(X)] \ge c\,P[u(X) \ge c]$. Choosing $u$ well gives the variants: $(x-\mu)^2$ gives [[Chebyshev's Inequality]], and $e^{tx}$ gives the Chernoff bound.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=95)