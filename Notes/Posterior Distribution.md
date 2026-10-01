---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Posterior Distribution[^1]
> Conditioning the joint model $p(\theta, y) = p(\theta)\,p(y \mid \theta)$ on the observed data $y$ via [[Bayes' Theorem]] gives the posterior density
> $$
> \begin{align}
> p(\theta \mid y) = \frac{p(\theta, y)}{p(y)} = \frac{p(\theta)\, p(y \mid \theta)}{p(y)}, \qquad p(y) = \sum_\theta p(\theta)\, p(y \mid \theta) \quad \text{or} \quad p(y) = \int p(\theta)\, p(y \mid \theta)\, d\theta
> \end{align}
> $$
> with the sum over all values of a discrete $\theta$ and the integral for a continuous $\theta$.

> [!info] Unnormalized Posterior Density[^1]
> Since $p(y)$ does not depend on $\theta$, for fixed $y$ it is a constant, and
> $$
> \begin{align}
> p(\theta \mid y) \propto p(\theta)\, p(y \mid \theta)
> \end{align}
> $$
> The right side is the unnormalized posterior density, with $p(y \mid \theta)$ read as a function of $\theta$, not of $y$.

# Properties
- Technical core of [[Bayesian Inference]]: develop the model $p(\theta, y)$, then compute summaries of $p(\theta \mid y)$.[^1]
- The data enter only through the [[Likelihood Function]] $p(y \mid \theta)$ ([[Likelihood Principle]]).[^2]
- The normalizer $p(y)$ is the [[Prior Predictive Distribution]] evaluated at the observed data; when it is intractable, the unnormalized form is sampled with [[Markov Chain Monte Carlo]].
- Ratios of the posterior at two points need no normalizer: [[Posterior Odds]].
- Averaging the data model over it gives the posterior [[Predictive Distribution]]; interval summaries of it are [[Credible Interval|credible intervals]]; point summaries are [[Bayes Estimator|Bayes estimators]] or the [[Maximum a Posteriori Learning|MAP]] estimate.

[^1]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=C69MVM7Y)
[^2]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=PU6SRI86)
