---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Unitary Matrix)[^1]
> A [[Matrix]] $A \in M_n(\mathbb{C})$ is unitary if $A^*A = I_n$.

The real analogue of a unitary matrix is an [[Orthogonal Matrix]]: $A \in M_n(\mathbb{R})$ is orthogonal exactly when $A^TA = I_n$, which coincides with the unitary condition since $A^* = A^T$ for real matrices.

> [!abstract] Proposition 2 (Proposition 4.31)[^2]
> The columns of $A \in M_n(\mathbb{F})$ are orthonormal if and only if $A^*A = I_n$.

So $A$ is unitary (or [[Orthogonal Matrix|orthogonal]], in the real case) exactly when its columns form an [[Orthonormal Basis]] of $\mathbb{F}^n$.

> [!abstract] Theorem 3 (Corollary 4.30)[^3]
> Suppose $\mathcal{B}_V$ and $\mathcal{B}_W$ are [[Orthonormal Basis|orthonormal bases]] of $V$ and $W$, respectively. Then $T \in \mathcal{L}(V, W)$ is an [[Isometry (Linear Algebra)|isometry]] if and only if the columns of the matrix $[T]_{\mathcal{B}_V, \mathcal{B}_W}$ form an orthonormal basis of $\mathbb{F}^n$.

Combined with Proposition 2, this means [[Isometry (Linear Algebra)|isometries]] between [[Inner Product Space]]s are represented, with respect to orthonormal bases, by unitary matrices in the complex case and by [[Orthogonal Matrix|orthogonal matrices]] in the real case. This is one of the reasons inner product spaces are especially convenient to work with: the inverse of the corresponding structure-preserving map is trivial to compute, since if $A$ is unitary then $A^{-1} = A^*$ ([[Matrix Conjugate Transpose]]).[^4]

# Properties
- [[Orthogonal Matrix]]
- [[Isometry (Linear Algebra)]]
- [[Unitary Matrix Norm]]
- [[Unitarily Invariant Norm]]
- [[Condition Number of a Matrix]]
- [[Adjoint]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=301)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=301)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=300)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=301)
