---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Standard Gumbel Distribution[^1]
> The standard Gumbel distribution has [[Cumulative Distribution Function|CDF]]
> $$
> \begin{align}
> F(x) = \exp\!\left(-e^{-x}\right), \quad x \in \mathbb{R}
> \end{align}
> $$

# Properties
- If $E \sim$ [[Exponential Distribution|Exp]]$(1)$, then $G = -\log E$ is standard Gumbel, since $P(-\log E \leq x) = P(E \geq e^{-x}) = \exp(-e^{-x})$; equivalently $G = -\log(-\log U)$ for $U \sim \mathcal{U}(0,1)$ ([[Inverse Transform Sampling]]).
- Used in the [[Gumbel-Max Trick]] for sampling discrete distributions from unnormalized log-weights.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=21&annotation=SRMUKQYD)
