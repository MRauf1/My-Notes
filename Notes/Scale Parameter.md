---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Scale Parameter[^1]
> A parameter $\sigma > 0$ is a scale parameter if changing it stretches or compresses the pdf without changing its shape: $f(x; \sigma) = \frac{1}{\sigma} f_0\left(\frac{x}{\sigma}\right)$, i.e. $X = \sigma X_0$ for a fixed $X_0$.

A small scale makes the pdf tall and narrow, a large scale makes it spread out and low. The standard deviation $\sigma$ of the [[Normal Distribution]] and $\beta$ of the [[Gamma Distribution]] are scale parameters.

# Properties
- Multiplying by $\sigma$ multiplies the standard deviation, [[Interquartile Range]], and all quantiles by $\sigma$; standardized quantities such as [[Probability Distribution Skewness|skewness]] and [[Kurtosis]] are unchanged.
- The reciprocal $\lambda = 1/\beta$ of a scale parameter is called a rate parameter (e.g. the [[Exponential Distribution]] rate, the events per unit time of a [[Poisson Process]]).
- Combined with a [[Location Parameter]] it gives a location-scale family; contrast with a [[Shape Parameter]].

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=207)
