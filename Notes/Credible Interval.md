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

> [!info] Central Posterior Interval[^2]
> The $100(1-\alpha)\%$ central posterior interval is the range between the posterior $\alpha/2$ and $1 - \alpha/2$ quantiles, so exactly $100(\alpha/2)\%$ of the posterior probability lies above and below it. Such interval estimates are called posterior intervals.

**Comparison with a confidence interval.**[^4]

| | [[Confidence Interval]] | Credible (posterior) interval |
|---|---|---|
| Framework | Frequentist | Bayesian |
| Parameter | Fixed, unknown constant | Random variable with a distribution |
| Interval | Random (varies over repeated samples) | Fixed once data and prior are given |
| What is conditioned on | $\theta$ | Observed data $y$ |
| Meaning of "95%" | Long-run success rate of the procedure: ~95% of intervals from repeated experiments capture $\theta$; no probability statement about one computed interval | Direct: given prior and data, $P(\theta \in \text{interval} \mid y) = 0.95$ |
| Prior information | Not used | Combined with the likelihood via [[Bayes' Theorem]] |

# Types
- Central posterior interval (above), also called the equal-tailed interval (ETI): the common choice in practice, being a direct pair of quantiles computable from posterior simulations.[^3]
- [[Highest Posterior Density Region]]: the region of probability $1-\alpha$ where the density is never lower than outside; coincides with the central interval for unimodal symmetric posteriors and can differ substantially for skewed ones.

# Properties
- It is nearly always important to report posterior uncertainty, not just point summaries: quantiles of the posterior of estimands of interest, or an interval summary.[^2]
- Randomness sits in $\theta$ (given fixed $y$), whereas in a confidence interval it sits in the endpoints (given fixed $\theta$) ([[Frequentist vs Bayesian Inference]]).
- The shift in applied statistics from hypothesis testing to interval estimation strengthens the case for the Bayesian viewpoint.[^1]
- Under [[Probability Matching Prior|probability matching priors]], credible intervals have exact or approximate frequentist coverage; asymptotically they agree with confidence intervals in regular models ([[Bernstein-von Mises Theorem]]).

[^1]: [Gelman et al., p. 3](zotero://open-pdf/library/items/HDF44SF4?page=13&annotation=T8HRK3GB)
[^2]: [Gelman et al., p. 33](zotero://open-pdf/library/items/HDF44SF4?page=43&annotation=FK747TRJ)
[^3]: [Gelman et al., p. 33](zotero://open-pdf/library/items/HDF44SF4?page=43&annotation=ZLLGPFN5)
[^4]: Supplementary notes provided by the creator.
