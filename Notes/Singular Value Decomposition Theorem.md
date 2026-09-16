---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Theorem 5.1 -- Singular Value Decomposition (SVD))[^1]
> Let $V$ and $W$ be [[Finite-Dimensional Vector Space|finite-dimensional]] [[Inner Product Space]]s and let $T \in \mathcal{L}(V, W)$ have [[Rank]] $r$. Then there exist [[Orthonormal Basis|orthonormal bases]] $(e_1, \dots, e_n)$ of $V$ and $(f_1, \dots, f_m)$ of $W$ and numbers $\sigma_1 \geq \dots \geq \sigma_r > 0$ such that
> $$
> Te_j = \sigma_j f_j \text{ for } j = 1, \dots, r, \qquad Te_j = 0 \text{ for } j = r+1, \dots, n
> $$

The numbers $\sigma_1, \dots, \sigma_r$ are the [[Singular Value|singular values]] of $T$; the vectors $e_1, \dots, e_n$ are the right singular vectors and $f_1, \dots, f_m$ are the left singular vectors.[^2]

Unlike the earlier fact that $V, W$ admit *some* bases in which the matrix of $T$ has $1$s on part of the diagonal and $0$s elsewhere (which says essentially nothing useful, since those bases are otherwise arbitrary), the SVD gives *orthonormal* bases with this simple diagonal form — a genuinely powerful structural statement. In some ways it serves as a substitute for eigenvalues and eigenvectors, with the advantage that, unlike an [[Eigenvalue|eigendecomposition]], a singular value decomposition always exists for every $T \in \mathcal{L}(V, W)$ between finite-dimensional inner product spaces.[^3]

> [!abstract] Theorem 2 (Theorem 5.4 -- Matrix Form)[^4]
> Let $A \in M_{m,n}(\mathbb{F})$ have [[Rank]] $r$. Then there exist matrices $U \in M_m(\mathbb{F})$ and $V \in M_n(\mathbb{F})$, with $U$ and $V$ [[Unitary Matrix|unitary]] (if $\mathbb{F} = \mathbb{C}$) or [[Orthogonal Matrix|orthogonal]] (if $\mathbb{F} = \mathbb{R}$), and unique real numbers $\sigma_1 \geq \dots \geq \sigma_r > 0$ such that
> $$
> A = U \Sigma V^*
> $$
> where $\Sigma \in M_{m,n}(\mathbb{R})$ has $(j,j)$ entry $\sigma_j$ for $1 \leq j \leq r$, and all other entries $0$.

Theorem 2 is the matrix form of Theorem 1: $U$'s columns are the left singular vectors, $V$'s columns are the right singular vectors, and $\Sigma$'s nonzero diagonal entries are the [[Singular Value|singular values]].

Geometrically, $A = U\Sigma V^*$ decomposes the map $x \mapsto Ax$ into a sequence of transformations of $\mathbb{F}^n$: $x \mapsto V^*x \mapsto \Sigma(V^*x) \mapsto U(\Sigma(V^*x))$. Since $V^*$ is unitary, it acts as an [[Isometry (Linear Algebra)|isometry]] on $\mathbb{F}^n$ — algebraically, $V^* = [I]_{E, \mathcal{B}'}$ where $\mathcal{B}'$ is the orthonormal basis given by the columns of $V$ and $E$ is the standard basis, so $V^*$ is the isometry sending $\mathcal{B}'$ to $E$. As a map in $\mathcal{L}(\mathbb{F}^n, \mathbb{F}^m)$, $\Sigma$ then stretches the standard basis vectors according to the singular values (sending $e_j \mapsto \sigma_j e_j$ for $j \leq r$ and collapsing $e_j \mapsto 0$ for $j > r$), so the unit sphere is mapped to an ellipsoid whose semi-axis lengths are the singular values. Finally $U = [I]_{\mathcal{B}, E}$ is the isometry of $\mathbb{F}^m$ sending the standard basis $E$ to the orthonormal basis $\mathcal{B}$ given by its columns — like $V^*$, it acts as some combination of rotations and reflections. In $\mathbb{R}^2$, any such isometry must be a rotation or a reflection; something similar holds in higher dimensions.[^5]

> [!abstract] Theorem 3 (Theorem 5.7 -- Outer Product Form)[^6]
> Let $A \in M_{m,n}(\mathbb{F})$. Then there exist [[Orthonormal Basis|orthonormal bases]] $(u_1, \dots, u_m)$ of $\mathbb{F}^m$ and $(v_1, \dots, v_n)$ of $\mathbb{F}^n$ such that
> $$
> A = \sum_{j=1}^r \sigma_j u_j v_j^*
> $$
> where $\sigma_1 \geq \dots \geq \sigma_r > 0$ are the nonzero [[Singular Value|singular values]] of $A$.

This alternate form shows that a rank-$r$ matrix in $M_{m,n}(\mathbb{F})$, which generally takes $mn$ numbers to describe, can be specified using only $(m+n)r$ numbers (the entries of $\sigma_1 u_1, \dots, \sigma_r u_r$ and of $v_1, \dots, v_r$) — the basis for the [[Low-Rank Matrix Approximation Theorem|best low-rank approximation]] of a matrix.

# Algorithm
- [[Singular Value Decomposition Algorithm]]

# Properties
- [[Singular Value]]
- [[Orthonormal Basis]]
- [[Rank]]
- [[Eigenvalue]]
- [[Low-Rank Matrix Approximation Theorem]]
- [[Pseudoinverse]]
- [[Adjoint]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=309)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=309)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=310)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=317)
[^5]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=321)
[^6]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=323)
