---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 ([[Multiple Linear Regression]] [[Hypothesis Test]])[^1]
> For a multiple linear regression, to test the [[Null Hypothesis]] $H_0: \beta_1 = \beta_2 = \dots = \beta_p = 0$ (there is no relationship between $X, Y$) vs. the [[Alternative Hypothesis]] $H_a:$ at least one of $\beta_j$ is non-zero, we use the [[F-Test Statistic]]
> $$
> \begin{align}
> F = \frac{(TSS - RSS) / p}{RSS / (n - p - 1)}
> \end{align}
> $$
> where $TSS$ is [[Total Sum of Squares]] and $RSS$ is [[Residual Sum of Squares]].

If the linear model assumptions are correct, then $E[RSS / (n - p - 1)] = \sigma^2$, and if $H_0$ is true, then $E[(TSS - RSS) / p] = \sigma^2$, so if there's no relationship between $X, Y$, then $F \approx 1$.

> [!info] Definition 2 (F-Test Statistic for Subset of Parameters)
> For the null hypothesis testing a subset of $q$ parameters, the F-test statistic is
> $$
> \begin{align}
> F = \frac{(RSS_0 - RSS) / q}{RSS / (n - p - 1)}
> \end{align}
> $$
> where $RSS_0$ is the [[Residual Sum of Squares]] of the second linear model that fitted only the subset of $q$ parameters.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=93)