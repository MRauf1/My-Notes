---
tags:
  - mathematics
  - linear_algebra
  - computer_science
  - numerical_analysis
---

# Definition
> [!abstract] Theorem 1 (Exercise 5.4.11 -- Cholesky Decomposition)[^1]
> If $A \in M_n(\mathbb{F})$ is [[Positive Definite Matrix|positive definite]], then there is an [[Upper Triangular Matrix|upper triangular]] matrix $X \in M_n(\mathbb{F})$ such that
> $$
> A = X^*X
> $$

> [!info] Definition 2 (Cholesky Factorization, Numerical Form)[^2]
> If $A \in \mathbb{R}^{n \times n}$ is symmetric and [[Positive Definite Matrix|positive definite]], then an [[LU Decomposition]] can be arranged so that $U = L^T$:
> $$
> \begin{align}
> A = LL^T
> \end{align}
> $$
> where $L$ is [[Lower Triangular Matrix|lower triangular]] with positive diagonal entries (not, in general, a unit diagonal). This is Theorem 1 with $L = X^*$.

# Types
- [[LDLT Factorization]] ($A = LDL^T$, no square roots)
- [[Pivoted Cholesky Factorization]] (for symmetric positive semidefinite matrices)

# Properties
- The $n$ square roots required are all of positive numbers, so the algorithm is well-defined.[^2]
- [[Pivoting]] is not required for numerical stability.[^2]
- Only the lower triangle of $A$ is accessed, so storage is $n(n+1)/2$ entries, compared with $n^2$ for [[Gaussian Elimination|LU]] of a general matrix.[^3]
- Work: about $n^3/6$ multiplications and $n^3/6$ additions, plus $n$ square roots. LU of a general matrix costs $n^3/3$ multiplications and $n^3/3$ additions.[^3]
- Solving $Ax = b$: [[Forward-Substitution]] on $Ly = b$, then [[Back-Substitution]] on $L^T x = y$. Each takes about $n^2/2$ multiplications, so about $n^2$ in total.
- Banded case: about $\beta^2 n/2$ multiplications ([[Banded Matrix]]). Sparse case: see [[Sparse Matrix]].
- [[Symmetric Indefinite Factorization]] (the replacement when $A$ is symmetric but indefinite)
- [[Positive Definite Matrix]]
- [[Upper Triangular Matrix]]
- [[QR Decomposition]]
- [[Matrix Conjugate Transpose]]
- Used in [[Multivariate Normal Sampling (Cholesky Factorization)|multivariate normal sampling]] to factor a covariance matrix $\Sigma = AA^\top$.

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=350)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=105)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=106)
