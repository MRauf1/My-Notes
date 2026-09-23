---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Symmetric Indefinite Matrix)[^1]
> A symmetric matrix $A$ is indefinite if $x^T A x$ takes both positive and negative values, depending on $x$.

For such $A$ the [[Cholesky Decomposition|Cholesky factorization]] does not apply, and some form of [[Pivoting]] is generally needed for stability. To preserve symmetry, the pivoting must be symmetric, of the form $PAP^T$ with $P$ a [[Permutation Matrix]].[^1]

> [!abstract] Theorem 2 (Symmetric Indefinite Factorization)[^2]
> A factorization $PAP^T = LDL^T$ with $L$ unit lower triangular and $D$ diagonal may not exist, and in general it cannot be computed stably with symmetric pivoting alone. The best achievable is
> $$
> \begin{align}
> PAP^T = LDL^T \qquad \text{or} \qquad PAP^T = LTL^T
> \end{align}
> $$
> where $D$ is block diagonal with $1 \times 1$ and $2 \times 2$ diagonal blocks, or $T$ is [[Tridiagonal Matrix|tridiagonal]].

A block matrix is a matrix partitioned into submatrices ("blocks") of compatible dimensions. A block diagonal matrix has all blocks zero except those on the main block diagonal.[^2]

# Types
- Block $LDL^T$ with diagonal pivoting: Bunch–Kaufman (partial pivoting, $O(n^2)$ comparisons in total) or Bunch–Parlett (complete pivoting, about $n^3/6$ comparisons, i.e., $O(n^3)$).
- Aasen's method: $PAP^T = LTL^T$ with $T$ tridiagonal.

# Properties
- Either form is stable and costs about $n^3/6$ multiplications and $n^3/6$ additions.[^3] Compare Cholesky at $n^3/6$ each, and [[Gaussian Elimination]] / [[LU Decomposition|LU]] on a nonsymmetric matrix at $n^3/3$ each.
- Storage: $n(n+1)/2$ entries, since only one triangle plus $D$ or $T$ is kept.
- Solve phase: $O(n^2)$ work, i.e., two unit triangular solves of about $n^2/2$ multiplications each, plus an $O(n)$ solve with the block diagonal $D$ or tridiagonal $T$.[^3]
- By Sylvester's law of inertia, $D$ has the same numbers of positive, negative and zero eigenvalues as $A$ (each $2 \times 2$ block contributes one positive and one negative eigenvalue). The factorization therefore reveals the inertia of $A$.
- [[LDLT Factorization]] (the positive definite, unpivoted special case)

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=107)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=107)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=108)
