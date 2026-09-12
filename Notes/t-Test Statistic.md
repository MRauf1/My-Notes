---
tags:
  - statistics
  - statistical_learning
---

# Definition

> [!info] Definition 1 ([[t-Test]] Statistic)[^1]
> For an estimated parameter $\hat{\mu}$ with the [[Null Hypothesis]] $H_0: \mu = a$, the t-test statistic is
> $$
> \begin{align}
> t = \frac{\hat{\mu} - a}{SE(\hat{\mu})} \sim t(n-p)
> \end{align}
> $$
> where $p$ is the number of parameters estimated to obtain $\hat{\mu}$ (e.g. $p = 2$ for [[Simple Linear Regression]]'s slope/intercept).

Measures the number of [[Standard Deviation]] that the estimated parameter is away from the value we are testing.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=86)