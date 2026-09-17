---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Algorithm 1 (Algorithm 6.15)[^1]
> To compute $\det(A)$ for $A \in M_n(\mathbb{F})$:
> 1. Convert $A$ into an [[Upper Triangular Matrix]] $B$ using [[Row Operations]] R1 and R3 only.
> 2. Let $k$ be the number of times two rows were switched.
> 3. $\det(A) = (-1)^k b_{11} \cdots b_{nn}$.

This works because R1 and R3 correspond to multiplication by [[Elementary Matrix|elementary matrices]] whose determinant is known: row replacement (R1) leaves the determinant unchanged, and each row swap (R3) multiplies it by $-1$, so tracking only the swaps and then reading off the product of the diagonal of the resulting [[Triangular Matrix Determinant|triangular matrix]] recovers $\det(A)$. For large matrices, this is far more efficient than [[Laplace Expansion]] or the [[Leibniz Formula for Determinant|permutation sum formula]].

# Properties
- [[Determinant]]
- [[Row Operations]]
- [[Elementary Matrix]]
- [[Triangular Matrix Determinant]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=370)
