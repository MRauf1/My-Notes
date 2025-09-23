---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Contingency Table]] [[Standardized Residual]])
> For a contingency table, the Standardized residuals are
> $$
> \begin{align}
> r_{ij} = \frac{n_{ij} - \hat{\mu}_{ij}}{\sqrt{\hat{\mu}_{ij} (1 - p_{i+})(1 - p_{+j})}}
> \end{align}
> $$
> where $p_{ij} = \frac{n_{ij}}{n}$

Standardized residuals are asymptotically follow the [[Normal Distribution]] $N(0, 1)$.

If the standardized residuals exceed $|2|$ or $|3|$, it suggests that there is significant dependence between $X, Y$. 