---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Contingency Table]] [[Pearson Residual]])
> For a contingency table, the Pearson residuals are
> $$
> \begin{align}
> e_{ij} = \frac{n_{ij} - \hat{\mu}_{ij}}{\sqrt{\hat{\mu}_{ij}}}
> \end{align}
> $$
> where $X^2 = \sum_{i} \sum_{j} e_{ij}$, where $X^2$ is the [[Pearson Chi-Squared Test]] statistic.

Pearson residuals are asymptotically follow the [[Normal Distribution]] (although the asymptotic [[Variance]] may not be $1$).

If the Pearson residuals exceed $|2|$ or $|3|$, it suggests that there is significant dependence between $X, Y$.