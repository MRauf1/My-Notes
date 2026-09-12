---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

> [!info] Definition 1 ([[Fisher Information]] [[Matrix]])
> Fisher Information matrix is a matrix, denoted as $I(\mathbf{\beta}) = - E[\nabla^2 L(\mathbf{\beta})]$, whose $jk$-th element is
> $$
> \begin{align}
> \iota(\mathbf{\beta})_{jk} = -E[\frac{\partial^2 L(\mathbf{\beta})}{\partial \beta_j \partial \beta_k}]
> \end{align}
> $$

# Properties
- [[Fisher Information Matrix Relationship with Covariance Matrix]]

Fisher information measures how much the data constrains $\beta$ by quantifying the [[Curvature|curvature]] of the [[Log-Likelihood Function|log-likelihood]] $L(\beta)$ around its maximum: a log-likelihood that is sharply peaked (high curvature, large $I(\beta)$) means only a narrow range of $\beta$ values fit the data well, so the estimate is precise; a flat log-likelihood (low curvature, small $I(\beta)$) means many nearby values of $\beta$ are almost equally plausible, so the estimate is imprecise. This is why $I(\beta)^{-1}$ equals the [[Fisher Information Matrix Relationship with Covariance Matrix|estimator's asymptotic covariance]].