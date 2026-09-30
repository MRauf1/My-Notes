---
tags:
  - statistics
  - categorical_variable_prediction
---

# Definition

Under the [[Maximum Likelihood Regularity Conditions]]:[^1]
- Large-sample [[Normal Distribution]]: $\sqrt{n}(\hat{\theta} - \theta_0) \xrightarrow{D} N(0, 1/I(\theta_0))$ ([[Maximum Likelihood Estimator Asymptotic Normality]])
- Asymptotically unbiased; not [[Unbiased Estimator|unbiased]] in general for finite $n$ (e.g. the MLE $\frac1n\sum(X_i - \bar{X})^2$ of a normal variance is biased)
- Asymptotically [[Efficient Estimator]]: its asymptotic variance attains the [[Rao-Cramér Lower Bound]]
- [[Consistent Estimator]]: a root of the likelihood equation converges in probability to $\theta_0$
- Invariant under reparametrization ([[Maximum Likelihood Estimator Invariance]])

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=385)