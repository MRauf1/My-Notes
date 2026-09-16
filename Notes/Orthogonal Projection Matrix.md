---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Orthogonal Projection Matrix from an Orthonormal Basis)[^1]
> Let $U$ be a subspace of $\mathbb{R}^n$ or $\mathbb{C}^n$, with [[Orthonormal Basis]] $(f_1, \dots, f_m)$. Then the matrix of the [[Orthogonal Projection]] $P_U$ with respect to the [[Standard Basis]] $E$ is
> $$
> \begin{align}
> [P_U]_E = \sum_{j=1}^m f_j f_j^*
> \end{align}
> $$

> [!abstract] Theorem 2 (Orthogonal Projection Matrix from an Arbitrary Basis)[^2]
> Let $U$ be a subspace of $\mathbb{R}^n$ or $\mathbb{C}^n$ with basis $(v_1, \dots, v_k)$. Let $A$ be the $n \times k$ matrix with columns $v_1, \dots, v_k$. Then
> $$
> \begin{align}
> [P_U]_E = A(A^*A)^{-1}A^*
> \end{align}
> $$

# Properties
- Theorem 2 implicitly claims that the matrix $A^*A$ is [[Matrix Inverse|invertible]].
- $A^*$ denotes the [[Matrix Conjugate Transpose]] of $A$.
- This formula underlies computing the best-fitting solution in [[Simple Linear Regression|least-squares]] problems, per the [[Best Approximation Theorem]].
- [[Pseudoinverse]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=276)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=277)
