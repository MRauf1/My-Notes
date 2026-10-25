---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Prior and Posterior Moment Relations[^1]
> For any Bayesian model $p(\theta, y)$, applying the [[Law of Total Expectation]] and the [[Law of Total Variance]] with $(\theta, y)$ in place of $(u, v)$ gives
> $$
> \begin{align}
> E(\theta) &= E\big(E(\theta \mid y)\big) \\
> \text{var}(\theta) &= E\big(\text{var}(\theta \mid y)\big) + \text{var}\big(E(\theta \mid y)\big)
> \end{align}
> $$
> where the outer moments are over the [[Prior Predictive Distribution]] of $y$.

- The prior mean is the average of all possible posterior means over the distribution of possible data.
- The posterior variance is **on average** smaller than the prior variance. The reduction is $\text{var}(E(\theta \mid y))$, the variation of posterior means across possible data: the more the data can move the posterior mean, the more they can reduce uncertainty about $\theta$.

# Properties
- These are statements about expectations only. For a particular observed $y$, the posterior variance can be similar to, or even larger than, the prior variance. This usually signals conflict between the [[Data Distribution|sampling model]] and the [[Prior Distribution]].[^1]
- The same identities, conditioned on $y$ and applied to $(\tilde{y}, \theta)$, give the mean and variance of the posterior [[Predictive Distribution]].
- Underlies the general behaviour described in [[Posterior Compromise Between Prior and Data]].

[^1]: [Gelman et al., p. 32](zotero://open-pdf/library/items/HDF44SF4?page=42&annotation=YLMZDPVB)
