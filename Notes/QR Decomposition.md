---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Theorem 4.32 -- QR Decomposition)[^1]
> If $A \in M_n(\mathbb{F})$ is invertible, then there exist a matrix $Q \in M_n(\mathbb{F})$ with orthonormal columns and an [[Upper Triangular Matrix|upper triangular matrix]] $R \in M_n(\mathbb{F})$ such that $A = QR$.

Since $Q$ has orthonormal columns, it is a [[Unitary Matrix|unitary]] (or [[Orthogonal Matrix|orthogonal]], in the real case) matrix, so $Q^{-1} = Q^*$ is trivial to compute.

The QR decomposition is useful for solving linear systems: given $Ax = b$ with $A = QR$, $Ax = b \iff Rx = Q^*b$. Since $Q^*$ is unitary, its inverse is known a priori and trivial to apply; since $Q^*$ is also an [[Isometry (Linear Algebra)|isometry]], applying it does not magnify any error already present in $b$. Solving the resulting upper triangular system $Rx = Q^*b$ by back-substitution is also less prone to round-off error than running the full elimination process on $Ax = b$ directly.[^2]

> [!abstract] Theorem 2 (Exercise 4.5.22 -- Extension to Singular $A$)[^3]
> Theorem 1 remains true even when $A$ is singular: performing the [[Gram-Schmidt Algorithm|Gram-Schmidt process]] only on the columns of $A$ that do not lie in the span of the preceding columns still produces enough orthonormal vectors to build $Q$, together with an upper triangular $R$ (now allowed to have zero entries corresponding to the dependent columns) such that $A = QR$.

Invertibility of $A$ is therefore not needed for a QR decomposition to exist. What Theorem 1 does implicitly rely on is that $A$ is square: $Q$ and $R$ are both taken in $M_n(\mathbb{F})$, matching the shape of $A$. Squareness itself is not essential to the underlying Gram-Schmidt argument, however: for any $A \in M_{m,n}(\mathbb{F})$ with $m \geq n$ (at least as many rows as columns, so that $n$ orthonormal vectors can exist in $\mathbb{F}^m$), the same argument produces $Q \in M_{m,n}(\mathbb{F})$ with orthonormal columns and upper triangular $R \in M_n(\mathbb{F})$ with $A = QR$ — the columns of $A$ need not even be linearly independent, by the same fix used for singular square $A$. This more general rectangular form is often called the reduced (or thin) QR decomposition.

# Properties
- [[Unitary Matrix]]
- [[Orthogonal Matrix]]
- [[Gram-Schmidt Algorithm]]
- [[LU Decomposition]]
- [[Schur Decomposition]]
- [[Cholesky Decomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=303)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=303)
[^3]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=307)
