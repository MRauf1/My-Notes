---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Data Distribution[^1]
> In a Bayesian model with joint distribution $p(\theta, y) = p(\theta)\, p(y \mid \theta)$, the [[Conditional Distribution]] $p(y \mid \theta)$ of the data given the parameters is the data distribution, also called the sampling distribution.

Bayesian usage of "sampling distribution" differs from the frequentist one, where it means the distribution of a [[Statistic]] over repeated samples.

# Properties
- Viewed as a function of $\theta$ for the fixed observed $y$, it is the [[Likelihood Function]]. The data affect the [[Posterior Distribution]] only through this function, which is why Bayesian inference obeys the [[Likelihood Principle]].[^2]
- Paired with the [[Prior Distribution]] $p(\theta)$ it gives the full probability model of [[Bayesian Inference]].
- For [[Exchangeability|exchangeable]] data it is commonly taken [[Independent and Identically Distributed|iid]]: $p(y \mid \theta) = \prod_{i=1}^n p(y_i \mid \theta)$.[^3]

[^1]: [Gelman et al., p. 6](zotero://open-pdf/library/items/HDF44SF4?page=16&annotation=BF4BS4G6)
[^2]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=PU6SRI86)
[^3]: [Gelman et al., p. 5](zotero://open-pdf/library/items/HDF44SF4?page=15&annotation=A2JKB3D2)
