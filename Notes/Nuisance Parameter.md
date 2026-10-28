---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Nuisance Parameter[^1][^2]
> An unknown parameter needed to build a realistic model but not itself of inferential interest. Writing the parameter vector as $\theta = (\theta_1, \theta_2)$ (each part possibly a vector) with interest only in $\theta_1$, the component $\theta_2$ is a nuisance parameter. Bayesian inference removes it by marginalization, reporting the [[Marginal Posterior Distribution]]
> $$
> \begin{align}
> p(\theta_1 \mid y) = \int p(\theta_1, \theta_2 \mid y)\, d\theta_2
> \end{align}
> $$

# Properties
- Classic example: the scale $\sigma^2$ of the random errors in a measurement problem, when only the location $\mu$ is of interest ([[Scale Parameter]]).[^1]
- Bayesian treatment averages over $\theta_2$, weighting each value by its posterior $p(\theta_2 \mid y)$, so its uncertainty propagates into inference on $\theta_1$; with simulation, draws of $\theta_2$ are simply ignored ([[Marginal Posterior Distribution]]).
- Frequentist counterparts eliminate it by maximization ([[Profile Likelihood Confidence Interval|profile likelihood]]) or by a [[Pivotal Quantity]] whose distribution does not depend on it.[^3]

[^1]: [Gelman et al., p. 63](zotero://open-pdf/library/items/HDF44SF4?page=73&annotation=C4DD4PTM)
[^2]: [Gelman et al., p. 63](zotero://open-pdf/library/items/HDF44SF4?page=73&annotation=P9R6RI8P)
[^3]: [Gelman et al., p. 66](zotero://open-pdf/library/items/HDF44SF4?page=76&annotation=6JZI6GYL)
