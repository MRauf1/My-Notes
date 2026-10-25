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
- **Summaries.**[^3][^4] The posterior contains all current information about $\theta$; ideally report the whole distribution (graphically in low dimensions). A key advantage of simulation-based Bayesian computation is that summaries of any transformation of $\theta$ come for free. Numerical summaries:
  - Location: mean (the posterior expectation), [[Median]], [[Mode]] (the single "most likely" value given data and model). The mode is often easiest to compute and so central to computational strategies for complex models.
  - Variation: standard deviation, [[Interquartile Range]], other quantiles. The mean and standard deviation are key for normal approximations, often improved by first applying a symmetrizing transformation to $\theta$ (e.g. logit for a probability) ([[Bernstein-von Mises Theorem]]).
  - Uncertainty intervals: [[Credible Interval]], [[Highest Posterior Density Region]].
- On average less variable than the prior ([[Prior and Posterior Moment Relations]]), and centered at a compromise between prior and data that is increasingly dominated by the data ([[Posterior Compromise Between Prior and Data]]).
- Depends on the data only through a [[Sufficient Statistic]]. Updating one observation at a time (each posterior becoming the next prior) gives the same posterior as a single batch update.[^5]
- Under an [[Improper Prior]], the posterior must be checked to be integrable.

[^1]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=C69MVM7Y)
[^2]: [Gelman et al., p. 7](zotero://open-pdf/library/items/HDF44SF4?page=17&annotation=PU6SRI86)
[^3]: [Gelman et al., p. 32](zotero://open-pdf/library/items/HDF44SF4?page=42&annotation=ECA9PBVM); [Gelman et al., p. 33](zotero://open-pdf/library/items/HDF44SF4?page=43&annotation=UTC8DI7P)
[^4]: [Gelman et al., p. 33](zotero://open-pdf/library/items/HDF44SF4?page=43&annotation=ZIFZ7H2X)
[^5]: [Gelman et al., p. 42](zotero://open-pdf/library/items/HDF44SF4?page=52&annotation=LL6W7MPC)
