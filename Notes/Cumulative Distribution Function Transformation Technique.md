---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!abstract] Theorem 1 ([[Cumulative Distribution Function]] [[Function Transformation|Transformation]] Technique)[^1]
> Let $X$ be [[Continuous Random Variable]] with pdf $f_X$ and support $S_X$. Let $Y = g(X)$ where $g$ is [[Injective Function]] and [[Differentiable Function]] on $S_X$. Denote the inverse by $x = g^{-1}(y)$. Then
> $$
> \begin{align}
> f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|, \quad y \in S_Y
> \end{align}
> $$
> where $\frac{dx}{dy} = \frac{d[g^{-1}(y)]}{dy}$ and $S_Y = \{g(x) : x \in S_X\}$ is the [[Random Variable Support|support]] of $Y$.

Hogg et al. call $J = \frac{dx}{dy}$ the Jacobian of the transformation, for convenience; in most of mathematics it is the [[Jacobian Matrix|Jacobian]] of the inverse transformation $x = g^{-1}(y)$. The result is proved by first computing the cdf $F_Y(y) = P(g(X) \leq y)$ and differentiating; the absolute value covers decreasing $g$, where the inequality flips. It is the one-dimensional case of [[Change of Variables]].

Algorithm, assuming $Y = g(X)$ is one-to-one:[^1]
1. Find the support $S_Y$ of $Y$.
2. Solve $y = g(x)$ for $x$, obtaining $x = g^{-1}(y)$.
3. Obtain $\frac{dx}{dy}$.
4. The pdf of $Y$ is $f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|$ for $y \in S_Y$.

# Properties
- For non-injective $g$, sum over one-to-one pieces or use the cdf method directly (see [[Random Variable Transformation]]).
- [[Inverse Transform Sampling]] is the special case where $g = F^{-1}$ (the inverse of the target CDF) and $X \sim \mathcal{U}[0,1]$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=71)
