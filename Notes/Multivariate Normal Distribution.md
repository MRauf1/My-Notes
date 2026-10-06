---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Multivariate Normal Distribution[^1]
> An $n$-dimensional [[Random Vector]] $\mathbf{X}$ has a multivariate normal distribution $N_n(\boldsymbol{\mu}, \Sigma)$ if its [[Moment Generating Function of Random Vector|mgf]] is
> $$
> \begin{align}
> M_{\mathbf{X}}(\mathbf{t}) = \exp\left\{\mathbf{t}^T\boldsymbol{\mu} + \frac{1}{2}\mathbf{t}^T\Sigma\,\mathbf{t}\right\}, \quad \mathbf{t} \in \mathbb{R}^n
> \end{align}
> $$
> where $\boldsymbol{\mu} \in \mathbb{R}^n$ and $\Sigma$ is a symmetric [[Positive Semidefinite Matrix|positive semidefinite]] matrix.

> [!info] Standard Multivariate Normal[^2]
> If $Z_1, \dots, Z_n$ are [[Independent and Identically Distributed|iid]] $N(0, 1)$, then $\mathbf{Z} = (Z_1, \dots, Z_n)^T$ has pdf and mgf
> $$
> \begin{align}
> f_{\mathbf{Z}}(\mathbf{z}) = \left(\frac{1}{2\pi}\right)^{n/2}\exp\left\{-\frac12\mathbf{z}^T\mathbf{z}\right\}, \qquad M_{\mathbf{Z}}(\mathbf{t}) = \exp\left\{\frac12\mathbf{t}^T\mathbf{t}\right\}
> \end{align}
> $$
> with $E[\mathbf{Z}] = \mathbf{0}$ and $\text{Cov}[\mathbf{Z}] = I_n$, i.e. $\mathbf{Z} \sim N_n(\mathbf{0}, I_n)$.

**Construction.**[^1] For $\mathbf{Z} \sim N_n(\mathbf{0}, I_n)$, define $\mathbf{X} = \Sigma^{1/2}\mathbf{Z} + \boldsymbol{\mu}$ with the [[Matrix Square Root]] $\Sigma^{1/2}$. Then $E[\mathbf{X}] = \boldsymbol{\mu}$, $\text{Cov}[\mathbf{X}] = \Sigma^{1/2}\Sigma^{1/2} = \Sigma$ ([[Covariance Matrix]]), and
$$
\begin{align}
M_{\mathbf{X}}(\mathbf{t}) = e^{\mathbf{t}^T\boldsymbol{\mu}} E\left[e^{(\Sigma^{1/2}\mathbf{t})^T\mathbf{Z}}\right] = \exp\left\{\mathbf{t}^T\boldsymbol{\mu} + \tfrac12\mathbf{t}^T\Sigma\,\mathbf{t}\right\}
\end{align}
$$
So $\boldsymbol{\mu}$ is the [[Mean Vector]] and $\Sigma$ the covariance matrix, and every $N_n(\boldsymbol{\mu}, \Sigma)$ is an affine image of independent standard normals.

> [!info] Density (Positive Definite Case)[^1]
> If $\Sigma$ is [[Positive Definite Matrix|positive definite]], the map $\mathbf{Z} = \Sigma^{-1/2}(\mathbf{X} - \boldsymbol{\mu})$ is one-to-one with Jacobian $|\Sigma^{-1/2}| = |\Sigma|^{-1/2}$ ([[Random Vector Transformation]]), and
> $$
> \begin{align}
> f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}}\exp\left\{-\frac12(\mathbf{x} - \boldsymbol{\mu})^T\Sigma^{-1}(\mathbf{x} - \boldsymbol{\mu})\right\}, \quad \mathbf{x} \in \mathbb{R}^n
> \end{align}
> $$

**Positive definite vs. positive semidefinite $\Sigma$.** $\Sigma$ is always positive semidefinite, but not always positive definite; defining the distribution through the mgf allows both.
- $\Sigma$ is positive definite (all eigenvalues $> 0$, invertible) exactly when the distribution is non-degenerate: no nontrivial linear combination $\mathbf{a}^T\mathbf{X}$ has zero variance, i.e. no component is constant or an exact linear combination of the others, so the $n$ coordinates carry $n$ genuine degrees of freedom. Only then does the density above exist.
- $\Sigma$ is singular (some eigenvalues $= 0$) exactly when the distribution is degenerate: $\text{Var}(\mathbf{a}^T\mathbf{X}) = \mathbf{a}^T\Sigma\mathbf{a} = 0$ for $\mathbf{a}$ in the null space, so $\mathbf{X}$ lies with probability one in the lower-dimensional affine subspace $\boldsymbol{\mu} + \text{col}(\Sigma)$ of dimension $r = \text{rank}\,\Sigma$ (constant components, or perfectly collinear ones). Since that subspace has zero volume in $\mathbb{R}^n$, there is no density with respect to $n$-dimensional [[Lebesgue Measure]], and the formula above breaks down ($|\Sigma| = 0$, $\Sigma^{-1}$ undefined).
- The degenerate distribution is still a perfectly valid multivariate normal: the mgf definition and the construction $\Sigma^{1/2}\mathbf{Z} + \boldsymbol{\mu}$ still work, and on its $r$-dimensional subspace it has the density $(2\pi)^{-r/2}(\text{pdet}\,\Sigma)^{-1/2}\exp\{-\frac12(\mathbf{x} - \boldsymbol{\mu})^T\Sigma^{+}(\mathbf{x} - \boldsymbol{\mu})\}$, using the [[Pseudoinverse]] $\Sigma^+$ and the pseudo-determinant (product of nonzero eigenvalues).

# Types
- [[Bivariate Normal Distribution]] ($n = 2$).
- The univariate [[Normal Distribution]] ($n = 1$).

# Properties
- Quadratic form:[^3] if $\Sigma$ is positive definite, $Y = (\mathbf{X} - \boldsymbol{\mu})^T\Sigma^{-1}(\mathbf{X} - \boldsymbol{\mu}) \sim$ [[Chi-Squared Distribution|$\chi^2(n)$]], since $Y = \mathbf{Z}^T\mathbf{Z} = \sum Z_i^2$. $\sqrt{Y}$ is the Mahalanobis distance, and the contours of the density are the ellipsoids $\{Y = c\}$. In the degenerate case, $(\mathbf{X}-\boldsymbol{\mu})^T\Sigma^+(\mathbf{X}-\boldsymbol{\mu}) \sim \chi^2(r)$.
- [[Multivariate Normal Distribution Affine Transformation]]: $A\mathbf{X} + \mathbf{b} \sim N_m(A\boldsymbol{\mu} + \mathbf{b}, A\Sigma A^T)$; hence all marginals are normal.
- [[Multivariate Normal Distribution Independence]]: subvectors are independent iff uncorrelated.
- [[Multivariate Normal Distribution Conditional Distribution]]: conditionals are normal with linear mean and constant covariance.
- [[Multivariate Normal Density Product]]: a product of normal densities in the same variable is an unnormalized normal density (precisions add).
- [[Principal Component Analysis]]: rotating to the eigenbasis of $\Sigma$ gives independent components.
- Sampling: $\boldsymbol{\mu} + A\mathbf{Z}$ for any $AA^T = \Sigma$ ([[Multivariate Normal Sampling (Cholesky Factorization)]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=217)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=216)
[^3]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=218)
