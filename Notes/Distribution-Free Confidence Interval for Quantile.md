---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Distribution-Free Confidence Interval for a Quantile[^1]
> Let $X$ be continuous with cdf $F$ and $p$th quantile $\xi_p$ ($F(\xi_p) = p$), and let $Y_1 < \dots < Y_n$ be the [[Order Statistic|order statistics]] of a [[Random Sample]] on $X$. For $i < \lfloor (n+1)p \rfloor < j$,
> $$
> \begin{align}
> \gamma = P(Y_i < \xi_p < Y_j) = \sum_{w=i}^{j-1}\binom{n}{w}p^w(1 - p)^{n-w}
> \end{align}
> $$
> so the realized interval $(y_i, y_j)$ is a $100\gamma\%$ [[Confidence Interval]] for $\xi_p$.

Derivation: call an observation a success if $X < \xi_p$, which has probability $F(\xi_p) = p$. Then $Y_i < \xi_p$ means at least $i$ successes, and $Y_j > \xi_p$ means fewer than $j$ successes, so the event is "between $i$ (inclusive) and $j$ (exclusive) successes in $n$ independent trials", a [[Binomial Distribution|binomial]] probability.

# Properties
- Distribution-free: the only assumption on $F$ is continuity; the coverage does not depend on the shape of the distribution.
- The confidence level $\gamma$ takes only discrete values, determined by $n$, $i$, $j$; one picks $i, j$ to reach the desired level.
- The case $p = 1/2$ gives a confidence interval for the [[Median]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=277)
