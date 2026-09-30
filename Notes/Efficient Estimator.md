---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Efficient Estimator[^1]
> An [[Unbiased Estimator]] $Y$ of $\theta$ is an efficient estimator if and only if its variance attains the [[Rao-Cramér Lower Bound]], $\text{Var}(Y) = \frac{1}{nI(\theta)}$.

> [!info] Efficiency[^2]
> When differentiation under the integral or summation sign is allowed, the efficiency of an unbiased estimator is the ratio of the Rao-Cramér lower bound to its actual variance,
> $$
> \begin{align}
> \text{eff}(Y) = \frac{1/(nI(\theta))}{\text{Var}(Y)} \leq 1
> \end{align}
> $$

> [!info] Asymptotic Efficiency[^3]
> If $\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{D} N(0, \sigma^2_{\hat{\theta}})$, the asymptotic efficiency of $\hat{\theta}_n$ is
> $$
> \begin{align}
> e(\hat{\theta}_n) = \frac{1/I(\theta_0)}{\sigma^2_{\hat{\theta}}}
> \end{align}
> $$
> and $\hat{\theta}_n$ is asymptotically efficient if this ratio is $1$.

Efficiency measures how much of the information in the sample an estimator uses: an efficient estimator extracts all of it. For vector parameters, an unbiased $Y_j$ for $\theta_j$ is efficient if $\text{Var}(Y_j) = \frac{1}{n}[I^{-1}(\boldsymbol{\theta})]_{jj}$.[^4]

# Properties
- Under regularity conditions, maximum likelihood estimators are asymptotically efficient ([[Maximum Likelihood Estimator Asymptotic Normality]]), even when no finite-sample efficient estimator exists.
- Two asymptotically normal estimators are compared by the [[Asymptotic Relative Efficiency]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=382)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=383)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=386)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=405)
