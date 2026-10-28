---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Marginal Posterior Distribution[^1][^2]
> For $\theta = (\theta_1, \theta_2)$ with $\theta_1$ of interest and $\theta_2$ a [[Nuisance Parameter]], the marginal posterior of $\theta_1$ is obtained from the joint [[Posterior Distribution]] $p(\theta_1, \theta_2 \mid y) \propto p(y \mid \theta_1, \theta_2)\, p(\theta_1, \theta_2)$ by integrating out $\theta_2$:
> $$
> \begin{align}
> p(\theta_1 \mid y) = \int p(\theta_1, \theta_2 \mid y)\, d\theta_2
> \end{align}
> $$

> [!abstract] Mixture Form[^3]
> Factoring the joint posterior gives
> $$
> \begin{align}
> p(\theta_1 \mid y) = \int p(\theta_1 \mid \theta_2, y)\, p(\theta_2 \mid y)\, d\theta_2
> \end{align}
> $$
> a [[Mixture Distribution]] of the conditional posteriors $p(\theta_1 \mid \theta_2, y)$, with the marginal posterior $p(\theta_2 \mid y)$ as weighting function. The weights combine evidence from data and prior.

The ultimate aim of a multiparameter Bayesian analysis is usually the marginal posterior of the few parameters of interest: first obtain the joint posterior of all unknowns, then integrate over the rest.[^1]

# Properties
- **Simulation replaces integration.**[^1] Given draws from the joint posterior, keeping only the $\theta_1$ coordinates and ignoring $\theta_2$ yields draws from $p(\theta_1 \mid y)$.
- **Marginal and conditional simulation.**[^4] The mixture form is rarely evaluated explicitly but gives a practical scheme: draw $\theta_2 \sim p(\theta_2 \mid y)$, then $\theta_1 \sim p(\theta_1 \mid \theta_2, y)$. The pair is a joint posterior draw, so the integral is performed indirectly. This is two-stage [[Ancestral Sampling]] on the posterior, and the same scheme as sampling a [[Mixture Distribution]]. It is the basis for constructing and computing with multiparameter and [[Hierarchical Model|hierarchical]] models ([[Bayesian Posterior Simulation Strategy]]).
- It is the [[Marginal Distribution]] of the joint posterior; nuisance uncertainty widens it relative to the conditional posterior at a fixed $\theta_2$ ([[Law of Total Variance]]).
- The posterior [[Predictive Distribution]] has the same mixture structure, averaging over all parameters, e.g. $p(\tilde{y} \mid y) = \iint p(\tilde{y} \mid \mu, \sigma^2, y)\, p(\mu, \sigma^2 \mid y)\, d\mu\, d\sigma^2$.[^5]

[^1]: [Gelman et al., p. 63](zotero://open-pdf/library/items/HDF44SF4?page=73&annotation=C4DD4PTM)
[^2]: [Gelman et al., p. 63](zotero://open-pdf/library/items/HDF44SF4?page=73&annotation=H78MLHQF)
[^3]: [Gelman et al., p. 64](zotero://open-pdf/library/items/HDF44SF4?page=74&annotation=VJBCXDLJ)
[^4]: [Gelman et al., p. 64](zotero://open-pdf/library/items/HDF44SF4?page=74&annotation=5F798C6T)
[^5]: [Gelman et al., p. 66](zotero://open-pdf/library/items/HDF44SF4?page=76&annotation=K27Y3WQ3)
