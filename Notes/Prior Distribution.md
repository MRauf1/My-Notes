---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Prior Distribution[^1]
> In a Bayesian model for parameters $\theta$ and data $y$, the joint [[Joint Probability Distribution|probability distribution]] factors as
> $$
> \begin{align}
> p(\theta, y) = p(\theta)\, p(y \mid \theta)
> \end{align}
> $$
> The [[Marginal Distribution|marginal]] $p(\theta)$ is the prior distribution: the uncertainty about $\theta$ before the data $y$ are observed.

# Properties
- The second factor $p(y \mid \theta)$ is the [[Data Distribution]]; conditioning the joint on observed $y$ turns the prior into the [[Posterior Distribution]] via [[Bayes' Theorem]].
- Averaging the data distribution over the prior gives the [[Prior Predictive Distribution]].
- Under the [[Probability Bayesian Framework]], the prior encodes the state of knowledge about $\theta$ as a probability distribution.
- How to choose it: [[Prior Distribution Selection]], [[Conjugate Prior]], [[Probability Matching Prior]].

[^1]: [Gelman et al., p. 6](zotero://open-pdf/library/items/HDF44SF4?page=16&annotation=BF4BS4G6)
