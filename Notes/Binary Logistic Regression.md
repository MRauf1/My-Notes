---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Binary [[Logistic Regression]])
> Given independent variables $X$ with $k$ predictors and a dependent variable $Y$ distributed from the [[Bernoulli Distribution]] with parameter $p$, the binary logistic regression is
> $$
> \begin{align}
> P(Y) = E[Y | X = X_i] = \frac{1}{1 + e^{-(X_i \beta)}}
> \end{align}
> $$
> where $\beta$ are the coefficients.