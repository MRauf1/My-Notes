---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Normal Distribution Linear Combination[^1]
> Let $X_1, \dots, X_n$ be [[Mutually Independent Random Variables|independent]] with $X_i \sim N(\mu_i, \sigma_i^2)$, and let $Y = \sum_{i=1}^n a_i X_i$ for constants $a_i$. Then
> $$
> \begin{align}
> Y \sim N\left(\sum_{i=1}^n a_i \mu_i, \sum_{i=1}^n a_i^2 \sigma_i^2\right)
> \end{align}
> $$

> [!abstract] Corollary 1 (Sample Mean of a Normal Sample)[^1]
> If $X_1, \dots, X_n$ are [[Independent and Identically Distributed|iid]] $N(\mu, \sigma^2)$, then $\bar{X} = n^{-1}\sum_i X_i \sim N(\mu, \sigma^2/n)$.

Proof: the [[Moment Generating Function Technique]] gives $M_Y(t) = \prod_i \exp(a_i\mu_i t + \tfrac12 a_i^2\sigma_i^2 t^2)$, the mgf of the stated normal. The mean and variance follow from the general rules for a [[Linear Combination of Random Variables]]; what is special is that the result stays normal.

# Properties
- Holds without independence if $(X_1, \dots, X_n)$ is jointly [[Multivariate Normal Distribution|multivariate normal]], with variance $\mathbf{a}^T\Sigma\mathbf{a}$ ([[Multivariate Normal Distribution Affine Transformation]]).
- Marginal normality of each $X_i$ alone is not enough without independence or joint normality.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=209)
