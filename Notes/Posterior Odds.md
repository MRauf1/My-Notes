---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Posterior Odds[^1]
> The ratio of the [[Posterior Distribution|posterior density]] at two points $\theta_1, \theta_2$ under a given model, $p(\theta_1 \mid y) / p(\theta_2 \mid y)$, is the posterior odds for $\theta_1$ compared to $\theta_2$. By [[Bayes' Theorem]], the normalizer $p(y)$ cancels:
> $$
> \begin{align}
> \frac{p(\theta_1 \mid y)}{p(\theta_2 \mid y)} = \frac{p(\theta_1)\, p(y \mid \theta_1) / p(y)}{p(\theta_2)\, p(y \mid \theta_2) / p(y)} = \frac{p(\theta_1)}{p(\theta_2)} \cdot \frac{p(y \mid \theta_1)}{p(y \mid \theta_2)}
> \end{align}
> $$
> Posterior odds = prior odds $\times$ likelihood ratio $p(y \mid \theta_1)/p(y \mid \theta_2)$.

# Properties
- Most familiar with a discrete parameter and $\theta_2$ the complement of $\theta_1$, where it reduces to the [[Odds]] $p/(1-p)$ of the posterior probability.
- [[Odds]] give an alternative representation of probabilities in which Bayes' rule becomes a single multiplication.
- Only the unnormalized posterior is needed, so it is computable even when $p(y)$ is not.
- The likelihood ratio is the same quantity that drives the [[Likelihood Ratio Test]]; the Bayesian version weights it by prior odds.

[^1]: [Gelman et al., p. 8](zotero://open-pdf/library/items/HDF44SF4?page=18&annotation=QQCD4Q7J)
