---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Poisson Distribution]] [[Addition]])[^1]
> Consider a sum of [[Independent Random Variable|independent]] [[Poisson Distribution|Poisson RVs]] $X_i$ with parameters $\mu_i$. Then $X = \sum_{i} X_i$ has a [[Poisson Distribution]] with parameter $\mu = \sum_{i} \mu_i$.

Proof: by the [[Moment Generating Function Technique]], $\prod_i e^{\mu_i(e^t - 1)} = e^{(\sum_i \mu_i)(e^t - 1)}$. In a [[Poisson Process]], merging independent streams of events adds their rates.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=187)
