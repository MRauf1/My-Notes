---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Statistic[^1]
> Let $X_1, \dots, X_n$ be a sample on a random variable $X$. A function $T = T(X_1, \dots, X_n)$ of the sample is a statistic. Once the sample is drawn with realization $x_1, \dots, x_n$, the number $t = T(x_1, \dots, x_n)$ is the realization of $T$.

A statistic summarizes the information in a sample. It must be computable from the data alone, so it cannot depend on unknown parameters (e.g. $\bar{X}$ is a statistic, but $\bar{X} - \mu$ is not when $\mu$ is unknown). Before sampling, $T$ is a random variable with its own distribution, the sampling distribution.

# Types
- [[Estimator]]: a statistic used to estimate a parameter.
- [[Test Statistic]]: a statistic used to decide between hypotheses.
- [[Sample Mean]], [[Sample Variance]], [[Order Statistic|order statistics]], and sample quantiles ([[Sample Quantile]]).

# Properties
- Upper-case letters denote the statistic (random variable) and lower-case letters its observed realization, as with $X_i$ and $x_i$.
- Usually computed from a [[Random Sample]].
- Any statistic $Y = u(X_1, \dots, X_n)$ partitions the sample space into the level sets $\{\mathbf{x} : u(\mathbf{x}) = y\}$.[^2] A statistic whose partition keeps all the information about $\theta$ is a [[Sufficient Statistic]], and one whose distribution is free of $\theta$ is an [[Ancillary Statistic]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=242)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=435&annotation=M75GQ92V)
