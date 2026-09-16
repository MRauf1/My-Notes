---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Matrix Exponential)[^1]
> For $A \in M_n(\mathbb{C})$, the matrix exponential is
> $$
> e^A := \sum_{k=0}^\infty \frac{1}{k!} A^k
> $$

> [!abstract] Theorem 2 (Agrees with the Functional Calculus)[^2]
> If $A \in M_n(\mathbb{C})$ is Hermitian with [[Spectral Theorem|spectral decomposition]] $A = U \, \text{diag}(\lambda_1, \dots, \lambda_n) \, U^*$, then
> $$
> e^A = U \, \text{diag}(e^{\lambda_1}, \dots, e^{\lambda_n}) \, U^*
> $$
> i.e. $e^A$ agrees with $f(A)$ under the [[Function of a Matrix|functional calculus]] for $f(x) = e^x$.

# Properties
- [[Function of a Matrix]]
- [[Spectral Theorem]]
- [[Diagonalizable Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=344)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=344)
