---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Point Estimator[^1]
> Let $X_1, \dots, X_n$ be a [[Random Sample]] on $X$ with pdf or pmf $f(x; \theta)$, $\theta \in \Omega$ ([[Parameter Space]]). A [[Statistic]] $T = T(X_1, \dots, X_n)$ used to estimate $\theta$ is a point estimator of $\theta$. Its realization $t = T(x_1, \dots, x_n)$ is an estimate of $\theta$.

An estimator is a random variable (a rule applied to the random sample), while an estimate is the single number it produces for the observed data. Judging an estimator means judging its sampling distribution, not the particular estimate.

# Types
- [[Unbiased Estimator]]: $E_\theta(T) = \theta$ for all $\theta$.
- [[Maximum Likelihood Estimation|Maximum likelihood estimator]].
- Nonparametric estimators such as the [[Histogram]] and [[Kernel Density Estimation|kernel density estimate]].

# Properties
- Accuracy is summarized by the [[Mean Squared Error]], $E_\theta[(T - \theta)^2] = \text{bias}^2 + \text{variance}$ ([[Bias-Variance-MSE Decomposition of an Estimator]]), and asymptotically by [[Bias and Consistency of an Estimator|consistency]].
- The error of estimation is quantified by the [[Standard Error]] and by a [[Confidence Interval]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=242)
