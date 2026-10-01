---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Hierarchical Model[^1]
> A model, also called a multilevel model, used when information is available on several different levels of observational units. In the two-level case, units $i$ are nested in groups $j$ with
> $$
> \begin{align}
> y_{ij} \mid \theta_j &\sim p(y \mid \theta_j) \\
> \theta_j \mid \phi &\sim p(\theta \mid \phi) \\
> \phi &\sim p(\phi)
> \end{align}
> $$
> where the group parameters $\theta_j$ share a [[Prior Distribution]] governed by [[Hyperparameter|hyperparameters]] $\phi$.

# Properties
- [[Exchangeability]] can be stated at each level of units: units within a group, and groups among themselves.[^1]
- The group-level structure is the exchangeability-to-iid-mixture representation applied to the $\theta_j$.

[^1]: [Gelman et al., p. 5](zotero://open-pdf/library/items/HDF44SF4?page=15&annotation=HJL44P8P)
