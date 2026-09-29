---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Q-Q Plot[^1][^2]
> Let $X_1, \dots, X_n$ be a [[Random Sample]] with [[Order Statistic|order statistics]] $Y_1 < \dots < Y_n$ and realized values $y_k$, and let $F$ be a known cdf. With $p_k = k/(n + 1)$ and theoretical quantiles $\xi_{Z, p_k} = F^{-1}(p_k)$, the q-q plot is the plot of $y_k$ versus $\xi_{Z, p_k}$, $k = 1, \dots, n$. With $F = \Phi$ it is a normal q-q plot.

**Why it works.** Suppose $X$ belongs to the location-scale family with cdf $F((x - a)/b)$, $b > 0$ ([[Location Parameter]], [[Scale Parameter]]), and let $Z = (X - a)/b$, which has the known cdf $F$. From $p = P(X \leq \xi_{X,p}) = P\left(Z \leq \frac{\xi_{X,p} - a}{b}\right)$,
$$
\begin{align}
\xi_{X,p} = b\,\xi_{Z,p} + a
\end{align}
$$
so the quantiles of $X$ are a linear function of those of $Z$. Each $y_k$ estimates $\xi_{X, p_k}$ ([[Sample Quantile]]), so the plot is approximately a straight line with slope $b$ and intercept $a$ exactly when the cdf of $X$ has the form $F((x - a)/b)$.

# Properties
- A diagnostic for a distributional assumption that does not require knowing the location and scale parameters.
- Systematic curvature reveals departures: an S-shape indicates tails lighter or heavier than $F$, and a bend at one end indicates skewness.
- Extends to comparing two samples by plotting their sample quantiles against each other.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=275)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=276)
