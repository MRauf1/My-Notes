---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Precision (Statistics)[^1]
> The inverse of the variance of a distribution, $1/\sigma^2$ (for a random vector, the inverse [[Covariance Matrix]]).

It plays a prominent role in manipulating normal distributions, because combining Gaussian sources of information adds precisions rather than variances.

# Properties
- **Precisions add under Gaussian conditioning.** For normal data and a normal prior with known precisions, the posterior precision equals the prior precision plus the data precision ([[Posterior Compromise Between Prior and Data]]):[^1]
$$
\begin{align}
\frac{1}{\tau_n^2} = \frac{1}{\tau_0^2} + \frac{n}{\sigma^2}
\end{align}
$$
- The posterior mean is the precision-weighted average of the prior mean and the data.
- Distinct from [[Precision]] in numerical analysis (number of digits).

[^1]: [Gelman et al., p. 40](zotero://open-pdf/library/items/HDF44SF4?page=50&annotation=QULYUGVQ)
