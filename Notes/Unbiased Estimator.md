---
tags:
  - statistics
  - statistical_learning
---

# Definition

On average, taken over a large number of observations, the unbiased [[Estimator]] would be expected to equal the population parameter/value.

Unbiased estimators do not systematically over- or under-estimate the true parameter.[^1] Formally, a statistic $T$ is unbiased for $\theta$ if $E(T) = \theta$; e.g. the [[Sample Mean]] is unbiased for $\mu$ and the [[Sample Variance]] $S^2$ (divisor $n - 1$) is unbiased for $\sigma^2$, while the divisor-$n$ version is not.[^2] Unbiasedness is a frequentist criterion, averaging over repeated samples with the parameter fixed. It is a finite-sample property, unlike the asymptotic [[Consistent Estimator|consistency]]. The best unbiased estimator, the one with the smallest variance at every $\theta$, is the [[Minimum Variance Unbiased Estimator]].

[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=168)

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=83)

