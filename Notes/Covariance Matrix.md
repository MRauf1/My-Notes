---
tags:
  - statistics
  - categorical_variable_prediction
  - mathematical_statistics
---

# Definition

> [!info] Definition 1 ([[Covariance]] [[Matrix]])
> Matrix with the [[Variance]] on the diagonals and [[Covariance]] everywhere else
> $$
> \begin{align}
> Cov[\mathbf{Z}] = \begin{bmatrix}Var[Z_1] & Cov[Z_1, Z_2] & \dots & Cov[Z_1, Z_m] \\ Cov[Z_2, Z_1] & Var[Z_2] & \dots & \dots \\ \vdots & \vdots & \vdots & \vdots \\ Cov[Z_m, Z_1] & \dots & \dots & Var[Z_m]\end{bmatrix}
> \end{align}
> $$

> [!info] Definition 2 (Variance-Covariance Matrix)[^1]
> Let $\mathbf{X} = (X_1, \dots, X_n)^T$ be a [[Random Vector]] with $\sigma_i^2 = \text{Var}(X_i) < \infty$ and [[Mean Vector|mean]] $\boldsymbol{\mu} = E[\mathbf{X}]$. Its variance-covariance matrix is the [[Expectation of Random Matrix|expectation of the random matrix]]
> $$
> \begin{align}
> \text{Cov}(\mathbf{X}) = E\left[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T\right] = [\sigma_{ij}]
> \end{align}
> $$
> whose $i$th diagonal entry is $\sigma_{ii} = \sigma_i^2 = \text{Var}(X_i)$ and $(i, j)$th off-diagonal entry is $\sigma_{ij} = \text{Cov}(X_i, X_j)$.

The outer product $(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T$ collects all pairwise products of centered components, so its expectation holds every variance and covariance at once. It is the $n$-dimensional analogue of $\sigma^2$.

> [!abstract] Theorem 1 (Covariance Matrix Identities)[^1]
> Let $\mathbf{X}$ be an $n$-dimensional random vector with finite variances and $\mathbf{A}$ an $m \times n$ constant matrix. Then
> $$
> \begin{align}
> \text{Cov}(\mathbf{X}) &= E[\mathbf{X}\mathbf{X}^T] - \boldsymbol{\mu}\boldsymbol{\mu}^T \\
> \text{Cov}(\mathbf{A}\mathbf{X}) &= \mathbf{A}\,\text{Cov}(\mathbf{X})\,\mathbf{A}^T
> \end{align}
> $$

These are the matrix versions of $\text{Var}(X) = E(X^2) - \mu^2$ and $\text{Var}(aX) = a^2\,\text{Var}(X)$ ([[Variance Basic Properties]]), and follow from [[Expectation of Random Matrix|linearity for random matrices]].

# Properties
- Symmetric: $\text{Cov}(\mathbf{X})^T = \text{Cov}(\mathbf{X})$, since $\text{Cov}(X_i, X_j) = \text{Cov}(X_j, X_i)$, i.e. $(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T$ is symmetric. For a complex random vector the covariance matrix is defined as $E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^H]$ with the [[Matrix Conjugate Transpose|conjugate transpose]], and it is Hermitian. In both cases it is a [[Self-Adjoint Linear Map|self-adjoint]] matrix, so the spectral theorem gives real eigenvalues and an orthonormal eigenbasis (the principal axes).
- [[Positive Semidefinite Matrix|Positive semidefinite]]:[^2] for every constant $\mathbf{a} \in \mathbb{R}^n$, $Y = \mathbf{a}^T\mathbf{X}$ is a random variable, so
$$
\begin{align}
0 \leq \text{Var}(\mathbf{a}^T \mathbf{X}) = \mathbf{a}^T\,\text{Cov}(\mathbf{X})\,\mathbf{a}
\end{align}
$$
  Hence all eigenvalues are $\geq 0$. It is singular exactly when some nontrivial linear combination $\mathbf{a}^T\mathbf{X}$ is constant with probability one, i.e. the distribution lies in a proper affine subspace.
- Its diagonal entries are the variances, so $\text{tr}\,\text{Cov}(\mathbf{X}) = \sum_i \text{Var}(X_i) = E\lVert \mathbf{X} - \boldsymbol{\mu} \rVert^2$.
- Diagonal for [[Mutually Independent Random Variables|independent]] (or merely pairwise uncorrelated) components.
- Normalizing by the standard deviations gives the correlation matrix $[\rho_{ij}]$ ([[Correlation]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=157)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=158)
