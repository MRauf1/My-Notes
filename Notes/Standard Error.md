---
tags: statistics, statistical_learning
---

# Definition

> [!info] Definition 1 (Standard Error)[^1]
> Given an estimated parameter $\hat{\mu}$, its standard error is
> $$
> \begin{align}
> Var[\hat{\mu}] = SE(\hat{\mu})^2 = \frac{\sigma^2}{n}
> \end{align}
> $$
> where $\sigma$ is the [[Standard Deviation]] of $y_i$ of $Y$.
> This formula holds provided that the $n$ observations are [[Correlation|uncorrelated]].

Roughly speaking, the standard errors tells the average amount that the estimate $\hat{\mu}$ deviates from the actual value of $\mu$. According to the formula, this deviation gets lower as $n$ increases.

# Types
- [[Residual Standard Error]]

[^1]: [Introduction to Statistical Learning with Python](zotero://open-pdf/library/items/9JTAJ2JI?page=84)