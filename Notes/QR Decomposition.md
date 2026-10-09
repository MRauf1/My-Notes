---
tags:
  - mathematics
  - linear_algebra
  - computer_science
  - numerical_analysis
---

# Definition
> [!abstract] Theorem 1 (Theorem 4.32 -- QR Decomposition)[^1]
> If $A \in M_n(\mathbb{F})$ is invertible, then there exist a matrix $Q \in M_n(\mathbb{F})$ with orthonormal columns and an [[Upper Triangular Matrix|upper triangular matrix]] $R \in M_n(\mathbb{F})$ such that $A = QR$.

Since $Q$ has orthonormal columns, it is a [[Unitary Matrix|unitary]] (or [[Orthogonal Matrix|orthogonal]], in the real case) matrix, so $Q^{-1} = Q^*$ is trivial to compute.

The QR decomposition is useful for solving linear systems: given $Ax = b$ with $A = QR$, $Ax = b \iff Rx = Q^*b$. Since $Q^*$ is unitary, its inverse is known a priori and trivial to apply; since $Q^*$ is also an [[Isometry (Linear Algebra)|isometry]], applying it does not magnify any error already present in $b$. Solving the resulting upper triangular system $Rx = Q^*b$ by back-substitution is also less prone to round-off error than running the full elimination process on $Ax = b$ directly.[^2]

> [!abstract] Theorem 2 (Exercise 4.5.22 -- Extension to Singular $A$)[^3]
> Theorem 1 remains true even when $A$ is singular: performing the [[Gram-Schmidt Algorithm|Gram-Schmidt process]] only on the columns of $A$ that do not lie in the span of the preceding columns still produces enough orthonormal vectors to build $Q$, together with an upper triangular $R$ (now allowed to have zero entries corresponding to the dependent columns) such that $A = QR$.

Invertibility of $A$ is therefore not needed for a QR decomposition to exist. What Theorem 1 does implicitly rely on is that $A$ is square: $Q$ and $R$ are both taken in $M_n(\mathbb{F})$, matching the shape of $A$. Squareness itself is not essential to the underlying Gram-Schmidt argument, however: for any $A \in M_{m,n}(\mathbb{F})$ with $m \geq n$ (at least as many rows as columns, so that $n$ orthonormal vectors can exist in $\mathbb{F}^m$), the same argument produces $Q \in M_{m,n}(\mathbb{F})$ with orthonormal columns and upper triangular $R \in M_n(\mathbb{F})$ with $A = QR$ — the columns of $A$ need not even be linearly independent, by the same fix used for singular square $A$. This more general rectangular form is often called the reduced (or thin) QR decomposition.

> [!abstract] Theorem 3 (Exercise 6.2.6 -- Determinant)[^4]
> If $A = QR$ is a QR decomposition of $A \in M_n(\mathbb{C})$, then $|\det(A)| = |r_{11} \cdots r_{nn}|$.

> [!info] Definition 4 (Full and Reduced QR Factorization)[^5]
> For $A \in \mathbb{R}^{m \times n}$ with $m > n$, the QR factorization is
> $$
> \begin{align}
> A = Q \begin{bmatrix} R \\ O \end{bmatrix} = \begin{bmatrix} Q_1 & Q_2 \end{bmatrix} \begin{bmatrix} R \\ O \end{bmatrix} = Q_1 R
> \end{align}
> $$
> where $Q \in \mathbb{R}^{m \times m}$ is [[Orthogonal Matrix|orthogonal]], $R \in \mathbb{R}^{n \times n}$ is upper triangular, $Q_1$ is the first $n$ columns of $Q$ and $Q_2$ the remaining $m - n$. $A = Q_1R$, with $Q_1$ having orthonormal columns and the same shape as $A$, is the reduced ("economy size") QR factorization.

> [!abstract] Theorem 5 (Orthonormal Bases from QR)[^6]
> If $A$ has full column rank (so $R$ is nonsingular), then the columns of $Q_1$ form an [[Orthonormal Basis|orthonormal basis]] for $\operatorname{span}(A)$, and the columns of $Q_2$ form an orthonormal basis for $\operatorname{span}(A)^\perp = \{z \in \mathbb{R}^m : A^Tz = 0\}$, the null space of $A^T$.

> [!abstract] Theorem 6 (Least Squares via QR)[^5]
> Since orthogonal $Q$ preserves the 2-norm,
> $$
> \begin{align}
> \lVert b - Ax \rVert_2^2 = \left\lVert Q^Tb - \begin{bmatrix} R \\ O \end{bmatrix} x \right\rVert_2^2 = \lVert c_1 - Rx \rVert_2^2 + \lVert c_2 \rVert_2^2, \qquad Q^Tb = \begin{bmatrix} c_1 \\ c_2 \end{bmatrix}
> \end{align}
> $$
> with $c_1 \in \mathbb{R}^n$. So the [[Linear Least Squares Problem|least squares]] solution solves $Rx = c_1$, and the minimum residual norm is $\lVert r \rVert_2 = \lVert c_2 \rVert_2$.

If $A$ is rank-deficient, the QR factorization still exists but $R$ is singular, and the least squares solution is not unique ([[QR Factorization with Column Pivoting]]).[^7] Orthonormal bases from QR are also useful in eigenvalue computations and optimization.[^6]

# Types
Methods for computing the QR factorization:[^6]
- [[Householder QR Factorization|Householder transformations]] (elementary reflectors)
- [[Givens Rotation|Givens transformations]] (plane rotations)
- [[Gram-Schmidt Algorithm|Gram-Schmidt orthogonalization]] (classical and [[Modified Gram-Schmidt Algorithm|modified]])
- [[QR Factorization with Column Pivoting]]

# Properties
- [[Unitary Matrix]]
- [[Orthogonal Matrix]]
- [[Gram-Schmidt Algorithm]]
- [[LU Decomposition]]
- [[Schur Decomposition]]
- [[Cholesky Decomposition]]
- [[Determinant]]
- [[Linear Least Squares Problem]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=303)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=303)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=307)
[^4]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=375)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=140)
[^6]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=141)
[^7]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=155)
