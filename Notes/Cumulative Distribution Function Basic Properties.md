---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Theorem 1 ([[Cumulative Distribution Function]] Characterization)[^1]
> Let $X$ be a [[Random Variable]] with cdf $F$. Then
> 1. For all $a < b$, $F(a) \leq F(b)$ ($F$ is nondecreasing)
> 2. $\lim_{x \rightarrow - \infty} F(x) = 0$
> 3. $\lim_{x \rightarrow \infty} F(x) = 1$
> 4. $\lim_{x \downarrow x_0} F(x) = F(x_0)$ ($F$ is right-[[Continuous Function|continuous]])

> [!abstract] Theorem 2 (Interval Probability)[^1]
> For $a < b$,
> $$
> \begin{align}
> P(a < X \leq b) = F_X(b) - F_X(a)
> \end{align}
> $$

> [!abstract] Theorem 3 (Point Probability)[^2]
> For all $x \in \mathbb{R}$,
> $$
> \begin{align}
> P(X = x) = F_X(x) - F_X(x^-), \quad F_X(x^-) = \lim_{z \uparrow x} F_X(z)
> \end{align}
> $$

# Properties
- Properties 2-4 follow from the [[Continuity Theorem of Probability]] applied to the monotone events $\{X \leq x_n\}$.
- Conversely, any function satisfying 1-4 is the cdf of some random variable.
- $F$ has at most countably many jumps, and $F$ is continuous at $x$ exactly when $P(X = x) = 0$ (see [[Continuous Random Variable]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=57)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=58)
