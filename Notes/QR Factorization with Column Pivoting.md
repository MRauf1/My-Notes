---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (QR Factorization with Column Pivoting)[^1]
> A [[QR Decomposition|QR factorization]] in which, at each stage, the column of the remaining unreduced submatrix with maximum Euclidean norm is selected, interchanged (explicitly or implicitly) with the next column in natural order, and zeroed below the diagonal as usual; the transformation is then applied to the remaining unreduced columns.

This treats the columns of $A$ as an unordered set from which to select a maximal linearly independent subset. It requires that at each step the remaining columns have no components in the already completed columns: true for [[Householder QR Factorization|Householder]], [[Givens Rotation|Givens]], and row-oriented [[Modified Gram-Schmidt Algorithm|modified Gram-Schmidt]], but not for column-oriented Gram-Schmidt (classical or modified).[^1]

> [!abstract] Theorem 2 (Rank-Revealing Form)[^2]
> If $\operatorname{rank}(A) = k < n$, then after $k$ steps the remaining unreduced columns are zero (or negligible) below row $k$, giving
> $$
> \begin{align}
> Q^T A P = \begin{bmatrix} R & S \\ O & O \end{bmatrix}
> \end{align}
> $$
> where $R$ is $k \times k$, upper triangular and nonsingular, and $P$ is a [[Permutation Matrix]] performing the column interchanges.

> [!info] Definition 3 (Basic Solution)[^3]
> A basic solution of $Ax \cong b$ (one with at most $k$ nonzero components) is obtained by solving $Rz = c_1$, where $c_1$ is the first $k$ components of $Q^Tb$, and taking
> $$
> \begin{align}
> x = P \begin{bmatrix} z \\ 0 \end{bmatrix}
> \end{align}
> $$

In data fitting, this amounts to ignoring components of the model that are redundant or not well-determined. The minimum-norm solution can instead be obtained by applying further orthogonal transformations on the right to annihilate $S$.[^3]

# Properties
- In practice the rank is unknown, so it is discovered by monitoring the norms of the remaining unreduced columns and stopping when the maximum falls below a relative tolerance ([[Numerical Rank]]).[^3]
- More sophisticated rank-revealing QR techniques exist; the [[Singular Value Decomposition Theorem|SVD]] is the most reliable (but most expensive) way to determine numerical rank.[^3]
- With column pivoting, Householder QR gives a useful solution for (nearly) rank-deficient problems where the [[Normal Equations]] fail outright.[^4]
- [[Pivoting]]
- [[Linear Least Squares Problem]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=156)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=156)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=157)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=164)
