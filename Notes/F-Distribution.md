---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] F-Distribution[^1]
> Let $U \sim \chi^2(r_1)$ and $V \sim \chi^2(r_2)$ be independent [[Chi-Squared Distribution|chi-squared]] variables. Then
> $$
> \begin{align}
> F = \frac{U/r_1}{V/r_2}
> \end{align}
> $$
> has the F-distribution with $r_1$ (numerator) and $r_2$ (denominator) degrees of freedom, with pdf
> $$
> \begin{align}
> g_1(w) = \frac{\Gamma[(r_1 + r_2)/2]\,(r_1/r_2)^{r_1/2}}{\Gamma(r_1/2)\,\Gamma(r_2/2)}\frac{w^{r_1/2 - 1}}{(1 + r_1 w/r_2)^{(r_1 + r_2)/2}}, \quad 0 < w < \infty
> \end{align}
> $$
> and zero elsewhere.

$F$ is a ratio of two independent variance estimates, each scaled by its degrees of freedom; it compares the spread explained by two sources, which is why it appears in comparing two normal variances and in ANOVA and regression tests ([[F-Test Statistic]]).

# Properties
- Moments:[^2] $E(F^k) = (r_2/r_1)^k E(U^k) E(V^{-k})$ exists if and only if $r_2 > 2k$. In particular $E(F) = \frac{r_2}{r_2 - 2}$ for $r_2 > 2$, which is close to $1$ for large $r_2$.
- $1/F \sim F(r_2, r_1)$.
- If $T$ has a [[t-Distribution]] with $r$ degrees of freedom, $T^2 \sim F(1, r)$.
- $\frac{r_1 F / r_2}{1 + r_1 F/r_2} = \frac{U}{U + V} \sim$ [[Beta Distribution|Beta]]$(r_1/2, r_2/2)$.
- As $r_2 \to \infty$, $r_1 F \to \chi^2(r_1)$ in distribution.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=229)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=230)
