---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Tolerance Interval[^1]
> Let $Y_1 < \dots < Y_n$ be the [[Order Statistic|order statistics]] of a [[Random Sample]] from a continuous distribution with cdf $F$. If
> $$
> \begin{align}
> \gamma = P[F(Y_j) - F(Y_i) \geq p]
> \end{align}
> $$
> then the realized interval $(y_i, y_j)$ is a $100\gamma\%$ tolerance interval for $100p\%$ of the probability for the distribution of $X$, and $y_i, y_j$ are the $100\gamma\%$ tolerance limits.

A [[Confidence Interval]] traps a parameter (e.g. the mean); a tolerance interval traps a stated proportion $p$ of the population itself, with confidence $\gamma$. It answers "where will most individual values fall?", which is often the practical question, e.g. whether nearly all filled containers exceed a labeled amount.

# Properties
- Distribution-free: by the [[Probability Integral Transform]], $F(Y_j) - F(Y_i) \sim$ [[Beta Distribution|Beta]]$(j - i, n - j + i + 1)$ whatever the continuous $F$, so $\gamma$ is computable from $n, i, j, p$ alone.
- Two levels are involved: the content $p$ (what fraction of the distribution is covered) and the confidence $\gamma$ (how often the procedure achieves that coverage).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=333)
