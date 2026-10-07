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

Equivalently (Hogg Theorem 5.3.1),[^2] $Y_n = \frac{\sum_{i=1}^n X_i - n\mu}{\sqrt{n}\,\sigma} \xrightarrow{D} N(0, 1)$, or in the often more convenient form $\sqrt{n}(\bar{X} - \mu) \xrightarrow{D} N(0, \sigma^2)$ ([[Convergence in Distribution]]). For normal samples this holds exactly for every $n$.

> [!abstract] Theorem 2 (Multivariate Central Limit Theorem)[^3]
> Let $\{\mathbf{X}_n\}$ be iid random vectors with mean vector $\boldsymbol{\mu}$ and positive definite covariance matrix $\Sigma$, whose common mgf exists near $\mathbf{0}$. Then
> $$
> \begin{align}
> \mathbf{Y}_n = \frac{1}{\sqrt{n}}\sum_{i=1}^n(\mathbf{X}_i - \boldsymbol{\mu}) = \sqrt{n}(\bar{\mathbf{X}} - \boldsymbol{\mu}) \xrightarrow{D} N_p(\mathbf{0}, \Sigma)
> \end{align}
> $$
> (The mgf assumption is for Hogg's proof; finite second moments suffice.)

Whatever the shape of the population (as long as its variance is finite), the standardized [[Sample Mean]] is approximately normal for large $n$. The exact normality for normal samples ([[Normal Distribution Linear Combination]]) becomes approximate normality for all finite-variance samples.

# Properties
- Justifies large-sample (approximate) [[Confidence Interval|confidence intervals]] $\bar{x} \pm z_{\alpha/2}\,s/\sqrt{n}$ and $z$-tests, with $\sigma$ replaced by the sample standard deviation.
- Equivalently $\sqrt{n}(\bar{X} - \mu) \to N(0, \sigma^2)$ in distribution; the error of $\bar{X}$ shrinks at rate $\sigma/\sqrt{n}$, which is the [[Monte Carlo Convergence Rate]].
- Explains the normal approximations to the [[Binomial Distribution Normal Approximation|binomial]], [[Poisson Distribution Normal Approximation|Poisson]], and [[Chi-Squared Distribution Normal Approximation|chi-squared]] distributions, which are sums of iid variables.
- Fails without finite variance: sample means of the [[Cauchy Distribution]] never become normal.
- This is why the normal distribution is central to statistics:[^4] few populations are normal, but the distributions of statistics computed from samples are often nearly normal. The theorem is stated for the sample mean, but it extends to most common statistics (the sample variance, sample quantiles, regression coefficients, maximum likelihood and M-estimators) via the [[Delta Method]], [[Slutsky's Theorem]], and asymptotic normality results; the sample mean is not special in having good convergence properties.
- The limit is used through the [[Multivariate Normal Distribution]] in the vector case.
- In Monte Carlo it gives $\hat{\mu}_n - \mu \approx N(0, \sigma^2/n)$ and hence the [[Monte Carlo Confidence Interval]]; the vector form $\sqrt{n}(\bar{Y} - \mu) \xrightarrow{D} N(0, \Sigma)$ needs only a finite covariance matrix $\Sigma$.[^5]
- If $\sigma^2 < \infty$ but the third moment is large or infinite, the normal approximation sets in more slowly; its speed is governed by $E|Y - \mu|^3/\sigma^3$ (Berry–Esseen) ([[Infinite Moments in Monte Carlo]]).[^6]

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=256)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=358)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=367)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=362)
[^5]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=19&annotation=288EKVRQ); [Owen](zotero://open-pdf/library/items/TXMSRRI3?page=19&annotation=VHXGC27L)
[^6]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/TXMSRRI3?page=35&annotation=TV4U9UKC)
