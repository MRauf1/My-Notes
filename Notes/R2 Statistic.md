---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 ($R^2$ Statistic)[^1]
> $$
> \begin{align}
> R^2 = \frac{TSS - RSS}{TSS} = 1 - \frac{RSS}{TSS}
> \end{align}
> $$
> where $RSS$ is the [[Residual Sum of Squares]] and $TSS$ is the [[Total Sum of Squares]].

It is the proportion of [[Variance]] of $Y$ explained by the model that uses $X$. In particular, the numerator is the amount of variability explained by the [[Regression]], while the denominator is the amount of variability inherent in $Y$.

The [[Range]] of the statistic is $[0, 1]$, with the higher score indicating better fit.

In [[Simple Linear Regression]], $R^2 = (Corr[X, Y])^2$ ([[Correlation]]). In [[Multiple Linear Regression]], $R^2 = (Corr[Y, \hat{Y}])^2$. In fact, the linear model maximizes this correlation.

It always increases with more parameters even if the parameter is not statistically significant.

It is a proportionate measure of fit of the model.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=88)