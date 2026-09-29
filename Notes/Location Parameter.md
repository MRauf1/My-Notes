---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Location Parameter[^1]
> A parameter $\mu$ of a family of distributions is a location parameter if changing it only shifts the pdf along the axis without changing its shape: $f(x; \mu) = f_0(x - \mu)$ for a fixed pdf $f_0$. Equivalently, $X = \mu + e$ where the distribution of $e$ does not depend on $\mu$ (the location model).

For the [[Normal Distribution]], $\mu$ is a location parameter and $X = \mu + e$ with random error $e \sim N(0, \sigma^2)$; conversely any such $X$ is $N(\mu, \sigma^2)$.

# Properties
- Shifting by $\mu$ shifts the mean, median, and mode by $\mu$ and leaves the variance unchanged.
- Together with a [[Scale Parameter]] it forms a location-scale family $f(x; \mu, \sigma) = \frac{1}{\sigma} f_0\left(\frac{x - \mu}{\sigma}\right)$, e.g. normal, [[Laplace Distribution|Laplace]], [[Cauchy Distribution|Cauchy]], [[Continuous Uniform Distribution|uniform]].
- Contrast with a [[Shape Parameter]], which changes the form of the pdf.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=207)
