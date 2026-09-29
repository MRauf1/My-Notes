---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Multivariate Normal Distribution Conditional Distribution[^1]
> Let $\mathbf{X} \sim N_n(\boldsymbol{\mu}, \Sigma)$ be partitioned as $\mathbf{X} = (\mathbf{X}_1^T, \mathbf{X}_2^T)^T$ with $\boldsymbol{\mu} = (\boldsymbol{\mu}_1^T, \boldsymbol{\mu}_2^T)^T$ and $\Sigma = \begin{bmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{bmatrix}$, and assume $\Sigma$ is positive definite. Then
> $$
> \begin{align}
> \mathbf{X}_1 \mid \mathbf{X}_2 \sim N_m\left(\boldsymbol{\mu}_1 + \Sigma_{12}\Sigma_{22}^{-1}(\mathbf{X}_2 - \boldsymbol{\mu}_2),\ \Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}\right)
> \end{align}
> $$

Proof idea: $\mathbf{W} = \mathbf{X}_1 - \Sigma_{12}\Sigma_{22}^{-1}\mathbf{X}_2$ is an [[Multivariate Normal Distribution Affine Transformation|affine function]] of $\mathbf{X}$ with $\text{Cov}(\mathbf{W}, \mathbf{X}_2) = O$, so $\mathbf{W}$ is independent of $\mathbf{X}_2$ ([[Multivariate Normal Distribution Independence]]); then $\mathbf{X}_1 = \mathbf{W} + \Sigma_{12}\Sigma_{22}^{-1}\mathbf{X}_2$ given $\mathbf{X}_2$ is a normal shifted by a known amount.

> [!abstract] Corollary 1 (Bivariate Case)[^2]
> For the [[Bivariate Normal Distribution]] with means $\mu_1, \mu_2$, standard deviations $\sigma_1, \sigma_2$, and correlation $\rho$,
> $$
> \begin{align}
> Y \mid X = x &\sim N\left(\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1),\ \sigma_2^2(1 - \rho^2)\right) \\
> X \mid Y = y &\sim N\left(\mu_1 + \rho\frac{\sigma_1}{\sigma_2}(y - \mu_2),\ \sigma_1^2(1 - \rho^2)\right)
> \end{align}
> $$

# Properties
- The [[Conditional Expectation|conditional mean]] is linear in the conditioning value (the regression line of the [[Linear Conditional Expectation Theorem]]), and the conditional covariance $\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ (the Schur complement of $\Sigma_{22}$) does not depend on $\mathbf{x}_2$.
- Conditioning never increases uncertainty: $\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21} \preceq \Sigma_{11}$, the matrix form of the [[Law of Total Variance]].
- In the bivariate case, since the conditional variance is the same for every $x$, $99\%$ of the conditional probability lies in the band $\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1) \pm 2.576\,\sigma_2\sqrt{1 - \rho^2}$ about the regression line; the band narrows as $\rho^2 \to 1$, so $\rho$ measures the concentration of probability about the line ([[Correlation]]).
- Only $\Sigma_{22}$ must be invertible; with a singular $\Sigma_{22}$ the same formulas hold with the [[Pseudoinverse]] $\Sigma_{22}^+$.
- The basis of Gaussian process regression and the Kalman filter update.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=220)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=221)
