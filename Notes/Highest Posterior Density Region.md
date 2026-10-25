---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Highest Posterior Density Region[^1]
> A $100(1-\alpha)\%$ highest posterior density (HPD) region is a set $R$ such that
> $$
> \begin{align}
> P(\theta \in R \mid y) = 1 - \alpha \quad \text{and} \quad p(\theta_1 \mid y) \geq p(\theta_2 \mid y) \ \text{for all } \theta_1 \in R,\ \theta_2 \notin R
> \end{align}
> $$
> i.e. the density inside the region is never lower than outside. Equivalently, $R = \{\theta : p(\theta \mid y) \geq k_\alpha\}$ for the largest $k_\alpha$ achieving probability $1 - \alpha$.

# Properties
- An alternative to the central posterior interval ([[Credible Interval]]); the two coincide when the [[Posterior Distribution]] is unimodal and symmetric.[^1]
- They can differ substantially when the posterior is highly skewed.[^2] For a multimodal posterior the HPD region can be a union of disjoint intervals.
- Among all regions with probability $1-\alpha$, the HPD region has the smallest volume.
- Not invariant under reparameterization (densities change by a Jacobian, [[Change of Variables]]), whereas central intervals are, since quantiles transform monotonically.
- The central interval is more common in practice: it has a direct interpretation as the posterior $\alpha/2$ and $1-\alpha/2$ quantiles and is directly computed from posterior simulations.[^1]

[^1]: [Gelman et al., p. 33](zotero://open-pdf/library/items/HDF44SF4?page=43&annotation=ZLLGPFN5)
[^2]: [Gelman et al., p. 34](zotero://open-pdf/library/items/HDF44SF4?page=44&annotation=4RYJ6RKB)
