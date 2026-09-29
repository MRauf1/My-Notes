---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Central Limit Theorem[^1]
> Let $X_1, \dots, X_n$ be a [[Random Sample]] from a distribution with mean $\mu$ and finite variance $\sigma^2$. Then the cdf of
> $$
> \begin{align}
> W_n = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}}
> \end{align}
> $$
> converges to $\Phi$, the cdf of the standard [[Normal Distribution]], as $n \to \infty$.

Whatever the shape of the population (as long as its variance is finite), the standardized [[Sample Mean]] is approximately normal for large $n$. The exact normality for normal samples ([[Normal Distribution Linear Combination]]) becomes approximate normality for all finite-variance samples.

# Properties
- Justifies large-sample (approximate) [[Confidence Interval|confidence intervals]] $\bar{x} \pm z_{\alpha/2}\,s/\sqrt{n}$ and $z$-tests, with $\sigma$ replaced by the sample standard deviation.
- Equivalently $\sqrt{n}(\bar{X} - \mu) \to N(0, \sigma^2)$ in distribution; the error of $\bar{X}$ shrinks at rate $\sigma/\sqrt{n}$, which is the [[Monte Carlo Convergence Rate]].
- Explains the normal approximations to the [[Binomial Distribution Normal Approximation|binomial]], [[Poisson Distribution Normal Approximation|Poisson]], and [[Chi-Squared Distribution Normal Approximation|chi-squared]] distributions, which are sums of iid variables.
- Fails without finite variance: sample means of the [[Cauchy Distribution]] never become normal.
- The multivariate version: $\sqrt{n}(\bar{\mathbf{X}} - \boldsymbol{\mu}) \to N_k(\mathbf{0}, \Sigma)$ ([[Multivariate Normal Distribution]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=256)
