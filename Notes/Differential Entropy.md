---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Differential Entropy[^1]
> For a density $p(\mathbf{x})$ over continuous variables,
> $$
> \begin{align}
> \mathrm{H}[\mathbf{x}] = -\int p(\mathbf{x}) \ln p(\mathbf{x})\,d\mathbf{x}
> \end{align}
> $$

**Relation to discrete entropy.** Discretizing $x$ into bins of width $\Delta$ gives the discrete [[Entropy]] $-\sum_i p(x_i)\Delta \ln p(x_i) - \ln\Delta$. As $\Delta \to 0$ the first term tends to the differential entropy, so the two differ by $-\ln\Delta$, which diverges: specifying a continuous variable very precisely requires a large number of bits.[^1]

> [!abstract] The Gaussian Maximizes Differential Entropy[^2][^3]
> Among all densities on $\mathbb{R}$ with fixed mean $\mu$ and variance $\sigma^2$, the differential entropy is maximized (using Lagrange multipliers for normalization, mean, and variance) by the [[Normal Distribution|Gaussian]]
> $$
> \begin{align}
> p(x) = \frac{1}{(2\pi\sigma^2)^{1/2}}\exp\left\{-\frac{(x - \mu)^2}{2\sigma^2}\right\}, \qquad \mathrm{H}[x] = \frac{1}{2}\left\{1 + \ln(2\pi\sigma^2)\right\}
> \end{align}
> $$
> More generally, among densities on $\mathbb{R}^D$ with fixed covariance $\boldsymbol{\Sigma}$, the maximizer is the [[Multivariate Normal Distribution|multivariate Gaussian]], with $\mathrm{H}[\mathbf{x}] = \frac{1}{2}\ln\left|2\pi e\,\boldsymbol{\Sigma}\right|$.

# Properties
- Non-negativity was not imposed as a constraint in the maximization; the resulting Gaussian is non-negative anyway, so the constraint is unnecessary in hindsight.[^2]
- Unlike discrete entropy, differential entropy can be negative: the Gaussian's is negative for $\sigma^2 < 1/(2\pi e)$.[^3]
- It increases as the distribution broadens (increasing $\sigma^2$).
- Not invariant under a change of variables: $\mathbf{y} = \mathbf{A}\mathbf{x}$ gives $\mathrm{H}[\mathbf{y}] = \mathrm{H}[\mathbf{x}] + \ln|\det\mathbf{A}|$. Differences of differential entropies, such as [[Kullback-Leibler Divergence]] and [[Mutual Information]], are invariant.
- [[Conditional Entropy]] extends it to conditional densities.

[^1]: [Bishop, 2006, p. 53](zotero://open-pdf/library/items/5G99AZ8U?page=73&annotation=XJL32KWI)
[^2]: [Bishop, 2006, p. 54](zotero://open-pdf/library/items/5G99AZ8U?page=74&annotation=AINS2FC6)
[^3]: [Bishop, 2006, p. 54](zotero://open-pdf/library/items/5G99AZ8U?page=74&annotation=MLKPPZTC)
