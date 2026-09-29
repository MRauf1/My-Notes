---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Percentile Bootstrap Confidence Interval[^1]
> Let $\mathbf{x} = (x_1, \dots, x_n)$ be a realized [[Random Sample]] from $F(x; \theta)$, let $\hat{\theta}$ be a point [[Estimator]] of $\theta$, and let $B$ be the number of bootstrap replications (often $3000$ or more).
> 1. For $j = 1, \dots, B$: draw a bootstrap sample $\mathbf{x}_j^*$ of size $n$ from $x_1, \dots, x_n$ at random with replacement, and compute $\hat{\theta}_j^* = \hat{\theta}(\mathbf{x}_j^*)$.
> 2. Order them as $\hat{\theta}^*_{(1)} \leq \dots \leq \hat{\theta}^*_{(B)}$, and let $m = \lfloor(\alpha/2)B\rfloor$.
> 3. The $(1 - \alpha)100\%$ percentile bootstrap confidence interval is
> $$
> \begin{align}
> \left(\hat{\theta}^*_{(m)},\ \hat{\theta}^*_{(B+1-m)}\right)
> \end{align}
> $$
> the $\frac{\alpha}{2}100\%$ and $(1 - \frac{\alpha}{2})100\%$ percentiles of the bootstrap distribution of $\hat{\theta}^*$.

**Motivation.**[^2] If $\hat{\theta} \sim N(\theta, \sigma_{\hat{\theta}}^2)$, the usual interval is $(\hat{\theta} - z^{(1-\alpha/2)}\sigma_{\hat{\theta}},\ \hat{\theta} - z^{(\alpha/2)}\sigma_{\hat{\theta}})$. If $\hat{\theta}^* \sim N(\hat{\theta}, \sigma_{\hat{\theta}}^2)$, then $P(\hat{\theta}^* \leq \hat{\theta}_L) = \alpha/2$ and $P(\hat{\theta}^* \leq \hat{\theta}_U) = 1 - \alpha/2$: the endpoints of the interval are the $\alpha/2$ and $1 - \alpha/2$ percentiles of the distribution of $\hat{\theta}^*$. With infinitely many independent samples, the percentiles of the histogram of their estimates would give the interval directly. With only one sample, the [[Bootstrap]] simulates that sampling variability by resampling from the [[Empirical Distribution Function]], since the sample is the only information about the variability. The normality assumption is not needed for the procedure to be valid.

# Properties
- Needs no formula for the [[Standard Error]] or the sampling distribution of $\hat{\theta}$; it applies to complicated estimators (medians, ratios, correlations) as long as they can be computed.
- Transformation-respecting: the interval for $g(\theta)$ is $g$ of the interval for $\theta$ when $g$ is monotone.
- Coverage is only approximate and can be poor for small $n$ or biased, skewed $\hat{\theta}$; refinements (BCa, bootstrap-$t$) correct this.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=321)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=320)
