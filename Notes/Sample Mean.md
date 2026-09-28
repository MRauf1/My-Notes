---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Sample Mean[^1]
> For a [[Random Sample]] $X_1, \dots, X_n$ with common mean $\mu$ and variance $\sigma^2$, the sample mean is
> $$
> \begin{align}
> \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i
> \end{align}
> $$
> and it satisfies
> $$
> \begin{align}
> E(\bar{X}) = \mu, \qquad \text{Var}(\bar{X}) = \frac{\sigma^2}{n}
> \end{align}
> $$

$\bar{X}$ is the [[Linear Combination of Random Variables|linear combination]] with $a_i = 1/n$, so the moments follow from linearity of expectation and the variance formula for independent variables. It is the [[Arithmetic Mean]] of the observations, viewed as a random variable.

# Properties
- Since $E(\bar{X}) = \mu$, $\bar{X}$ is an [[Unbiased Estimator|unbiased]] estimator of $\mu$.
- Its standard deviation $\sigma/\sqrt{n}$ (the standard error) shrinks at rate $1/\sqrt{n}$, so $\bar{X}$ concentrates around $\mu$ ([[Chebyshev's Inequality]] gives $P(|\bar{X} - \mu| \geq \epsilon) \leq \sigma^2/(n\epsilon^2)$), and $\bar{X} \to \mu$ almost surely by the [[Strong Law of Large Numbers]].
- It is the [[Maximum Likelihood Estimation|maximum likelihood estimator]] of $\mu$ for a normal sample.
- If $\sigma^2 = \infty$ or the mean does not exist (e.g. the [[Cauchy Distribution]]), these properties fail.
- $E(\bar{X}^2) = \sigma^2/n + \mu^2$, used in computing the mean of the [[Sample Variance]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=168)
