---
tags:
  - statistics
  - statistical_learning
---

# Definition

> [!info] Definition 1 ([[Simple Linear Regression]] Coefficient [[Confidence Interval]])[^1]
> For simple linear regression, the $(1 - \alpha)100\%$ confidence intervals for the estimated parameters are
> $$
> \begin{align}
> \hat{\beta}_0 &\pm t_{\alpha / 2, n-2} \cdot SE(\hat{\beta}_0) \\
> \hat{\beta}_1 &\pm t_{\alpha / 2, n-2} \cdot SE(\hat{\beta}_1)
> \end{align}
> $$

Uses the [[t-Distribution|t-score]] with $n - 2$ degrees of freedom, not the $z$-score, since the error variance is estimated from the data rather than known.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=84)