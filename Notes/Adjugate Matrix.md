---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!info] Definition 1 (Cofactor Matrix and Adjugate)[^1]
> Let $A \in M_n(\mathbb{F})$. The cofactor matrix of $A$ is the matrix $C \in M_n(\mathbb{F})$ with $c_{ij} = (-1)^{i+j} \det(A_{ij})$ (the cofactors from [[Laplace Expansion]], using the [[Matrix Minor|minors]] $A_{ij}$). The adjugate of $A$ is
> $$
> adj(A) = C^T
> $$

> [!abstract] Theorem 2 (Theorem 6.29 -- Inverse via the Adjugate)[^2]
> If $A \in M_n(\mathbb{F})$ is [[Invertible Linear Map|invertible]], then
> $$
> A^{-1} = \frac{1}{\det A} adj(A)
> $$

# Properties
- [[Determinant]]
- [[Matrix Minor]]
- [[Laplace Expansion]]
- [[Matrix Inverse]]
- [[Determinant Invertible Matrix Theorem]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=392)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=392)
