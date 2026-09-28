---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Kurtosis[^1]
> Let $X$ be a [[Random Variable]] with mean $\mu$ and variance $\sigma^2$ such that the fourth central [[Moment (Statistics)|moment]] exists. The kurtosis of $X$ is
> $$
> \begin{align}
> \kappa = \frac{E[(X - \mu)^4]}{\sigma^4}
> \end{align}
> $$

Kurtosis measures the heaviness of the tails of a distribution relative to its variance. It is often described as "peakedness", but modern analysis shows it is dominated by tail behavior (values of $|X - \mu|$ beyond about $\sigma$) and says little about the shape of the peak.

# Properties
- Invariant under affine maps $aX + b$ with $a \neq 0$.
- $\kappa \geq 1 + \gamma^2 \geq 1$ where $\gamma$ is the [[Probability Distribution Skewness|skewness]]; $\kappa = 1$ only for a two-point symmetric distribution.
- A [[Normal Distribution]] has $\kappa = 3$; the excess kurtosis is $\kappa - 3$. The [[Laplace Distribution]] has $\kappa = 6$ and the [[Continuous Uniform Distribution]] has $\kappa = 9/5$.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=92)
