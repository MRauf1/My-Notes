---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] QQ Transformation[^1]
> Let $F$ be a continuous [[Cumulative Distribution Function|CDF]] and $G$ any CDF, with $G^{-1}$ its generalized inverse ([[Quantile Function]]). If $X \sim F$, then
> $$
> \begin{align}
> Y = G^{-1}(F(X)) \sim G
> \end{align}
> $$
> because $F(X) \sim \mathcal{U}(0,1)$. The map $G^{-1} \circ F$ is the QQ transformation: it sends each quantile of $F$ to the corresponding quantile of $G$.

It composes the [[Probability Integral Transform]] with [[Inverse Transform Sampling]], and sometimes $G^{-1} \circ F$ is simpler than either factor, so one can go from $X \sim F$ to $Y \sim G$ without passing through a uniform. The location-scale map $Y = \mu + \sigma Z$ ($\sigma > 0$) taking $Z \sim \mathcal{N}(0,1)$ to $Y \sim \mathcal{N}(\mu, \sigma^2)$ is a QQ transformation used without thinking of inversion.

# Properties
- Requires $F$ continuous: if $F$ is discrete and $X = F^{-1}(U)$, then $F(X)$ is not $\mathcal{U}(0,1)$, so the construction fails in general.[^2]
- It is monotone non-decreasing, so it preserves the ranks of the inputs; this is what makes it useful with [[Common Random Numbers]].
- The [[Array Sampling Method]] with a sorted array is a QQ transformation of a discrete uniform index.
- Inverse transform sampling is the special case $F = \mathcal{U}(0,1)$, i.e. $F(x) = x$ on $(0,1)$.

[^1]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=6&annotation=2HYQFJJR)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=6&annotation=YLBZU82T)
