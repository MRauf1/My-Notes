---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Multivariate Probability Distribution]] [[Discrete]])
> [[Multivariate Probability Distribution]] where the [[Random Variable]] are [[Discrete]].
> $$
> \begin{align}
> P(X_1 = x_1, \dots, X_n = x_n) = f(x_1, \dots, x_n)
> \end{align}
> $$

> [!info] Definition 2 (Discrete Random Vector and Joint PMF)[^1]
> A [[Random Vector]] $(X_1, X_2)$ is discrete if its space $\mathcal{D}$ is finite or [[Countable Set|countable]]; then $X_1$ and $X_2$ are both [[Discrete Random Variable|discrete]]. Its joint probability mass function is
> $$
> \begin{align}
> p_{X_1, X_2}(x_1, x_2) = P[X_1 = x_1, X_2 = x_2], \quad (x_1, x_2) \in \mathcal{D}
> \end{align}
> $$
> and for an event $B \subseteq \mathcal{D}$,
> $$
> \begin{align}
> P[(X_1, X_2) \in B] = \sum\sum_{B} p_{X_1, X_2}(x_1, x_2)
> \end{align}
> $$

For $n$ variables, $X_1, \dots, X_n$ are of the discrete type if the [[Joint Cumulative Distribution Function|joint cdf]] can be written $F_{\mathbf{X}}(\mathbf{x}) = \sum \cdots \sum_{w_1 \leq x_1, \dots, w_n \leq x_n} p(w_1, \dots, w_n)$. A point function $p$ is essentially a joint pmf if it is nonnegative for all real arguments and sums to $1$ over them.[^2]

The joint pmf uniquely determines the [[Joint Cumulative Distribution Function]]. By convention it is extended by zero outside $\mathcal{D}$, so $\sum\sum_{\mathcal{D}}$ can be written $\sum_{x_2}\sum_{x_1}$.

# Properties
## Definitional Properties
- [[Multivariate Discrete Probability Distribution Definitional Properties]]: $0 \leq p_{X_1, X_2}(x_1, x_2) \leq 1$ and $\sum\sum_{\mathcal{D}} p_{X_1, X_2}(x_1, x_2) = 1$, which characterize joint pmfs.

## Other
- Its support is the set of points with $p(x_1, x_2) > 0$ ([[Random Variable Support]]).
- The [[Marginal Distribution|marginal pmfs]] are row and column sums of the joint pmf table.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=102)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=150)
