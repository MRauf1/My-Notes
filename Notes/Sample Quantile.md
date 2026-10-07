---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Sample Quantile[^1][^2]
> Let $X$ have a continuous cdf $F$ with $p$th quantile $\xi_p = F^{-1}(p)$, $0 < p < 1$ ([[Quantile Function]]), and let $Y_1 < \dots < Y_n$ be the [[Order Statistic|order statistics]] of a [[Random Sample]] on $X$. With $k = \lfloor p(n + 1) \rfloor$, the $p$th sample quantile (the $100p$th sample percentile) is $Y_k$, a point estimator of $\xi_p$.

Justification: the area under $f$ to the left of $Y_k$ is $F(Y_k)$, and substituting $z = F(y_k)$ in the pdf of $Y_k$ gives a beta integral,
$$
\begin{align}
E[F(Y_k)] = \int_0^1 \frac{n!}{(k-1)!(n-k)!}z^k(1 - z)^{n-k}\,dz = \frac{k}{n + 1}
\end{align}
$$
so on average a fraction $k/(n+1) \approx p$ of the probability lies to the left of $Y_k$.

# Properties
- Interpolated version:[^2] writing $(n + 1)p = k + r$ with $k = \lfloor (n+1)p \rfloor$ and $0 < r < 1$, the weighted average $(1 - r)Y_k + rY_{k+1}$ is another common estimator of $\xi_p$ (the default in R's `quantile`). All such definitions agree asymptotically.
- Special cases: the sample median $Q_2$, and the sample quartiles $Q_1 \approx Y_{0.25(n+1)}$ and $Q_3 \approx Y_{0.75(n+1)}$, which form the [[Five-Number Summary]]; their difference estimates the [[Interquartile Range]].
- Plotting sample quantiles against theoretical quantiles gives a [[Q-Q Plot]].
- Order statistics also give an exact [[Distribution-Free Confidence Interval for Quantile]].
- Monte Carlo convention:[^3] estimate $Q_\theta = F^{-1}(\theta)$ of the distribution $F$ of $Y$ by $\tilde{Q}_\theta = Y_{(\lceil n\theta \rceil)}$, where $Y_{(1)} \leq \dots \leq Y_{(n)}$ are the [[Order Statistic|order statistics]] of $n$ IID simulated values.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=273)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=274)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=25&annotation=XGKFIM9D); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=26&annotation=FUXDHGXY)
