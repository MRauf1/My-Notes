---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Heteroscedasticity (Machine Learning)[^1]
> A model is **heteroscedastic** when its uncertainty varies as a function of the input, and **homoscedastic** when the uncertainty is constant everywhere.

# Properties
- In heteroscedastic regression with the [[Maximum Likelihood Loss Function Recipe]], the network predicts both the mean $\mu = f_1[\mathbf{x}, \boldsymbol{\phi}]$ and the variance $\sigma^2 = f_2[\mathbf{x}, \boldsymbol{\phi}]^2$ of a [[Normal Distribution]] (squared, or passed through another positive function, to keep the variance positive), and minimizes the resulting negative log-likelihood ([[Probabilistic Formulation of Regression]]).
- The homoscedastic case reduces to least squares, since the constant variance does not affect the minimizer of the mean.

[^1]: [Prince, Ch. 5](zotero://select/library/items/T3V9WVXD)
