---
tags: statistics, categorical_variable_prediction
---

# Definition

> [!info] Definition 1 (Variance of [[Discrete Random Variable]])
> For a [[Discrete Random Variable]] $X$, its variance is
> $$
> \begin{align}
> Var[X] = E[X - E[X]]^2 = \sum_{x \in S} [x - E[X]]^2 f(x)
> \end{align}
> $$

> [!info] Definition 2 (Variance of [[Continuous Random Variable]])
> For a [[Continuous Random Variable]] $X$, its variance is
> $$
> \begin{align}
> Var[X] = E[X - E[X]]^2 = \int_{-\infty}^{\infty} [x - E[X]]^2 f(x) dx
> \end{align}
> $$

Variance measures the spread around the mean via the expected squared deviation from the center of the distribution.[^1]

# Properties

## [[Conditional Variance]]
- [[Law of Total Variance]]

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=16)