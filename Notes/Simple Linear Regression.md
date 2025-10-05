---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 (Simple [[Linear Regression]])
> Given predicted parameters $\hat{\beta}_0, \hat{\beta}_1$, the simple linear regression model is
> $$
> \begin{align}
> \hat{y}_i = \hat{\beta}_0 + \hat{\beta}_1 x
> \end{align}
> $$
> Using the [[Residual Sum of Squares]] as the [[Loss Function]] and minimizing it, the solution is
> $$
> \begin{align}
> \hat{\beta}_1 &= \frac{\sum_{i=1}^n (x_i - \overline{x})(y_i - \overline{y})}{\sum_{i=1}^n (x_i - \overline{x})^2} \\
> \hat{\beta}_0 &= \overline{y} - \hat{\beta}_1 \overline{x}
> \end{align}
> $$
> where $\overline{x}$ is the [[Mean]] of $x_i$.

# Properties

## Coefficient Properties
- [[Simple Linear Regression Coefficient Standard Error]]
- [[Simple Linear Regression Coefficient Confidence Interval]]
- [[Simple Linear Regression Hypothesis Test]]

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=80)