---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Gaussian Elimination)[^1]
> Gaussian elimination reduces a general [[Linear System of Equations|linear system]] $Ax = b$ to an equivalent [[Upper Triangular Matrix|upper triangular]] system by successively applying [[Elementary Elimination Matrix|elementary elimination matrices]] $M_1, \dots, M_{n-1}$, one per column:
> $$
> \begin{align}
> MA = M_{n-1} \cdots M_1 A = U, \qquad Mb = M_{n-1} \cdots M_1 b
> \end{align}
> $$
> Setting $L = M^{-1} = L_1 \cdots L_{n-1}$ (unit lower triangular) gives $A = LU$, so Gaussian elimination is also known as [[LU Decomposition|LU factorization]]. The triangular system is then solved by [[Back-Substitution]].

The strategy is to transform a general system, via a nonsingular linear transformation, into a triangular one that is easy to solve by successive substitution. It stops at triangular form; compare [[Gauss-Jordan Elimination]], which goes on to diagonal form.[^2]

The process breaks down if the leading diagonal entry of the remaining unreduced submatrix is zero, since computing multipliers divides by it. This is fixed by [[Pivoting]]. If a column has no nonzero entry on or below the diagonal, then $M_k = I$ and the factorization still completes, but $U$ (and hence $A$) is singular and back-substitution fails. In floating-point arithmetic, a tiny (rather than exactly zero) pivot is the more insidious problem.[^3]

# Properties
- Costs about $n^3/3$ multiplications and a similar number of additions.[^4]
- Without pivoting it is unstable, because the [[Growth Factor]] can be arbitrarily large. With [[Partial Pivoting]] it is stable in practice.[^5]
- Pivoting is not needed (the method is stable without it) for [[Diagonally Dominant Matrix|matrices diagonally dominant by columns]] and for symmetric [[Positive Definite Matrix|positive definite matrices]].[^6]
- Gaussian elimination with partial pivoting almost always yields a very small relative [[Residual of Linear System|residual]], however ill-conditioned the system is.[^5]
- [[Scaling of Linear System|Scaling]] affects the sequence of pivots.
- [[Row Echelon Form]]
- Structure-exploiting alternatives: [[Cholesky Decomposition]] (symmetric positive definite), [[Symmetric Indefinite Factorization]], [[Banded Matrix]], [[Tridiagonal Matrix]], [[Sparse Matrix]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=88)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=86)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=90)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=99)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=96)
[^6]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=97)
