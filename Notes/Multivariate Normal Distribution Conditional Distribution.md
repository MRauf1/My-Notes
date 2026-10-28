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

> [!abstract] Theorem 1 (Arbitrary Index Subsets)[^3]
> Let $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \Sigma)$ on $\mathbb{R}^d$ and $u, v \subseteq \{1, \dots, d\}$. Write $\boldsymbol{\mu}_u, \boldsymbol{\mu}_v$ for the corresponding subvectors of $\boldsymbol{\mu}$ and $\Sigma_{uv}$ for the submatrix of $\Sigma$ with rows in $u$ and columns in $v$. If $\Sigma_{vv}$ is invertible, then
> $$
> \begin{align}
> \mathbf{X}_u \mid \mathbf{X}_v = \mathbf{x}_v \sim \mathcal{N}\left(\boldsymbol{\mu}_u + \Sigma_{uv}\Sigma_{vv}^{-1}(\mathbf{x}_v - \boldsymbol{\mu}_v),\ \Sigma_{uu} - \Sigma_{uv}\Sigma_{vv}^{-1}\Sigma_{vu}\right)
> \end{align}
> $$

Invertibility of $\Sigma_{vv}$ is no real restriction: conditioning on $\mathbf{X}_v$ only requires conditioning on its non-redundant components. Only $\Sigma_{vv}$, not all of $\Sigma$, needs to be invertible.

# Properties
- Closure under conditioning makes the multivariate normal ideal for [[Sequential Inversion|sequential]] sampling: one can first generate a linear combination such as $T = X_1 + \dots + X_d$, and later sample the $X_j$, or other linear combinations, conditionally on those already generated (apply the theorem to the jointly normal vector $(T, \mathbf{X})$).[^4]
- The [[Conditional Expectation|conditional mean]] is linear in the conditioning value (the regression line of the [[Linear Conditional Expectation Theorem]]), and the conditional covariance $\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21}$ (the Schur complement of $\Sigma_{22}$) does not depend on $\mathbf{x}_2$.
- Conditioning never increases uncertainty: $\Sigma_{11} - \Sigma_{12}\Sigma_{22}^{-1}\Sigma_{21} \preceq \Sigma_{11}$, the matrix form of the [[Law of Total Variance]].
- In the bivariate case, since the conditional variance is the same for every $x$, $99\%$ of the conditional probability lies in the band $\mu_2 + \rho\frac{\sigma_2}{\sigma_1}(x - \mu_1) \pm 2.576\,\sigma_2\sqrt{1 - \rho^2}$ about the regression line; the band narrows as $\rho^2 \to 1$, so $\rho$ measures the concentration of probability about the line ([[Correlation]]).
- Only $\Sigma_{22}$ must be invertible; with a singular $\Sigma_{22}$ the same formulas hold with the [[Pseudoinverse]] $\Sigma_{22}^+$.
- The basis of Gaussian process regression and the Kalman filter update.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=220)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=221)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=10&annotation=9T8F2TUW); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=10&annotation=FVTYF56F); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=8&annotation=DEZSUQCD)
[^4]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=10&annotation=ZAD4RQZZ)
