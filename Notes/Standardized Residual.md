---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Generalized Linear Model]] Standardized Residual)
> Given $\hat{\mu}_i =$ MLE of $E[Y_i]$, the standardized residuals are
> $$
> \begin{align}
> r_i = \frac{y_i - \hat{\mu}_i}{\sqrt{v(\hat{\mu}_i)} (1 - \hat{h}_i)} = \frac{e_i}{\sqrt{1 - \hat{h}_i}}
> \end{align}
> $$
> where $v(\mu) = Var[Y]$ when $E[Y] = \mu$, $e_i$ is the [[Pearson Residual]], and $\hat{h}_i$ is the $i$th [[Leverage]].