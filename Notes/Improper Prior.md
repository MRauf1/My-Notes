---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Proper and Improper Prior[^1]
> A prior density $p(\theta)$ is **proper** if it does not depend on the data and integrates to $1$. If $\int p(\theta)\, d\theta$ is a positive finite value, $p$ is an unnormalized density and can be renormalized. If $\int p(\theta)\, d\theta = \infty$ (e.g. $p(\theta) \propto 1$ on $\mathbb{R}$), the prior is **improper**.

An improper prior does not combine with the likelihood into a proper joint model $p(y, \theta)$. One can still formally define the unnormalized posterior[^2]
$$
\begin{align}
p(\theta \mid y) \propto p(y \mid \theta)\, p(\theta)
\end{align}
$$
and use it whenever it is integrable.

# Properties
- The resulting [[Posterior Distribution]] is often proper (e.g. given at least one data point), but **not always**. One must always check that $\int p(\theta \mid y)\, d\theta < \infty$ for all $y$ and that the posterior has a sensible form.[^2]
- Most reasonable interpretation: an approximation in situations where the likelihood dominates the prior.[^2]
- Arise naturally as [[Noninformative Prior|noninformative priors]] (flat priors on location parameters, $1/\theta$ on scale parameters, [[Jeffreys Prior]]).
- Can lead to improper posteriors in practice, e.g. a uniform prior on the logarithm of a hierarchical variance parameter ([[Hierarchical Model]]).[^3]
- Cause further difficulties when averaging over competing models: the [[Prior Predictive Distribution|marginal likelihood]] is defined only up to an arbitrary constant.[^4]

[^1]: [Gelman et al., p. 52](zotero://open-pdf/library/items/HDF44SF4?page=62&annotation=RUV8CAGG)
[^2]: [Gelman et al., p. 52](zotero://open-pdf/library/items/HDF44SF4?page=62&annotation=9Z9GTD3T)
[^3]: [Gelman et al., p. 54](zotero://open-pdf/library/items/HDF44SF4?page=64&annotation=3SUJ9DYU)
[^4]: [Gelman et al., p. 54](zotero://open-pdf/library/items/HDF44SF4?page=64&annotation=TBM6RC9R)
