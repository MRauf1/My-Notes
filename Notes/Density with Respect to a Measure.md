---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Density with Respect to a Measure[^1]
> A probability measure $P$ has density $p$ with respect to a reference [[Measure (Measure Theory)|measure]] $\mu$ when $dP = p\,d\mu$. "The density of this sample" is not a well-defined quantity until the reference measure $\mu$ is named.

In the one-dimensional case, if $Y = g(X)$ for invertible $g$, the densities of $X$ and $Y$ (with respect to the same reference measure) are related by the [[Jacobian Matrix|Jacobian]] of $g^{-1}$:
$$
\begin{align}
p_Y(y) = p_X\big(g^{-1}(y)\big) \left| \frac{dg^{-1}}{dy}(y) \right|
\end{align}
$$
This is the [[Change of Variables|change-of-variables]] formula for densities: one random variable, two descriptions, related by a Jacobian. Every measure conversion in Monte Carlo sampling reduces to this.

# Properties
- A mismatched reference measure is a silent bug in hand-written sampling code: it does not crash, it produces a plausible but wrong answer.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
