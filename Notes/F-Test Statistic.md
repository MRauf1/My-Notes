---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 ([[F-Test]] Statistic)[^1]
> $$
> \begin{align}
> F = \frac{(TSS - RSS) / p}{RSS / (n - p - 1)} \sim F()
> \end{align}
> $$
> where $TSS$ is [[Total Sum of Squares]] and $RSS$ is [[Residual Sum of Squares]].

If the linear model assumptions are correct, then $E[RSS / (n - p - 1)] = \sigma^2$, and if $H_0$ is true, then $E[(TSS - RSS) / p] = \sigma^2$, so if there's no relationship between $X, Y$, then $F \approx 1$.

#TODO 
Complete and verify this section.
Relationship between t-test and F-test

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=93)