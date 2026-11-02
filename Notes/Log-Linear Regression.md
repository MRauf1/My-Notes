---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Log-Linear Regression)[^1]
> A [[Generalized Linear Model]] for a count response $Y$ with mean $\mu(x) = E[Y \mid x]$ that uses the log [[Link Function|link]]:
> $$
> \begin{align}
> \log \mu(x) = x\beta \iff \mu(x) = e^{x\beta}
> \end{align}
> $$
> so each predictor acts multiplicatively on the mean. With a [[Poisson Distribution|Poisson]] random component this is [[Poisson Regression]]; applied to the cell counts of a contingency table, it gives the log-linear models for association.

# Types
- [[Poisson Regression]]

# Properties
- [[Log-Linear Regression Deviance]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L)
