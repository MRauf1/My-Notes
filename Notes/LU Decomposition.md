---
tags:
  - mathematics
  - linear_algebra
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

# Types
- [[LUP Decomposition]]
- [[LDU Decomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=128)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=375)