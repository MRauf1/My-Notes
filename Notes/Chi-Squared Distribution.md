---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Chi-Squared [[Probability Distribution]])[^1][^2]
> With [[Function Support]] $(0, \infty)$, denoted as $\chi^2(k)$, where $k$ is the [[Degree of Freedom]].
> $$
> \begin{align}
> f(x) = \frac{1}{2^{k/2} \Gamma(k/2)} x^{k/2 - 1} exp[-x / 2]
> \end{align}
> $$
> with mgf $M(t) = (1 - 2t)^{-k/2}$ for $t < \frac12$.

It is the [[Probability Distribution]] of a sum of squares of $k$ [[Independent Random Variable|independent]] standard [[Normal Distribution|normal]] [[Random Variable]].

If $X \sim \chi^2(k)$, then $X \sim Gamma(\alpha = k/2, \theta = 2)$, so it is a special case of the [[Gamma Distribution]].

**Degrees of freedom.** $k$ counts the independent standard normal components being squared and summed, i.e. the number of independent directions in which the underlying normal vector is free to vary. Linear constraints remove degrees of freedom: the residuals $X_i - \bar{X}$ of a normal sample satisfy $\sum_i (X_i - \bar{X}) = 0$, so they span only $n - 1$ free directions and $(n-1)S^2/\sigma^2 \sim \chi^2(n - 1)$ ([[Student's Theorem]]). More generally, a sum of squares of normal residuals after fitting $p$ linear parameters has $n - p$ degrees of freedom.

**Use.** It is the distribution of squared lengths of standard normal vectors, so it arises wherever squared normal deviations are summed: the [[Sample Variance]] of normal data, squared Mahalanobis distances of a [[Multivariate Normal Distribution]], Pearson's goodness-of-fit statistic, and the asymptotic distribution of likelihood ratio statistics. It is also the building block of the [[t-Distribution]] and [[F-Distribution]].

# Properties
## Basic Statistical Properties
- [[Chi-Squared Distribution Expectation]]
- [[Chi-Squared Distribution Variance]]
- Moments:[^3] for $k' > -k/2$, $E(X^{k'}) = \frac{2^{k'}\Gamma\left(\frac{k}{2} + k'\right)}{\Gamma\left(\frac{k}{2}\right)}$; every nonnegative integer $k'$ satisfies the condition, so all positive moments exist. In particular $E(X) = k$ and $\text{Var}(X) = 2k$. Negative moments exist only for $k' > -k/2$, which is what limits the moments of the $t$ and $F$ distributions.

## [[Probability Distribution Skewness]]
- [[Chi-Squared Distribution Skewness]]

# [[Addition]]
- [[Chi-Squared Distribution Addition]]

## [[Approximation]]
- [[Chi-Squared Distribution Normal Approximation]]

## Relation with [[Normal Distribution]]
- [[Chi-Squared Random Variable and Normal Random Variable]]

[^1]: [Categorical Data Analysis](zotero://open-pdf/library/items/JZKRKD5L?page=26)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=194)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=195)
