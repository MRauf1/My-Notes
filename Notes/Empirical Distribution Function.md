---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Empirical Distribution Function[^1]
> For a realized sample $x_1, \dots, x_n$, the empirical distribution function is
> $$
> \begin{align}
> \hat{F}_n(x) = \frac{1}{n}\#\{i : x_i \leq x\}
> \end{align}
> $$
> the discrete [[Cumulative Distribution Function|cdf]] that puts mass $1/n$ at each observed point $x_i$. It is an estimator of the population cdf $F(x)$.

It is the distribution of "picking one of the observed data points uniformly at random", and it is the model of the population used by the [[Bootstrap]].

# Properties
- A draw $x^*$ from $\hat{F}_n$ has $E(x^*) = \bar{x}$ and $\text{Var}(x^*) = \frac{1}{n}\sum_i (x_i - \bar{x})^2$ (the divisor-$n$ variance; compare [[Sample Variance]]).
- For each fixed $x$, $n\hat{F}_n(x) \sim$ [[Binomial Distribution|$b(n, F(x))$]], so $\hat{F}_n(x)$ is an [[Unbiased Estimator]] of $F(x)$ with variance $F(x)[1 - F(x)]/n$.
- $\hat{F}_n \to F$ uniformly in $x$ with probability one (Glivenko-Cantelli theorem), and plug-in estimators replace $F$ by $\hat{F}_n$ in a functional of $F$ (e.g. the [[Sample Mean]] and [[Sample Quantile|sample quantiles]]).
- Its jumps are at the [[Order Statistic|order statistics]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=320)
