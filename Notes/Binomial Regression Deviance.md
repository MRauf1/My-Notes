---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Binomial Regression]] [[Generalized Linear Model Deviance]])
> [[Deviance]] for any GLM link function with [[Binomial Distribution]] sampled outputs is
> $$
> \begin{align}
> D(\mathbf{y}, \hat{\mathbf{\mu}}) = 2 \sum_{i} y_i ln(\frac{y_i}{\hat{\mu}_i}) + 2 \sum_{i} (n_i - y_i) ln(\frac{n_i - y_i}{n_i - \hat{\mu}_i})
> \end{align}
> $$
> where $\hat{\mu}_i = n_i \hat{p}_i$.
> This works if $\mu_i, n_i - \mu_i$ are sufficiently large. Thus, it won't work for [[Binary Logistic Regression]].

> [!info] Definition 2 ([[Deviance]] and $G^2$)
> For a $2 \times 2$ table, for the independent binomial model $M$ under [[Homogeneity]] $(p_1 = p_2)$,
> $$
> \begin{align}
> G^2(M) = D_M(\mathbf{y}, \hat{\mathbf{\mu}})
> \end{align}
> $$