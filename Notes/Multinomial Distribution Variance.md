---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Multinomial Distribution]] [[Variance]])[^1]
> For a [[Multinomial Distribution]] denoted $Multinomial(n, p_1, \dots, p_c)$, its variance is
> $$
> \begin{align}
> Var[n_j] &= n p_j(1 - p_j) \\
> Var[X] &= n \begin{bmatrix}p_1 (1 - p_1) & - p_1 p_2 & \dots & - p_1 p_c \\ - p_1 p_2 & p_2 (1 - p_2) & \dots & \dots \\ \vdots & \vdots & \vdots & \vdots \\ - p_1 p_c & \dots & \dots & p_c (1 - p_c)\end{bmatrix}
> \end{align}
> $$

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=24)