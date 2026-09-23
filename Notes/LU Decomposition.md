---
tags:
  - mathematics
  - linear_algebra
  - computer_science
  - numerical_analysis
---

# Definition

> [!abstract] Theorem 1 (LU Decomposition)[^1]
> 1) Reduce $A$ to an [[Upper Triangular Matrix]] using [[Row Operations]] R1 only. If this succeeds, call the result $U$. If it fails, then $A$ does not have an LU Decomposition.
> 2) Define $L$ as a [[Lower Triangular Matrix]] with 1s on the diagonal and $-c$ in the $(i, j)$th entry if, during the elimination process, $c$ times row $j$ was added to row $i$.
> 3) $A = LU$

Not every [[Matrix]] has an LU Decomposition.

This decomposition can be used to solve linear systems in a fast and stable (not as susceptible to round-off errors) manner.

> [!abstract] Theorem 2 (Exercise 6.2.4a -- Determinant)[^2]
> If $A = LU$ is an LU decomposition of $A \in M_n(\mathbb{F})$, then $\det(A) = u_{11} \cdots u_{nn}$.

This holds since $L$ has $1$s on its diagonal, so $\det(L) = 1$ ([[Triangular Matrix Determinant]]), and $\det(A) = \det(L)\det(U) = \det(U)$ ([[Determinant Matrix Multiplication]]).

> [!abstract] Theorem 3 (Solving a Linear System with LU)[^3]
> Given $A = LU$, with $L$ unit lower triangular and $U$ upper triangular (computed by [[Gaussian Elimination]]), $Ax = b$ becomes $LUx = b$ and is solved by
> 1. [[Forward-Substitution]] on $Ly = b$,
> 2. [[Back-Substitution]] on $Ux = y$.

Computing the factorization costs about $n^3/3$ multiplications (and a similar number of additions). Each right-hand side then costs only about $n^2$ for the forward- and back-substitution. As $n$ grows, the factorization phase increasingly dominates the cost.[^4]

In implementations, $L$ and $U$ overwrite the storage of $A$. $U$ occupies the upper triangle (including the diagonal) and the multipliers of $L$ occupy the strict lower triangle. The unit diagonal of $L$ is not stored, and the matrices $M_k$, $L_k$, $P_k$ are never formed explicitly.[^5]

> [!abstract] Theorem 4 (Explicit Inversion Should Be Avoided)[^4]
> Solving $Ax = b$ via $x = A^{-1}b$ requires an LU factorization plus $n$ forward- and back-substitutions (one per column of $I$), about $n^3$ multiplications in total. That is three times the cost of LU factorization, and it also gives a less accurate answer.

# Types
- [[LUP Decomposition]] ($PA = LU$, from [[Partial Pivoting]])
- $PAQ = LU$, from [[Complete Pivoting]]
- [[LDU Decomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=128)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=375)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=88)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=99)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=98)