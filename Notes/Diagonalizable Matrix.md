---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Diagonalizable [[Matrix]])[^2]
> [[Matrix]] $A \in M_n(\mathbb{F})$ is diagonalizable if $A$ is [[Similar Matrix]] to a [[Diagonal Matrix]].

> [!abstract] Theorem 2 (Alternative)
> [[Matrix]] $A \in M_n(\mathbb{F})$ is diagonalizable if and only if there is a [[Basis]] $(v_1, \dots, v_n)$ of $\mathbb{F}^n$ such that for each $i = 1, \dots, n$, $v_i$ is an [[Eigenvector]] of $A$.

The constructive form of Theorem 2 — writing out $A$ in terms of its eigenvector and eigenvalue matrices — is the [[Eigendecomposition]] of $A$.

# Types
- [[Diagonal Matrix]] (trivially diagonalizable, since $D = I \cdot D \cdot I^{-1}$)
- [[Self-Adjoint Linear Map|Hermitian Matrix]] / [[Self-Adjoint Linear Map|Symmetric Matrix]] (orthonormally diagonalizable, per the [[Spectral Theorem]])
- [[Normal Matrix]] (unitarily diagonalizable, per the [[Spectral Theorem]])
- [[Unitary Matrix]]
- [[Orthogonal Matrix]]

# Properties
- [[Diagonalizable Matrix Linear Map]]
- [[Spectral Theorem]]
- [[Eigendecomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=224)