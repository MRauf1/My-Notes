---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Five-Number Summary[^1]
> For a sample with [[Order Statistic|order statistics]] $Y_1 < \dots < Y_n$, the five-number summary consists of the [[Sample Quantile|sample quantiles]]
> $$
> \begin{align}
> Y_1 \ (\text{minimum}), \quad Q_1 = Y_{0.25(n+1)}, \quad Q_2 \ (\text{sample median}), \quad Q_3 = Y_{0.75(n+1)}, \quad Y_n \ (\text{maximum})
> \end{align}
> $$

It summarizes location ($Q_2$), spread ($Q_3 - Q_1$, the sample [[Interquartile Range]]; $Y_n - Y_1$, the range), and asymmetry (the relative distances of $Q_1$ and $Q_3$ from $Q_2$).

# Properties
- The basis of the [[Boxplot]].
- Its middle three values are robust to outliers, while the extremes $Y_1, Y_n$ are very sensitive to them.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=274)
