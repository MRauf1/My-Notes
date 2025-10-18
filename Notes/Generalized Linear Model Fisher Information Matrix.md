---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Generalized Linear Model]] [[Fisher Information Matrix]])
> For GLM, the information matrix is
> $$
> \begin{align}
> I = \mathbf{X}^T \mathbf{W} \mathbf{X}
> \end{align}
> $$
> where $\mathbf{W} = diag(w_1, \dots, w_N)$ with $w_i = (\frac{\partial \mu_i}{\partial \eta_i})^2 \cdot \frac{1}{Var[Y_i]}$ ($\mu_i = E[Y_i]$).