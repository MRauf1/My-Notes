---
tags:
  - statistics
  - bayesian_statistics
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 (Normal [[Probability Distribution]])[^1][^2]
> Normal (also known as Gaussian) distribution, with [[Function Support]] $(-\infty, \infty)$, denoted as $N(\mu, \sigma^2)$ is
> $$
> \begin{align}
> f(x) = \frac{1}{\sigma \sqrt{2 \pi}} exp[-\frac{1}{2 \sigma^2} (x - \mu)^2]
> \end{align}
> $$
> where $\mu$ and $\sigma^2$ are its mean and variance. $Z \sim N(0, 1)$ is a standard normal random variable, with cdf $\Phi$ and pdf $\phi$.

> [!abstract] Theorem 1 (Standardization)[^2]
> $X \sim N(\mu, \sigma^2)$ if and only if $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$. Equivalently, $X = \mu + \sigma Z$, the location model $X = \mu + e$ with random error $e \sim N(0, \sigma^2)$.

# Types
- [[Multivariate Normal Distribution]] and [[Bivariate Normal Distribution]].
- [[Contaminated Normal Distribution]], a normal mixture with occasional outliers.

# Properties
## Basic Statistical Properties
- [[Normal Distribution Expectation]]
- [[Normal Distribution Variance]]
- [[Moment Generating Function|mgf]]:[^2] $M(t) = E[e^{t(\sigma Z + \mu)}] = \exp\{\mu t + \frac12\sigma^2 t^2\}$ for all $t$, from the standard normal mgf $e^{t^2/2}$.
- All moments:[^3] $E(X^k) = \sum_{j=0}^k \binom{k}{j}\sigma^j E(Z^j)\mu^{k-j}$ by the [[Binomial Theorem]], where the odd moments of $Z$ vanish and $E(Z^{2m}) = \frac{(2m)!}{2^m m!}$.

## Shape
- The pdf is symmetric about $\mu$, has maximum $1/(\sigma\sqrt{2\pi})$ at $x = \mu$, has the $x$-axis as horizontal asymptote, and has points of inflection at $\mu \pm \sigma$.[^2]
- By symmetry, the [[Median]] (and [[Mode]]) equals the mean, and $\Phi(-z) = 1 - \Phi(z)$.[^4]
- $\mu$ is a [[Location Parameter]] and $\sigma$ a [[Scale Parameter]]: changing them shifts or stretches the same bell shape.[^5]
- [[Kurtosis]] $3$ and all cumulants beyond the second are $0$ ([[Cumulant Generating Function]]).

## Related Distributions
- $V = (X - \mu)^2/\sigma^2 \sim \chi^2(1)$ ([[Chi-Squared Random Variable and Normal Random Variable]]).[^3]
- [[Normal Distribution Linear Combination]]: linear combinations of independent normals are normal; in particular $\bar{X} \sim N(\mu, \sigma^2/n)$.
- [[Student's Theorem]]: for a normal sample, $\bar{X}$ and $S^2$ are independent and $(\bar{X} - \mu)/(S/\sqrt{n})$ has a [[t-Distribution]].

[^1]: [Bayesian Statistical Methods](zotero://open-pdf/library/items/ELV3M9SP?page=20)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=204)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=208)
[^4]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=206)
[^5]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=207)
