---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Eigendecomposition)[^1]
> [[Matrix]] $A \in M_n(\mathbb{F})$ is [[Diagonalizable Matrix|diagonalizable]] if and only if there is a [[Basis]] $(v_1, \dots, v_n)$ of $\mathbb{F}^n$ such that for each $i = 1, \dots, n$, $v_i$ is an [[Eigenvector]] of $A$.
> In that case,
> $$
> A = S \begin{bmatrix}\lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_n \end{bmatrix} S^{-1}
> $$
> where $Av_i = \lambda_i v_i$ and $S = \begin{bmatrix}\mid & & \mid \\ v_1 & \dots & v_n \\ \mid & & \mid \end{bmatrix}$ ($S$ is the eigenvector matrix and the middle matrix is the [[Diagonal Matrix]] of [[Eigenvalue|eigenvalues]]).

This factorization $A = SDS^{-1}$ is called the eigendecomposition (or eigenvalue decomposition, EVD) of $A$. Only diagonalizable matrices admit such a factorization, and the pair $S, D$ is not unique (the eigenvectors can be rescaled, and both the columns of $S$ and the diagonal entries of $D$ can be reordered together).

When $A$ is [[Normal Matrix|normal]] — in particular [[Self-Adjoint Linear Map|Hermitian or, over $\mathbb{R}$, symmetric]] — the eigenvector matrix $S$ can be chosen [[Unitary Matrix|unitary]] (or [[Orthogonal Matrix|orthogonal]]), and this eigendecomposition is exactly the spectral decomposition of the [[Spectral Theorem]].

# Properties
- [[Diagonalizable Matrix]]
- [[Diagonalizable Linear Map]]
- [[Diagonalizable Matrix Linear Map]]
- [[Spectral Theorem]]
- [[Normal Matrix]]
- [[Self-Adjoint Linear Map]]
- [[Similar Matrix]]
- [[Eigenvalue]]
- [[Eigenvector]]
- [[Diagonal Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=224)
