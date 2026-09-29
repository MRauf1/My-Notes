---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Bivariate Normal Distribution[^1]
> $(X, Y)$ has a bivariate normal distribution if its pdf is
> $$
> \begin{align}
> f(x, y) = \frac{1}{2\pi\sigma_1\sigma_2\sqrt{1 - \rho^2}}e^{-q/2}, \quad -\infty < x, y < \infty
> \end{align}
> $$
> where
> $$
> \begin{align}
> q = \frac{1}{1 - \rho^2}\left[\left(\frac{x - \mu_1}{\sigma_1}\right)^2 - 2\rho\left(\frac{x - \mu_1}{\sigma_1}\right)\left(\frac{y - \mu_2}{\sigma_2}\right) + \left(\frac{y - \mu_2}{\sigma_2}\right)^2\right]
> \end{align}
> $$
> with $-\infty < \mu_i < \infty$, $\sigma_i > 0$, and $\rho^2 < 1$. Its mgf is
> $$
> \begin{align}
> M_{(X,Y)}(t_1, t_2) = \exp\left\{t_1\mu_1 + t_2\mu_2 + \frac12\left(t_1^2\sigma_1^2 + 2t_1t_2\rho\sigma_1\sigma_2 + t_2^2\sigma_2^2\right)\right\}
> \end{align}
> $$

It is the [[Multivariate Normal Distribution]] with $n = 2$, $\boldsymbol{\mu} = (\mu_1, \mu_2)^T$ and $\Sigma = \begin{bmatrix}\sigma_1^2 & \rho\sigma_1\sigma_2 \\ \rho\sigma_1\sigma_2 & \sigma_2^2\end{bmatrix}$; the condition $\rho^2 < 1$ is exactly positive definiteness of $\Sigma$.

# Properties
- Marginals: $M_{(X,Y)}(t_1, 0)$ shows $X \sim N(\mu_1, \sigma_1^2)$, and similarly $Y \sim N(\mu_2, \sigma_2^2)$.
- $E(XY) = \frac{\partial^2 M}{\partial t_1 \partial t_2}(0, 0) = \rho\sigma_1\sigma_2 + \mu_1\mu_2$, so $\text{Cov}(X, Y) = \rho\sigma_1\sigma_2$ and $\rho$ is the [[Correlation]] coefficient.
- $X$ and $Y$ are independent if and only if $\rho = 0$: at $\rho = 0$ the mgf factors ([[Multivariate Normal Distribution Independence]]).
- The conditional distributions are normal with linear means and constant variance $\sigma_2^2(1 - \rho^2)$ ([[Multivariate Normal Distribution Conditional Distribution]]).
- The density contours $q = c$ are ellipses centered at $(\mu_1, \mu_2)$, tilted along the direction of positive or negative correlation.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=214)
