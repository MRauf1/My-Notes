---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Difference of Proportions]] [[Confidence Interval]])
> Approximate $(1 - \alpha)100\%$ CI is
> $$
> \begin{align}
> \hat{p_1} - \hat{p_2} \pm z_{\alpha/2} \sqrt{\frac{\hat{p_1} (1 - \hat{p_1})}{n_1} + \frac{\hat{p_2} (1 - \hat{p_2})}{n_2}}
> \end{align}
> $$
> If the CI includes $0$, the data are consistent with $p_1 = p_2$ at level $\alpha$ (in a $2 \times 2$ table, with independence of the row and column variables); it does not prove equality, since a failure to reject is not evidence for $H_0$.

It is the [[Two-Sample Confidence Interval for Difference of Means|large-sample two-sample interval]] applied to [[Bernoulli Distribution|Bernoulli]] samples $b(1, p_1)$ and $b(1, p_2)$, with sample proportions $\hat{p}_1 = \bar{X}$, $\hat{p}_2 = \bar{Y}$ and the variances $p_i(1 - p_i)$ estimated by $\hat{p}_i(1 - \hat{p}_i)$.[^1]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=260)
