---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Large-Sample Confidence Interval for $\mu_1 - \mu_2$[^1]
> Let $X_1, \dots, X_{n_1}$ and $Y_1, \dots, Y_{n_2}$ be independent [[Random Sample|random samples]] from distributions with means $\mu_1, \mu_2$ and finite variances $\sigma_1^2, \sigma_2^2$. With $\hat{\Delta} = \bar{X} - \bar{Y}$ and [[Sample Variance|sample variances]] $S_1^2, S_2^2$, the pivot $Z = \frac{\hat{\Delta} - \Delta}{\sqrt{S_1^2/n_1 + S_2^2/n_2}}$ is approximately $N(0, 1)$, which gives the approximate $(1 - \alpha)100\%$ interval
> $$
> \begin{align}
> (\bar{x} - \bar{y}) \pm z_{\alpha/2}\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
> \end{align}
> $$

> [!info] Pooled $t$-Interval (Exact, Normal Equal-Variance Case)[^2]
> If $X \sim N(\mu_1, \sigma^2)$ and $Y \sim N(\mu_2, \sigma^2)$ with a common variance (a location model), let $n = n_1 + n_2$ and let the pooled variance be
> $$
> \begin{align}
> S_p^2 = \frac{(n_1 - 1)S_1^2 + (n_2 - 1)S_2^2}{n - 2}
> \end{align}
> $$
> Then $\frac{(\bar{X} - \bar{Y}) - \Delta}{S_p\sqrt{1/n_1 + 1/n_2}}$ has a [[t-Distribution]] with $n - 2$ degrees of freedom, and an exact $(1 - \alpha)100\%$ confidence interval for $\Delta = \mu_1 - \mu_2$ is
> $$
> \begin{align}
> (\bar{x} - \bar{y}) \pm t_{\alpha/2, n-2}\,s_p\sqrt{\frac{1}{n_1} + \frac{1}{n_2}}
> \end{align}
> $$

# Properties
- $\hat{\Delta}$ is an [[Unbiased Estimator]] of $\Delta$ with $\text{Var}(\hat{\Delta}) = \sigma_1^2/n_1 + \sigma_2^2/n_2$ by independence of the samples ([[Linear Combination of Random Variables]]); $\sqrt{s_1^2/n_1 + s_2^2/n_2}$ is the [[Standard Error]] of $\bar{X} - \bar{Y}$.
- The large-sample interval rests on the [[Central Limit Theorem]]; the pooled interval on [[Student's Theorem]], since $(n-2)S_p^2/\sigma^2 \sim \chi^2(n - 2)$ is the sum of two independent chi-squareds.
- With Bernoulli samples, the large-sample interval becomes the [[Difference of Proportions Confidence Interval]].
- If the variances differ, the pooled interval is invalid; Welch's approximate $t$-interval uses the unpooled standard error with adjusted degrees of freedom.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=257)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=258)
