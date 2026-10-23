---
tags:
  - computer_science
  - machine_learning
---

# Definition
> [!info] Bootstrap[^1]
> A frequentist method for obtaining error bars on parameter estimates. From an original data set $\mathbf{X} = \{\mathbf{x}_1, \dots, \mathbf{x}_N\}$, create a new data set $\mathbf{X}_B$ by drawing $N$ points at random from $\mathbf{X}$ **with replacement**. Repeat to generate $L$ data sets of size $N$; the statistical accuracy of the estimates is evaluated from the variability of the predictions across the $L$ bootstrap data sets.

In Hogg et al.'s formulation,[^2] a bootstrap sample is a random sample of size $n$ drawn with replacement from the [[Empirical Distribution Function]] $\hat{F}_n$ of the observed sample, which stands in for the unknown $F$. The only information about sampling variability is within the sample itself, and resampling the sample simulates that variability.

# Types
- [[Percentile Bootstrap Confidence Interval]]
- [[Bootstrap Hypothesis Test]]
- [[Bootstrap Standard Error]]: including the nonparametric vs parametric bootstrap

# Properties
- Used in machine learning for [[Bagging]] (bootstrap aggregating).
- Because sampling is with replacement, some points of $\mathbf{X}$ are replicated in $\mathbf{X}_B$ while others are absent; on average a bootstrap set contains a fraction $1 - (1 - 1/N)^N \to 1 - e^{-1} \approx 0.632$ of the distinct original points.
- Implements the [[Probability Frequentist Framework|frequentist]] notion of uncertainty, which considers the distribution of possible data sets, by using the empirical distribution of the observed data as a stand-in for the unknown data-generating distribution.
- Needs $L$ refits of the estimator, so its cost is $L$ times that of a single fit.
- Monte Carlo implementation:[^3] draw $I(i, b) \sim \mathcal{U}\{1, \dots, n\}$ and set $X_i^{*b} = X_{I(i,b)}$ for $i \leq n$, $b \leq B$; with $\hat{T}^{*b} = T(X_1^{*b}, \dots, X_n^{*b})$ and $\bar{T} = \frac{1}{B}\sum_b \hat{T}^{*b}$, the bootstrap variance estimate is $\frac{1}{B - 1}\sum_{b=1}^B(\hat{T}^{*b} - \bar{T})^2$, and the [[Percentile Bootstrap Confidence Interval|percentile]] 95% interval runs from the 2.5th to the 97.5th percentile of the $\hat{T}^{*b}$. Useful when $\hat{T}$ is too complicated to analyze or $F$ has unknown form.

[^1]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=ZV5X7D27)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=320)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=20&annotation=H637KXMV)
