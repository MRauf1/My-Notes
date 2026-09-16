---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Theorem 1 (Powers via Spectral Decomposition)[^1]
> If $A \in M_n(\mathbb{C})$ is Hermitian with [[Spectral Theorem|spectral decomposition]] $A = UDU^*$, $D = \text{diag}(\lambda_1, \dots, \lambda_n)$, then for $k \in \mathbb{N}$,
> $$
> A^k = (UDU^*)^k = UD^kU^* = U \, \text{diag}(\lambda_1^k, \dots, \lambda_n^k) \, U^*
> $$

This makes it easy to compute arbitrarily high powers of a Hermitian matrix, and suggests how to define more general functions of a matrix.

> [!info] Definition 2 (Function of a Matrix -- Functional Calculus)[^2]
> Let $A \in M_n(\mathbb{C})$ be Hermitian with spectral decomposition $A = U \, \text{diag}(\lambda_1, \dots, \lambda_n) \, U^*$, and let $f: \mathbb{R} \to \mathbb{R}$. Define
> $$
> f(A) := U \, \text{diag}(f(\lambda_1), \dots, f(\lambda_n)) \, U^*
> $$

This route to defining $f(A)$ is called the functional calculus. The resulting functions sometimes, but not always, behave the way the scalar function $f$'s properties would suggest.

# Properties
- [[Spectral Theorem]]
- [[Matrix Exponential]]
- [[Diagonal Matrix]]
- [[Eigenvalue]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=343)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=344)
