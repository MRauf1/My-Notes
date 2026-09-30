---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Asymptotic Relative Efficiency (ARE)[^1]
> Let $\sqrt{n}(\hat{\theta}_{1n} - \theta_0) \xrightarrow{D} N(0, \sigma^2_{\hat{\theta}_1})$ and $\sqrt{n}(\hat{\theta}_{2n} - \theta_0) \xrightarrow{D} N(0, \sigma^2_{\hat{\theta}_2})$. The asymptotic relative efficiency of $\hat{\theta}_{1n}$ to $\hat{\theta}_{2n}$ is the reciprocal ratio of their asymptotic variances,
> $$
> \begin{align}
> e(\hat{\theta}_{1n}, \hat{\theta}_{2n}) = \frac{\sigma^2_{\hat{\theta}_2}}{\sigma^2_{\hat{\theta}_1}}
> \end{align}
> $$

Between two asymptotically normal estimators with the same asymptotic mean, the one with the smaller asymptotic variance is preferred, and its ARE to the other exceeds $1$.

# Properties
- Sample-size interpretation:[^2] ARE is the limiting ratio of sample sizes needed for equal precision. For the [[Laplace Distribution]], the ARE of the sample median $Q_2$ to the sample mean $\bar{X}$ is $2$, so $\bar{X}$ needs twice as many observations to give confidence intervals as short as those from $Q_2$.
- The ARE of an estimator to an asymptotically efficient one (e.g. the MLE) is its asymptotic efficiency $e(\hat{\theta}_{1n})$ ([[Efficient Estimator]]).
- For normal data, the ARE of the median to the mean is $2/\pi \approx 0.64$; which estimator is better depends on the distribution, which is a key idea of robust statistics.
- An analogous notion of efficiency exists for tests.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=386)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=387)
