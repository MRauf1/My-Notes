---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 ([[Simple Linear Regression]] [[Hypothesis Test]])[^1]
> For a simple linear regression, testing the [[Null Hypothesis]] of $H_0: \beta_1 = 0$ vs. $H_a: \beta_1 \neq 0$ (or in other words, $H_0:$ there is no relationship between $X, Y$, and $H_a:$ there is some relationship between $X, Y$), we calculate the [[t-Test Statistic]]
> $$
> \begin{align}
> t = \frac{\hat{\beta}_1 - 0}{SE(\hat{\beta}_1)}
> \end{align}
> $$
> If we want to test the null hypothesis of $H_0: \beta_1 = a$, then replace $0$ with $a$ in the t-test statistic.

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=85)