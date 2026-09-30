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
- Because sampling is with replacement, some points of $\mathbf{X}$ are replicated in $\mathbf{X}_B$ while others are absent; on average a bootstrap set contains a fraction $1 - (1 - 1/N)^N \to 1 - e^{-1} \approx 0.632$ of the distinct original points.
- Implements the [[Probability Frequentist Framework|frequentist]] notion of uncertainty, which considers the distribution of possible data sets, by using the empirical distribution of the observed data as a stand-in for the unknown data-generating distribution.
- Needs $L$ refits of the estimator, so its cost is $L$ times that of a single fit.

[^1]: [Bishop, 2006, p. 23](zotero://open-pdf/library/items/5G99AZ8U?page=43&annotation=ZV5X7D27)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=320)
