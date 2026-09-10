---
tags:
  - mathematics
  - linear_algebra
---

# Definition

> [!info] Definition 1 (Frobenius [[Vector Norm]])[^1]
> [[Vector Norm]] in [[Frobenius Inner Product Space]] is
> $$
> \begin{align}
> \lVert A \rVert_F = \sqrt{tr(A^* A)}
> \end{align}
> $$

> [!abstract] Proposition 2 (Frobenius Norm as Sum of Column Norms)[^2]
> If $B$ has columns $b_1, \dots, b_n$, then
> $$
> tr(B^* B) = \sum_i \lVert b_i \rVert^2
> $$
> so $\lVert B \rVert_F^2 = \sum_i \lVert b_i \rVert^2$: the square of the Frobenius norm equals the sum of the absolute squares of all entries of $B$, i.e. the sum of the squared [[Vector Norm|norms]] of its columns.

# Properties
- [[Operator Norm and Frobenius Norm Inequality]]
- [[Rank-1 Matrix Operator Norm]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=254)
[^2]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=254)