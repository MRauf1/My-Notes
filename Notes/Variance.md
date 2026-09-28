---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Variance)[^2]
> Let $X$ be a [[Random Variable]] with finite mean $\mu$ such that $E[(X - \mu)^2]$ is finite. The variance of $X$ is
> $$
> \begin{align}
> \sigma^2 = \text{Var}(X) = E[(X - \mu)^2]
> \end{align}
> $$

> [!info] Definition 2 (Variance of [[Discrete Random Variable]])
> For a [[Discrete Random Variable]] $X$, its variance is
> $$
> \begin{align}
> \text{Var}(X) = E[(X - E[X])^2] = \sum_{x \in S} (x - E[X])^2 f(x)
> \end{align}
> $$

> [!info] Definition 3 (Variance of [[Continuous Random Variable]])
> For a [[Continuous Random Variable]] $X$, its variance is
> $$
> \begin{align}
> \text{Var}(X) = E[(X - E[X])^2] = \int_{-\infty}^{\infty} (x - E[X])^2 f(x)\,dx
> \end{align}
> $$

Variance measures the spread around the mean via the expected squared deviation from the center of the distribution.[^1] In the discrete case it is a weighted average of the squared deviations $(a_i - \mu)^2$ of the support points, with weights $p(a_i)$; it is the second [[Moment (Statistics)|moment]] of $X$ about $\mu$.

# Properties
- [[Variance Basic Properties]]
- $\sigma = \sqrt{\sigma^2}$ is the [[Standard Deviation]].
- $\text{Var}(X) = 0$ if and only if $X$ has a [[Degenerate Distribution]].

## [[Conditional Variance]]
- [[Law of Total Variance]]

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=16)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=84)
