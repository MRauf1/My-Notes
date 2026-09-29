---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Order Statistics[^1]
> Let $X_1, \dots, X_n$ be a [[Random Sample]] from a continuous distribution with pdf $f$, cdf $F$, and support $(a, b)$. Arranged in ascending order they are $Y_1 < Y_2 < \dots < Y_n$, and $Y_i$ is the $i$th order statistic. Their joint pdf is
> $$
> \begin{align}
> g(y_1, \dots, y_n) = n!\,f(y_1)f(y_2)\cdots f(y_n), \quad a < y_1 < y_2 < \dots < y_n < b
> \end{align}
> $$
> and zero elsewhere.

The factor $n!$ counts the orderings of the sample that produce the same sorted vector: sorting is an $n!$-to-one map, and each piece contributes the same density ([[Random Vector Transformation]], piecewise case). Ties have probability $0$ for continuous distributions.

> [!abstract] Theorem 1 (Marginal pdf of $Y_k$)[^2]
> $$
> \begin{align}
> g_k(y_k) = \frac{n!}{(k-1)!(n-k)!}[F(y_k)]^{k-1}[1 - F(y_k)]^{n-k}f(y_k), \quad a < y_k < b
> \end{align}
> $$

> [!abstract] Theorem 2 (Joint pdf of $Y_i < Y_j$)[^3]
> $$
> \begin{align}
> g_{ij}(y_i, y_j) = \frac{n!}{(i-1)!(j-i-1)!(n-j)!}[F(y_i)]^{i-1}[F(y_j) - F(y_i)]^{j-i-1}[1 - F(y_j)]^{n-j}f(y_i)f(y_j)
> \end{align}
> $$
> for $a < y_i < y_j < b$.

**Heuristic derivation (multinomial).**[^3] $P(y_i < Y_i < y_i + \Delta_i, y_j < Y_j < y_j + \Delta_j)$ is approximately a [[Multinomial Distribution|multinomial]] probability over $n$ independent trials: $i - 1$ observations below $y_i$ (probability $F(y_i)$ each), one in $(y_i, y_i + \Delta_i)$ (probability $\approx f(y_i)\Delta_i$), $j - i - 1$ between (probability $\approx F(y_j) - F(y_i)$), one in $(y_j, y_j + \Delta_j)$ (probability $\approx f(y_j)\Delta_j$), and $n - j$ above (probability $1 - F(y_j)$). The multinomial coefficient and the product of these probabilities give $g_{ij}(y_i, y_j)\Delta_i\Delta_j$. The same bookkeeping gives any joint pdf of order statistics.

# Properties
- Statistics built from order statistics:[^4] the sample range $Y_n - Y_1$, the sample midrange $(Y_1 + Y_n)/2$, and the sample median $Q_2 = Y_{(n+1)/2}$ ($n$ odd) or $(Y_{n/2} + Y_{n/2+1})/2$ ($n$ even); see also [[Sample Quantile]] and [[Median]].
- The extremes: $g_n(y) = n[F(y)]^{n-1}f(y)$ and $g_1(y) = n[1 - F(y)]^{n-1}f(y)$ ([[Cumulative Distribution Function Method]]).
- $F(Y_k)$ is the $k$th order statistic of a uniform sample and has a [[Beta Distribution|Beta]]$(k, n - k + 1)$ distribution ([[Probability Integral Transform]]).
- Order-statistic methods are distribution-free: [[Distribution-Free Confidence Interval for Quantile]], [[Tolerance Interval]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=270)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=271)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=272)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=273)
