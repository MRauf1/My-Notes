---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Square Root of a Positive Semidefinite Matrix[^1]
> Let $\Sigma$ be an $n \times n$ symmetric [[Positive Semidefinite Matrix|positive semidefinite]] matrix with spectral decomposition ([[Spectral Theorem]])
> $$
> \begin{align}
> \Sigma = V \Lambda V^T = \sum_{i=1}^n \lambda_i \mathbf{v}_i \mathbf{v}_i^T
> \end{align}
> $$
> where $\Lambda = \text{diag}(\lambda_1, \dots, \lambda_n)$ with $\lambda_1 \geq \dots \geq \lambda_n \geq 0$ the [[Eigenvalue|eigenvalues]], and $V$ an [[Orthogonal Matrix|orthogonal matrix]] whose columns $\mathbf{v}_i$ are the corresponding [[Eigenvector|eigenvectors]]. With $\Lambda^{1/2} = \text{diag}(\sqrt{\lambda_1}, \dots, \sqrt{\lambda_n})$, the square root of $\Sigma$ is
> $$
> \begin{align}
> \Sigma^{1/2} = V \Lambda^{1/2} V^T
> \end{align}
> $$
> which satisfies $\Sigma^{1/2}\Sigma^{1/2} = \Sigma$.

(Hogg et al. write the decomposition as $\Gamma^T\Lambda\Gamma$ with $\Gamma = V^T$.)

# Properties
- $\Sigma^{1/2}$ is symmetric and positive semidefinite, and it is the unique symmetric PSD square root of $\Sigma$.
- If $\Sigma$ is [[Positive Definite Matrix|positive definite]] (all $\lambda_i > 0$), then $\Sigma^{-1/2} := (\Sigma^{1/2})^{-1} = V\Lambda^{-1/2}V^T$, and $\Sigma^{-1/2}\Sigma\,\Sigma^{-1/2} = I$ (whitening).
- These powers obey the usual exponent laws, e.g. $\Sigma^{1/2}\Sigma^{-1/2} = I$ and $(\Sigma^{-1/2})^2 = \Sigma^{-1}$; it is a special case of a function of a matrix applied through the eigenvalues.
- Any $A$ with $AA^T = \Sigma$ can play the same role in constructing a [[Multivariate Normal Distribution]]; the symmetric root is canonical, while the triangular Cholesky factor is cheaper to compute ([[Multivariate Normal Sampling (Cholesky Factorization)]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=216)
