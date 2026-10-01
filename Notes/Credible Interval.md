---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Credible Interval[^1]
> A Bayesian (probability) interval $(l, u)$ for an unknown quantity $\theta$ is an interval to which the [[Posterior Distribution]] assigns high probability,
> $$
> \begin{align}
> P(l < \theta < u \mid y) = 1 - \alpha
> \end{align}
> $$
> It can be directly read as having probability $1 - \alpha$ of containing $\theta$, given the observed data.

A frequentist [[Confidence Interval]] may strictly be interpreted only in relation to a sequence of similar inferences in repeated practice. Most users give confidence intervals the common-sense Bayesian reading anyway, which is a primary motivation for Bayesian thinking.[^1]

# Properties
- Randomness sits in $\theta$ (given fixed $y$), whereas in a confidence interval it sits in the endpoints (given fixed $\theta$) ([[Frequentist vs Bayesian Inference]]).
- The shift in applied statistics from hypothesis testing to interval estimation strengthens the case for the Bayesian viewpoint.[^1]
- Under [[Probability Matching Prior|probability matching priors]], credible intervals have exact or approximate frequentist coverage; asymptotically they agree with confidence intervals in regular models ([[Bernstein-von Mises Theorem]]).

[^1]: [Gelman et al., p. 3](zotero://open-pdf/library/items/HDF44SF4?page=13&annotation=T8HRK3GB)
