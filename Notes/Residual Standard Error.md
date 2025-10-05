---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 (Residual [[Standard Error]])[^1]
> In a task like [[Linear Regression]] where $\sigma^2 = Var[\epsilon]$ is not known, it can be estimated using the residual standard error, which is
> $$
> \begin{align}
> \sigma \approx RSE = \sqrt{RSS/(n - p - 1)}
> \end{align}
> $$
> where $p$ is the number of parameters.

It is the estimate of the [[Standard Deviation]] of $\epsilon$. In [[Linear Regression]], roughly speaking, it is the average amount that the predicted output will deviate from the true regression line.

It is considered an absolute measure of the lack of fit of the model.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=84)