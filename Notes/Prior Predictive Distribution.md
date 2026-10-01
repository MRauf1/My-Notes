---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Prior Predictive Distribution[^1]
> Before the data are considered, the distribution of the unknown but observable $y$ is
> $$
> \begin{align}
> p(y) = \int p(y, \theta)\, d\theta = \int p(\theta)\, p(y \mid \theta)\, d\theta
> \end{align}
> $$
> It is the [[Marginal Distribution]] of $y$: *prior* because it is not conditioned on any previous observation of the process, *predictive* because it is a distribution for an observable quantity.

# Properties
- It is the [[Data Distribution]] averaged over the [[Prior Distribution]].
- Evaluated at the observed $y$, it is the normalizing constant of the [[Posterior Distribution]] (the marginal likelihood or evidence used in [[Bayesian Occam's Razor]]).
- Counterpart after observing $y$: the posterior [[Predictive Distribution]] $p(\tilde{y} \mid y) = \int p(\tilde{y} \mid \theta)\, p(\theta \mid y)\, d\theta$, which replaces the prior by the posterior.

[^1]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=S5AWPEDZ)
