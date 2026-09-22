---
tags:
  - mathematics
  - linear_algebra
---

# Definition
In short, the Spectral Theorem is just the [[Eigendecomposition]] applied to a [[Normal Matrix|normal]]/[[Self-Adjoint Linear Map|Hermitian/symmetric]] matrix: it guarantees that for exactly these matrices, the eigenvector matrix $S$ in $A = SDS^{-1}$ can be chosen unitary (or orthogonal), i.e. $S^{-1} = S^*$, turning an ordinary eigendecomposition into a spectral decomposition.

> [!abstract] Lemma 1 (Lemma 5.18)[^1]
> If $A \in M_n(\mathbb{F})$ is Hermitian, then $A$ has an [[Eigenvector]] in $\mathbb{F}^n$. If $V$ is a nonzero finite-dimensional [[Inner Product Space]] and $T \in \mathcal{L}(V)$ is [[Self-Adjoint Linear Map|self-adjoint]], then $T$ has an eigenvector.

> [!abstract] Theorem 2 (Theorem 5.19 -- The Spectral Theorem for Self-Adjoint Maps and Hermitian Matrices)[^2]
> If $V$ is a finite-dimensional inner product space and $T \in \mathcal{L}(V)$ is self-adjoint, then there is an [[Orthonormal Basis]] of $V$ consisting of eigenvectors of $T$. If $A \in M_n(\mathbb{F})$ is Hermitian (if $\mathbb{F} = \mathbb{C}$) or symmetric (if $\mathbb{F} = \mathbb{R}$), then there exist a unitary (if $\mathbb{F} = \mathbb{C}$) or orthogonal (if $\mathbb{F} = \mathbb{R}$) matrix $U \in M_n(\mathbb{F})$ and real numbers $\lambda_1, \dots, \lambda_n \in \mathbb{R}$ such that
> $$
> A = U \, \text{diag}(\lambda_1, \dots, \lambda_n) \, U^*
> $$

The matrix statement follows from the linear-map statement together with the fact that eigenvalues of self-adjoint maps are real. The proof is inductive: given a unit eigenvector $e_1$ of $T$ with eigenvalue $\lambda_1$, self-adjointness gives $\langle Tv, e_1 \rangle = \langle v, Te_1 \rangle = \lambda_1 \langle v, e_1 \rangle$ for any $v$, so whenever $\langle v, e_1 \rangle = 0$, also $\langle Tv, e_1 \rangle = 0$ — i.e. $T$ maps $\langle e_1 \rangle^\perp$ to itself, and the same argument repeats on this smaller self-adjoint subspace.

The factorization $A = U \, \text{diag}(\lambda_1, \dots, \lambda_n) \, U^*$ is called a spectral decomposition of $A$ (the set of eigenvalues of a linear map is sometimes called its spectrum, hence the theorem's name). Theorem 2 gives a necessary and sufficient condition for unitary/orthogonal diagonalizability *in the case of all-real eigenvalues*; it says nothing about maps or matrices with nonreal eigenvalues, and there exist linear maps that can only be diagonalized by a non-orthonormal basis.

> [!abstract] Theorem 3 (Theorem 5.23 -- The Spectral Theorem for Normal Maps and Normal Matrices)[^3]
> If $V$ is a finite-dimensional inner product space over $\mathbb{C}$ and $T \in \mathcal{L}(V)$ is [[Normal Matrix|normal]], then there is an orthonormal basis of $V$ consisting of eigenvectors of $T$. If $A \in M_n(\mathbb{C})$ is normal, then there exist a unitary matrix $U \in M_n(\mathbb{C})$ and complex numbers $\lambda_1, \dots, \lambda_n \in \mathbb{C}$ such that $A = U \, \text{diag}(\lambda_1, \dots, \lambda_n) \, U^*$.

Unlike Theorem 2, being [[Normal Matrix|normal]] is a **necessary and sufficient** condition for unitary diagonalizability in general (allowing complex eigenvalues): $T$ can be diagonalized by an orthonormal basis if and only if $T$ is normal. Not every operator is normal, though, so not every operator can be unitarily diagonalized — the next-best universal result is the [[Schur Decomposition]], which unitarily *triangularizes* every operator on a complex inner product space, whether or not it is normal.

> [!abstract] Theorem 4 (Simultaneous Spectral Decomposition of Commuting Hermitian Matrices)[^4]
> If $A, B \in M_n(\mathbb{C})$ are Hermitian and commute ($AB = BA$), then $A$ and $B$ admit spectral decompositions sharing the same unitary matrix: $A = U \, \text{diag}(\lambda_1, \dots, \lambda_n) \, U^*$ and $B = U \, \text{diag}(\mu_1, \dots, \mu_n) \, U^*$ for the same $U$.

The eigenvalues $\lambda_j$ and $\mu_j$ can still differ between $A$ and $B$ — it is only the eigenvectors (the columns of $U$) that are forced to coincide, not the eigenvalues paired with them.

# Properties
- [[Self-Adjoint Linear Map]]
- [[Normal Matrix]]
- [[Diagonalizable Matrix]]
- [[Unitary Matrix]]
- [[Eigenspace]]
- [[Orthogonal Direct Sum]]
- [[Function of a Matrix]]
- [[Schur Decomposition]]
- [[Eigendecomposition]]

# Geometric Interpretation (Computer Graphics)[^5]
- Writing the real spectral decomposition as $A = RSR^T$ with $R$ orthogonal (columns $\mathbf{v}_1, \mathbf{v}_2, \dots$, the eigenvectors) and $S$ diagonal (entries $\lambda_1, \lambda_2, \dots$, the eigenvalues), the map $\mathbf{x} \mapsto A\mathbf{x}$ decomposes geometrically into: (1) rotate $\mathbf{v}_1, \mathbf{v}_2, \dots$ onto the coordinate axes (the transform by $R^T$), (2) scale along each axis by the corresponding eigenvalue (the transform by $S$), (3) rotate the axes back to $\mathbf{v}_1, \mathbf{v}_2, \dots$ (the transform by $R$).
- Consequently, every symmetric matrix is geometrically just a [[Scale Transformation|scale]] along some (possibly non-uniform, non–axis-aligned) set of orthogonal directions — its eigenvectors.

[^5]: [Fundamentals of Computer Graphics](zotero://open-pdf/library/items/7B6A4MRC?page=135&annotation=LEDLVFTS)

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=341)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=341)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=346)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=349)
