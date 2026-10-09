---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Householder QR Factorization)[^1]
> For $A \in \mathbb{R}^{m \times n}$, apply a sequence of [[Householder Transformation|Householder transformations]] $H_1, \dots, H_n$, where $H_k$ annihilates the subdiagonal entries of column $k$ of the current matrix, proceeding column by column from left to right:
> $$
> \begin{align}
> H_n \cdots H_1 A = \begin{bmatrix} R \\ O \end{bmatrix}
> \end{align}
> $$
> with $R$ [[Upper Triangular Matrix|upper triangular]]. Since the product of orthogonal matrices is orthogonal, taking $Q^T = H_n \cdots H_1$, i.e., $Q = H_1 \cdots H_n$, gives the [[QR Decomposition]] $A = Q \begin{bmatrix} R \\ O \end{bmatrix}$.

Each $H_k$ is applied only to the remaining unreduced submatrix, and it does not disturb the previously reduced columns, so the zeros are preserved.[^2]

![[Householder QR Factorization Algorithm.png]]

Here $a_j$ denotes the $j$-th column of (the current) $A$. The rescaling needed for a robust implementation is omitted, and an efficient implementation avoids operations on the leading zeros of each $v_k$.[^2]

To solve the [[Linear Least Squares Problem|least squares problem]] $Ax \cong b$, apply the same transformations to $b$, obtaining the equivalent triangular problem $\begin{bmatrix} R \\ O \end{bmatrix} x \cong Q^Tb = \begin{bmatrix} c_1 \\ c_2 \end{bmatrix}$, and solve $Rx = c_1$ by [[Back-Substitution]]. $Q$ never needs to be formed explicitly.[^3]

> [!abstract] Theorem 2 (Rank Deficiency)[^4]
> If $\beta_k = 0$ at step $k$, the column is already reduced and the step is skipped, so the factorization still completes. By the sign choice of $\alpha_k$, $\beta_k = 0$ only if the column is already zero on and below the diagonal, meaning column $k$ of $A$ is linearly dependent on the first $k - 1$ columns; then $R$ has a zero diagonal entry and is singular.

A more insidious problem is a tiny but nonzero diagonal entry of $R$, indicating near rank deficiency; this is handled by [[QR Factorization with Column Pivoting]].[^4]

# Properties
- Storage: $R$ and the Householder vectors (the implicit representation of $Q$) can overwrite the space of $A$. An explicit $Q_1$ needs additional storage.[^5]
- Cost: about $mn^2 - n^3/3$ multiplications and as many additions. For $m \approx n$ this is about the same as the [[Normal Equations]]; for $m \gg n$ it is about twice as much.[^6]
- Accuracy: relative error proportional to $\operatorname{cond}(A) + \lVert r \rVert_2 [\operatorname{cond}(A)]^2$, which is the best possible since it matches the inherent [[Sensitivity of Linear Least Squares Problem|sensitivity of the problem]]. It can be expected to break down (in back-substitution) only if $\operatorname{cond}(A) \approx 1/\epsilon_{mach}$ or worse.[^6]
- The most efficient and accurate orthogonalization method for dense least squares problems.[^6]
- [[Givens Rotation]] (alternative, about 50% more work)
- [[Modified Gram-Schmidt Algorithm]] (alternative)

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=144)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=145)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=145)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=144)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=152)
[^6]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=164)
