---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Fisher Information Matrix]] Relationship with [[Covariance Matrix]])
> For a [[Maximum Likelihood Estimation|maximum likelihood estimator]] $\mathbf{\hat{\beta}}$ of the true parameter $\mathbf{\beta}$, the asymptotic [[Covariance Matrix]] of the estimator is
> $$
> \begin{align}
> Cov[\mathbf{\hat{\beta}}] = I(\mathbf{\beta})^{-1}
> \end{align}
> $$
> Since $\mathbf{\beta}$ is unknown, $I(\mathbf{\beta})$ is estimated in practice by evaluating the [[Fisher Information Matrix]] at $\mathbf{\hat{\beta}}$, i.e. $I(\mathbf{\hat{\beta}})^{-1}$. [[Standard Error]] of $\mathbf{\hat{\beta}}$ are the [[Square Root]] of the diagonal elements of the [[Covariance Matrix]].

The greater the [[Curvature]] of the [[Log-Likelihood Function]], the smaller the [[Standard Error]].
