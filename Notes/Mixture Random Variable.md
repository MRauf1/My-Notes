---
tags:
  - statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Mixture [[Random Variable]])[^1]
> [[Random Variable]] that is neither [[Discrete Random Variable]] nor [[Continuous Random Variable]]: its [[Cumulative Distribution Function]] is not continuous, nor is it a step function.

A typical mixture cdf has the form $F = \alpha F_d + (1 - \alpha) F_c$ with $0 < \alpha < 1$, $F_d$ a discrete (step) cdf and $F_c$ a continuous cdf; probability is split between point masses and a density (e.g. a censored measurement that equals a threshold with positive probability).

# Properties
- If $F_d$ is a discrete CDF, $F_c$ a continuous one and $0 < \lambda < 1$, then $\lambda F_d + (1 - \lambda)F_c$ is the CDF of a distribution with atoms from $F_d$ and density from $F_c$; it can still be sampled by [[Inverse Transform Sampling]] with the generalized inverse.[^2]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=72)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=4&annotation=JQL8XJYZ)
