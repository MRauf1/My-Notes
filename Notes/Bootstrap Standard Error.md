---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Bootstrap Standard Error[^1]
> Let $\hat{\theta} = \hat{\theta}(x_1, \dots, x_n)$ be an estimate of $\theta$. Draw $B$ [[Bootstrap]] samples $\mathbf{x}_i^* = (x_{i,1}^*, \dots, x_{i,n}^*)^T$ with replacement from the [[Empirical Distribution Function]] $\hat{F}_n$, which places mass $1/n$ on each $x_i$. Let $\hat{\theta}_i^* = \hat{\theta}(\mathbf{x}_i^*)$ for $i = 1, \dots, B$. The bootstrap estimate of the [[Standard Error|standard error]] of $\hat{\theta}$ is the standard deviation of the bootstrap estimates,
> $$
> \begin{align}
> SE_B = \left[\frac{1}{B - 1}\sum_{i=1}^B (\hat{\theta}_i^* - \bar{\theta}^*)^2\right]^{1/2}, \qquad \bar{\theta}^* = \frac{1}{B}\sum_{i=1}^B \hat{\theta}_i^*
> \end{align}
> $$
> (The printed $\hat{\theta}_1^*$ inside the sum should be $\hat{\theta}_i^*$.)

The summary $\hat{\theta} \pm SE(\hat{\theta})$ is useful descriptively and for asymptotic confidence intervals. For MLEs, asymptotic theory usually gives $SE$ directly ([[Maximum Likelihood Estimator Standard Error]]). The bootstrap gives it for any estimator, including MVUEs, without deriving its sampling distribution.

> [!info] Nonparametric vs Parametric Bootstrap[^2]
> - The nonparametric bootstrap resamples from $\hat{F}_n$ and makes no assumptions about $f(x; \theta)$.
> - The parametric bootstrap uses the assumed model: it resamples from the fitted distribution $f(x; \hat{\theta})$, e.g. $N(\bar{x}, s^2)$ for a normal model.
>
> Hogg et al. recommend the nonparametric bootstrap in general, because its validity does not need the strong model assumptions (Efron and Tibshirani, 1993, pp. 55-56).

# Properties
- The same bootstrap replicates $\hat{\theta}_i^*$ also give the [[Percentile Bootstrap Confidence Interval]].
- The parametric bootstrap can be more accurate when the model is correct, especially for small $n$. It inherits any model misspecification, however.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=460&annotation=YGI76VEW)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=461&annotation=9V7W5MCF)
