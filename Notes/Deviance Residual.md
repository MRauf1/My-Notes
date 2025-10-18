---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Generalized Linear Model]] [[Deviance]] Residual)
> Given $\hat{\mu}_i =$ MLE of $E[Y_i]$, the $i$th deviance residual are
> $$
> \begin{align}
> sign(y_i - \hat{\mu}_i) \cdot \sqrt{d_i}
> \end{align}
> $$
> where $d_i = -2 (L(\hat{\mu}_i, y_i) - L(y_i, y_i)) \geq 0$