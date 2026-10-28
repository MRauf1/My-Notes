---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Multivariate Normal Sampling (Cholesky Factorization)[^1]
> To sample $\mathcal{N}(\mu, \Sigma)$: factor $AA^\top = \Sigma$ via [[Cholesky Decomposition]], draw a vector $z$ of independent standard normals componentwise (e.g. via the [[Box-Muller Transform]]), and return $\mu + Az$.

More generally, any $C$ with $CC^\top = \Sigma$ works: $\mathbf{X} = \mu + C\mathbf{Z}$ with $\mathbf{Z} \sim \mathcal{N}(\mathbf{0}, I)$ gives $\mathbf{X} \sim \mathcal{N}(\mu, \Sigma)$ by the [[Multivariate Normal Distribution Affine Transformation|affine transformation]] property. Choices of $C$:[^2]
- **Spectral.** Since $\Sigma$ is symmetric [[Positive Semidefinite Matrix|positive semidefinite]], it has an [[Eigendecomposition]] $\Sigma = P\Lambda P^\top$ ([[Spectral Theorem]]) with eigenvalues $\Lambda_{ii} \geq 0$ and eigenvectors as the columns of $P$; take the symmetric [[Matrix Square Root]] $C = P\Lambda^{1/2}P^\top$. This is often preferred.
- **Singular $\Sigma$.** $C$ can be $d \times r$ with $r = \mathrm{rank}\,\Sigma$, by dropping the eigenpairs with $\Lambda_{ii} = 0$. For singular or numerically nearly singular $\Sigma$, compute $\Sigma = U\,\mathrm{diag}(\sigma_1, \dots, \sigma_d)V^\top$ by the [[Singular Value Decomposition Theorem|SVD]] instead; here $U = V = P$ and the decomposition is the spectral one, but the SVD enforces $\sigma_i \geq 0$. Take $C = U\,\mathrm{diag}(\sqrt{\sigma_1}, \dots, \sqrt{\sigma_d})U^\top$.
- **Cholesky.** For positive definite $\Sigma$, take $C = L$ lower triangular with $LL^\top = \Sigma$ ([[Cholesky Decomposition]]). Easy to program, but $L$ can be numerically unreliable when $\Sigma$ is (nearly) singular, although the product $LL^\top$ remains reliable (Trefethen and Bau, 1997, Lecture 23).

# Properties
- Used for MALA/HMC proposals and every Gaussian primitive in Monte Carlo rendering.
- Finding the spectral or Cholesky factor costs $O(d^3)$, so closed-form factors for specially structured $\Sigma$ (e.g. the covariance of [[Brownian Motion]], whose Cholesky factor is explicit) are valuable when $d$ is very large.[^3]
- Alternatively, components or linear combinations can be generated in any order and the rest drawn from their Gaussian conditionals ([[Multivariate Normal Distribution Conditional Distribution]], [[Sequential Inversion]]).

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=8&annotation=ZHNJZERN); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=9&annotation=ZA72QYFU); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=9&annotation=YVX27XE3)
[^3]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=9&annotation=XEA3MYTF); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/I5B7ZUIV?page=9&annotation=YVX27XE3)
