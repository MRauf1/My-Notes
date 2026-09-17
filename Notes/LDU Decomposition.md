---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (LDU Decomposition)
> A factorization $A = LDU$ of $A \in M_n(\mathbb{F})$, where $L$ is a [[Lower Triangular Matrix]] with $1$s on the diagonal, $D$ is a [[Diagonal Matrix]], and $U$ is an [[Upper Triangular Matrix]] with $1$s on the diagonal.

An LDU decomposition refines an [[LU Decomposition]] $A = L(DU')$ by separating out the pivots: the diagonal entries of the upper triangular factor in an LU decomposition become the diagonal entries of $D$, once the remaining upper triangular factor $U$ is normalized to have $1$s on its own diagonal. It exists exactly when $A$ has an LU decomposition.

> [!abstract] Theorem 2 (Exercise 6.2.5)[^1]
> If $A = LDU$ is an LDU decomposition of $A \in M_n(\mathbb{F})$, then
> $$
> \det A = d_{11} \cdots d_{nn}
> $$

# Properties
- [[LU Decomposition]]
- [[Diagonal Matrix]]
- [[Upper Triangular Matrix]]
- [[Lower Triangular Matrix]]
- [[Determinant]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=375)
