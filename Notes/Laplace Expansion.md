---
tags:
  - mathematics
  - linear_algebra
---

# Definition
> [!abstract] Proposition 1 (Proposition 6.9 -- Laplace Expansion Along a Row)[^1]
> If $A \in M_n(\mathbb{F})$, then for any $i = 1, \dots, n$,
> $$
> \det A = \sum_{j=1}^n (-1)^{i+j} a_{ij} \det(A_{ij})
> $$

> [!abstract] Corollary 2 (Corollary 6.12 -- Laplace Expansion Along a Column)[^2]
> If $A \in M_n(\mathbb{F})$, then for any $j = 1, \dots, n$,
> $$
> \det A = \sum_{i=1}^n (-1)^{i+j} a_{ij} \det(A_{ij})
> $$

Each term $(-1)^{i+j}\det(A_{ij})$ is the cofactor of the entry $a_{ij}$; expanding along any row or column and summing the entries against their cofactors always yields the same value, $\det(A)$.

# Properties
- [[Determinant]]
- [[Matrix Minor]]
- [[Adjugate Matrix]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=366)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=369)
