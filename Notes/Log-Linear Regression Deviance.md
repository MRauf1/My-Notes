---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Log-Linear Regression]] [[Generalized Linear Model Deviance]])
> For a log-linear model,
> $$
> \begin{align}
> D(\mathbf{y}, \hat{\mathbf{\mu}}) = 2 \sum_{i} (y_i ln(\frac{y_i}{\hat{\mu}_i}) - y_i + \hat{\mu}_i)
> \end{align}
> $$
> If the linear predictor has an intercept/bias, this simplifies to
> $$
> \begin{align}
> D(\mathbf{y}, \hat{\mathbf{\mu}}) = 2 \sum_{i} y_i ln(\frac{y_i}{\hat{\mu}_i})
> \end{align}
> $$