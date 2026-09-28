---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Sample Variance[^1]
> For a [[Random Sample]] $X_1, \dots, X_n$ with [[Sample Mean]] $\bar{X}$, the sample variance is
> $$
> \begin{align}
> S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2 = \frac{1}{n-1}\left(\sum_{i=1}^n X_i^2 - n\bar{X}^2\right)
> \end{align}
> $$
> If the common distribution has mean $\mu$ and variance $\sigma^2$, then
> $$
> \begin{align}
> E(S^2) = \sigma^2
> \end{align}
> $$

Proof: using $E(X_i^2) = \sigma^2 + \mu^2$ and $E(\bar{X}^2) = \sigma^2/n + \mu^2$,
$$
\begin{align}
E(S^2) = \frac{1}{n-1}\left(\sum_{i=1}^n E(X_i^2) - nE(\bar{X}^2)\right) = \frac{1}{n-1}\left\{n\sigma^2 + n\mu^2 - n\left[\frac{\sigma^2}{n} + \mu^2\right]\right\} = \sigma^2
\end{align}
$$

**Why $n - 1$.** The deviations are measured from $\bar{X}$, which is fitted from the same data, rather than from the unknown $\mu$. Since $\bar{X}$ minimizes $\sum_i (X_i - c)^2$ over $c$, $\sum_i (X_i - \bar{X})^2 \leq \sum_i (X_i - \mu)^2$, so dividing by $n$ systematically underestimates $\sigma^2$:
$$
\begin{align}
E\left[\frac{1}{n}\sum_{i=1}^n (X_i - \bar{X})^2\right] = \frac{n-1}{n}\sigma^2
\end{align}
$$
The $n$ deviations $X_i - \bar{X}$ sum to $0$, so only $n - 1$ of them are free (one degree of freedom is spent estimating $\mu$). Dividing by $n - 1$ (Bessel's correction) removes the bias exactly. If $\mu$ were known, $\frac{1}{n}\sum_i (X_i - \mu)^2$ would already be unbiased.

**Which estimator is biased, and in which framework.** The biased estimator is the divide-by-$n$ one, $\hat{\sigma}^2 = \frac{1}{n}\sum_i (X_i - \bar{X})^2$. It is the plug-in (method of moments) estimator, and it is also the [[Maximum Likelihood Estimation|maximum likelihood estimator]] of $\sigma^2$ for a normal sample. $S^2$ is its bias-corrected version. "Bias" itself is a frequentist notion: $E(\hat{\theta}) - \theta$ averages over repeated samples with the parameter held fixed, and the $n - 1$ correction exists to satisfy the frequentist criterion of [[Unbiased Estimator|unbiasedness]]. Other estimators are built on other criteria and generally do not use $n - 1$:
- Bayesian estimators, such as the posterior mean of $\sigma^2$, depend on the prior and are typically biased in the frequentist sense. Unbiasedness is not a design goal in the [[Probability Bayesian Framework|Bayesian framework]], which conditions on the observed data rather than averaging over hypothetical samples.
- Unbiasedness is not the same as accuracy: for a normal sample, dividing by $n + 1$ gives the smallest [[Mean Squared Error]] among estimators of the form $c\sum_i (X_i - \bar{X})^2$, trading a little bias for less variance ([[Bias-Variance-MSE Decomposition of an Estimator]]).
- $S^2$ is unbiased for $\sigma^2$, but $S$ is still biased for $\sigma$ (by [[Jensen's Inequality]], $E(S) \leq \sqrt{E(S^2)} = \sigma$), so unbiasedness is not preserved by nonlinear reparametrization.

All three estimators ($1/(n-1)$, $1/n$, $1/(n+1)$) differ by $O(1/n)$ and are consistent, so the choice matters only for small samples.

# Properties
- The computational form $\sum X_i^2 - n\bar{X}^2$ is algebraically equal but numerically unstable when $\bar{X}$ is large relative to the spread; the two-pass or Welford update is used in practice.
- For a normal sample, $(n-1)S^2/\sigma^2$ has a [[Chi-Squared Distribution]] with $n - 1$ degrees of freedom, independent of $\bar{X}$.
- The sample analogue of the population [[Variance]]; $S$ is the sample [[Standard Deviation]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=169)
