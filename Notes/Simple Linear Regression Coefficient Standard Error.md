---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 ([[Simple Linear Regression]] Coefficient [[Standard Error]])[^1]
> The standard errors of the estimated coefficients $\hat{\beta}_0, \hat{\beta}_1$ are
> $$
> \begin{align}
> SE(\hat{\beta}_0)^2 &= \sigma^2 [\frac{1}{n} + \frac{\overline{x}^2}{\sum_{i=1}^n (x_i - \overline{x})^2}] \\
> SE(\hat{\beta}_1)^2 &= \frac{\sigma^2}{\sum_{i=1}^n (x_i - \overline{x})^2}
> \end{align}
> $$
> where $\sigma^2 = Var[\epsilon]$.

$SE(\hat{\beta}_0)$ would be the same as $SE(\hat{\mu})$ from [[Standard Error]] if $\overline{x} = 0$.

$SE(\hat{\beta}_1)$ is smaller when $x_i$ are more spread out - intuitively, we have more leverage to estimate a slope when this is the case.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=84)