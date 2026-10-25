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
- It is a [[Mixture Distribution]] of the data model over the prior. Rearranging [[Bayes' Theorem]] gives, for any $\theta$,[^2]
$$
\begin{align}
p(y) = \frac{p(y \mid \theta)\, p(\theta)}{p(\theta \mid y)}
\end{align}
$$
which yields $p(y)$ in closed form whenever prior and posterior densities are known, e.g. with a [[Conjugate Prior]].
- Its moments can be matched to observed data to set [[Hyperparameter|hyperparameters]], a rough stand-in for a [[Hierarchical Model]] ([[Prior Distribution Selection]]).

[^1]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=S5AWPEDZ)
[^2]: [Gelman et al., p. 44](zotero://open-pdf/library/items/HDF44SF4?page=54&annotation=G3EWZFMC)
