---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Generalized Linear Model]] Pearson Residual)
> Given $\hat{\mu}_i =$ MLE of $E[Y_i]$, the pearson residuals are
> $$
> \begin{align}
> e_i = \frac{y_i - \hat{\mu}_i}{\sqrt{v(\hat{\mu}_i)}}
> \end{align}
> $$
> where $v(\mu) = Var[Y]$ when $E[Y] = \mu$.