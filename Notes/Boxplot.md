---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Boxplot (Tukey Box-and-Whisker Plot)[^1]
> A plot of the [[Five-Number Summary]] in which a box spans $Q_1$ to $Q_3$ (the middle $50\%$ of the data), with a line at the median $Q_2$. With $h = 1.5(Q_3 - Q_1)$, define the lower and upper fences
> $$
> \begin{align}
> LF = Q_1 - h, \qquad UF = Q_3 + h
> \end{align}
> $$
> Points outside $(LF, UF)$ are potential outliers and are plotted individually; the whiskers extend from the box to the adjacent points, the most extreme observations still inside the fences.

The fences keep the extreme [[Order Statistic|order statistics]], which are very sensitive to outliers, from dictating the picture.

# Properties
- The fences use the sample [[Interquartile Range]], so they are robust to the outliers they are meant to flag.
- For normal data only a small fraction of observations fall outside the fences, so many flagged points suggest heavier tails than normal (e.g. a [[Contaminated Normal Distribution]]).
- A compact visual comparison of the location, spread, and skewness of several samples.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=275)
