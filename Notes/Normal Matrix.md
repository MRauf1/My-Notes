---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Normal Matrix / Normal Linear Map)[^1]
> A [[Matrix]] $A \in M_n(\mathbb{C})$ is normal if $A^*A = AA^*$. A [[Linear Map]] $T \in \mathcal{L}(V)$ is normal if $T^*T = TT^*$.

> [!abstract] Theorem 2 (Matrix Characterization)[^2]
> A linear map $T$ is normal if and only if its matrix with respect to an [[Orthonormal Basis]] is normal.

Every [[Self-Adjoint Linear Map|self-adjoint map or Hermitian matrix]] is normal. Every [[Isometry (Linear Algebra)|isometry]] or [[Unitary Matrix|unitary matrix]] is normal too: if $T$ is an isometry, then $T^{-1} = T^*$ ([[Adjoint]]), so $TT^* = I = T^*T$.[^3]

> [!abstract] Lemma 3 (Lemma 5.21 -- Real/Imaginary Part Decomposition)[^4]
> Let $V$ be a complex inner product space and $T \in \mathcal{L}(V)$. Define $T_r := \frac{1}{2}(T + T^*)$ and $T_i := \frac{1}{2i}(T - T^*)$. Then $T_r$ and $T_i$ are both self-adjoint, and $T$ is normal if and only if $T_r T_i = T_i T_r$.

> [!abstract] Theorem 4 (Eigenvectors of $A$ and $A^*$ Coincide)
> If $A$ is normal and $Av = \lambda v$ for $v \neq 0$, then $A^*v = \bar\lambda v$. So $A$ and $A^*$ share exactly the same eigenvectors, but the eigenvalue that $A^*$ associates to a shared eigenvector is the complex conjugate of the eigenvalue $A$ associates to it.

> [!abstract] Theorem 5 (Exercise 5.4.19b)[^5]
> Let $V$ be a finite-dimensional inner product space over $\mathbb{C}$ and $T \in \mathcal{L}(V)$. Then $T$ is normal if and only if $V$ is the [[Orthogonal Direct Sum]] of the [[Eigenspace|eigenspaces]] of $T$.

Combined with the [[Spectral Theorem]], normality is exactly the necessary and sufficient condition for a linear map to be diagonalizable by an orthonormal basis.

# Properties
- [[Adjoint]]
- [[Self-Adjoint Linear Map]]
- [[Unitary Matrix]]
- [[Isometry (Linear Algebra)]]
- [[Spectral Theorem]]
- [[Eigenspace]]
- [[Orthogonal Direct Sum]]
- [[Eigendecomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=345)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=345)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=345)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=345)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=351)
