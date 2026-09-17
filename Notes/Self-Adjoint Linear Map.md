---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Self-Adjoint Linear Map, Hermitian Matrix, Symmetric Matrix)[^1]
> A [[Linear Map]] $T \in \mathcal{L}(V)$ is self-adjoint if $T^* = T$. A [[Matrix]] $A \in M_n(\mathbb{C})$ is Hermitian if $A^* = A$. A matrix $A \in M_n(\mathbb{R})$ is symmetric if $A^T = A$.

> [!abstract] Theorem 2 (Matrix Characterization)[^2]
> A [[Linear Map]] $T$ on a finite-dimensional [[Inner Product Space]] $V$ is self-adjoint if and only if its matrix with respect to an [[Orthonormal Basis]] is Hermitian. If $V$ is a real inner product space, $T$ is self-adjoint if and only if its matrix with respect to an orthonormal basis is symmetric.

Recall that [[Eigenvector]]s of a [[Linear Map]] with distinct [[Eigenvalue]]s are always linearly independent. If the map is self-adjoint, more is true:

> [!abstract] Proposition 3 (Proposition 5.15 -- Eigenvectors are Orthogonal)[^3]
> Let $T \in \mathcal{L}(V)$ be self-adjoint. If $Tv_1 = \lambda_1 v_1$ and $Tv_2 = \lambda_2 v_2$ with $\lambda_1 \neq \lambda_2$, then $\langle v_1, v_2 \rangle = 0$.

> [!abstract] Theorem 4 (Exercise 5.3.10b -- Trace is Real)[^4]
> If $T$ is self-adjoint, then $tr(T) \in \mathbb{R}$.

This follows from $tr(T^*) = \overline{tr(T)}$ ([[Adjoint]]) together with $T^* = T$: $tr(T) = tr(T^*) = \overline{tr(T)}$, so $tr(T)$ equals its own conjugate.

> [!abstract] Theorem 5 (Exercise 5.3.16)[^4]
> The set of all self-adjoint linear maps on $V$ is a real [[Vector Space]].

This vector space is only real, not complex: if $T$ is self-adjoint and nonzero, $iT$ is generally not self-adjoint, since $(iT)^* = \bar{i}T^* = -iT \neq iT$.

> [!abstract] Theorem 6 (Exercise 5.4.19a -- Real Case)[^5]
> Let $V$ be a finite-dimensional inner product space over $\mathbb{R}$ and $T \in \mathcal{L}(V)$. Then $T$ is self-adjoint if and only if $V$ is the [[Orthogonal Direct Sum]] of the [[Eigenspace|eigenspaces]] of $T$.

> [!abstract] Theorem 7 (Exercise 5.4.19c -- Complex Case)[^5]
> Let $V$ be a finite-dimensional inner product space over $\mathbb{C}$ and $T \in \mathcal{L}(V)$. Then $T$ is self-adjoint if and only if all eigenvalues of $T$ are real and $V$ is the [[Orthogonal Direct Sum]] of the eigenspaces of $T$.

These are the eigenspace-decomposition forms of the [[Spectral Theorem]].

> [!abstract] Theorem 8 (Exercise 6.1.11)[^6]
> If $A \in M_n(\mathbb{C})$ is Hermitian, then $\det(A) \in \mathbb{R}$.

# Properties
- [[Adjoint]]
- [[Eigenvector]]
- [[Eigenvalue]]
- [[Trace]]
- [[Vector Space]]
- [[Spectral Theorem]]
- [[Normal Matrix]]
- [[Eigenspace]]
- [[Orthogonal Direct Sum]]
- [[Determinant]]
- [[Eigendecomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=334)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=334)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=334)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=339)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=351)
[^6]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=365)
