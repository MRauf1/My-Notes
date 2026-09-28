---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Cumulative Function|Cumulative]] Distribution Function)[^1][^2]
> For a [[Random Variable]] $X$, its cdf is
> $$
> \begin{align}
> F_X(x) = P_X((-\infty, x]) = P(\{c \in \mathcal{C} : X(c) \leq x\}) = P(X \leq x), \quad x \in \mathbb{R}
> \end{align}
> $$

Every random variable has a cdf, and it determines the distribution completely. How it relates to the pmf or pdf depends on the type of $X$:
- Discrete: $F_X$ is a step function, and the [[Probability Mass Function]] is the jump size, $p_X(x) = F_X(x) - F_X(x^-)$.
- Absolutely continuous: $F_X(x) = \int_{-\infty}^x f_X(t)\,dt$, and $F_X'(x) = f_X(x)$ at every $x$ where the [[Probability Density Function]] $f_X$ is continuous.
- [[Mixture Random Variable|Mixture]]: $F_X$ has jumps but is not a step function.

# Properties
- [[Cumulative Distribution Function Basic Properties]]
- [[Random Variables Equal in Distribution]]
- Its (generalized) inverse is the [[Quantile Function]].
- Multivariate version: [[Joint Cumulative Distribution Function]].

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=19)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=55)
