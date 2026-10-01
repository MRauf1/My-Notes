---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Geometric Standard Deviation[^1]
> For a positive [[Random Variable]] $\theta$,
> $$
> \begin{align}
> \mathrm{GSD}(\theta) = \exp\big(\mathrm{sd}[\log \theta]\big)
> \end{align}
> $$

# Properties
- The [[Standard Deviation]] on the log scale, mapped back by $\exp$; paired with the [[Geometric Mean]] $\exp(E[\log \theta])$.
- It is a multiplicative factor ($\geq 1$): spread is described as "times or divided by" the GSD rather than "plus or minus".
- Dimensionless and invariant to rescaling, like the [[Coefficient of Variation]].

[^1]: [Gelman et al., p. 6](zotero://open-pdf/library/items/HDF44SF4?page=16&annotation=3BPERD6Z)
