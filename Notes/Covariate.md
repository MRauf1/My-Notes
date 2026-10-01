---
tags:
  - statistics
  - bayesian_statistics
---

# Definition
> [!info] Covariate[^1]
> An observation on each unit that is not modeled as random. Covariates, or explanatory variables, are labeled $x$, in contrast to the outcomes $y$ whose distribution is modeled.

# Properties
- Information relevant to the outcome should be carried by covariates rather than by unit indexes; then the outcomes can be treated as [[Exchangeability|exchangeable]] conditional on $x$.
- Models are then for $p(y \mid x, \theta)$, as in [[Regression]], where the parameters are regression coefficients.

[^1]: [Gelman et al., p. 5](zotero://open-pdf/library/items/HDF44SF4?page=15&annotation=S3ZVEMDR)
