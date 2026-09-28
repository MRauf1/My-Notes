---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Random Variable]] [[Function Transformation|Transformation]])[^1]
> Given a random variable $X$ with known distribution and a [[Function]] $g$, the transformed random variable is $Y = g(X)$, i.e. $Y(c) = g(X(c))$. The problem is to find the distribution of $Y$. If $X$ has space $\mathcal{D}_X$, then $Y$ has space $\mathcal{D}_Y = \{g(x) : x \in \mathcal{D}_X\}$.

> [!abstract] Theorem 1 (Discrete Transformation, General Rule)[^1]
> For a [[Discrete Random Variable]] $X$ with pmf $p_X$ and any $g$,
> $$
> \begin{align}
> p_Y(y) = P[g(X) = y] = \sum_{x \in \mathcal{D}_X : g(x) = y} p_X(x), \quad y \in \mathcal{D}_Y
> \end{align}
> $$
> If $g$ is [[Injective Function|one-to-one]], the sum has a single term: $p_Y(y) = p_X(g^{-1}(y))$.

Hogg et al. say that for non-one-to-one $g$ there is no overall rule, but there is: Theorem 1 always holds, since $\{g(X) = y\}$ is the [[Disjoint Set Union|disjoint union]] of the events $\{X = x\}$ over the preimage $g^{-1}(\{y\})$. What lacks a single formula is computing that preimage, which depends on $g$. The practical recipe is: list the points of $\mathcal{D}_Y$, and for each $y$ collect the $x$ values mapping to it and add their probabilities.

# Techniques
- **Pmf (preimage) method**, discrete case: Theorem 1.
- **Cdf method**, any case: compute $F_Y(y) = P(g(X) \leq y) = P(X \in \{x : g(x) \leq y\})$ directly, then differentiate for a pdf. It handles non-monotone $g$ by splitting the set $\{x : g(x) \leq y\}$ into intervals (e.g. for $Y = X^2$, $F_Y(y) = F_X(\sqrt{y}) - F_X\big((-\sqrt{y})^-\big)$ for $y \geq 0$).
- **Change-of-variable (Jacobian) method**, continuous one-to-one $g$: [[Cumulative Distribution Function Transformation Technique]], $f_Y(y) = f_X(g^{-1}(y)) \left|\frac{dx}{dy}\right|$.
- **Piecewise one-to-one extension**, continuous case: if the support of $X$ splits into pieces $A_1, \dots, A_m$ on each of which $g$ is one-to-one and differentiable, then $f_Y(y) = \sum_{i} f_X(g_i^{-1}(y)) \left|\frac{d}{dy} g_i^{-1}(y)\right|$, summed over the pieces whose image contains $y$; this is the continuous counterpart of Theorem 1.
- **Mgf method**: compute $M_Y(t) = E[e^{t g(X)}]$ and recognize it, using the [[Moment Generating Function Equal Distribution Theorem]]. Most useful for sums of [[Independent Random Variable|independent]] variables.
- [[Inverse Transform Sampling]] is the special case where the transformation is an inverse cdf applied to a uniform variable.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=63)
