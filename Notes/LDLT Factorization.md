---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (LDLᵀ Factorization)[^1]
> For a symmetric [[Positive Definite Matrix|positive definite]] matrix $A$,
> $$
> \begin{align}
> A = LDL^T
> \end{align}
> $$
> where $L$ is unit [[Lower Triangular Matrix|lower triangular]] and $D$ is [[Diagonal Matrix|diagonal]] with positive diagonal entries.

It is a variant of the [[Cholesky Decomposition|Cholesky factorization]] $A = \tilde{L}\tilde{L}^T$, related by $\tilde{L} = L D^{1/2}$. So $d_{ii} = \tilde{\ell}_{ii}^2$: the diagonal of $D$ holds the squares of the diagonal entries of the Cholesky factor.[^1]

# Properties
- It needs no square roots, whereas the Cholesky algorithm needs $n$ of them.[^1]
- Work: about $n^3/6$ multiplications and $n^3/6$ additions, the same leading order as Cholesky. Storage: $n(n+1)/2$ entries ($L$ strictly below the diagonal, $D$ on it).
- Solving $Ax = b$: [[Forward-Substitution]] with $L$ (about $n^2/2$ multiplications), $n$ divisions by $D$, then [[Back-Substitution]] with $L^T$ (about $n^2/2$ multiplications). That is about $n^2$ multiplications in total.
- It is the symmetric counterpart of the [[LDU Decomposition]] ($U = L^T$).
- [[Symmetric Indefinite Factorization]] (the pivoted generalization for indefinite $A$)

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=106)
