---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Augmented System)[^1]
> The [[Linear Least Squares Problem|least squares problem]] $Ax \cong b$, $A \in \mathbb{R}^{m \times n}$, is equivalent to the $(m+n) \times (m+n)$ square system obtained from the residual definition $r + Ax = b$ and the orthogonality condition $A^Tr = 0$:
> $$
> \begin{align}
> \begin{bmatrix} I & A \\ A^T & O \end{bmatrix} \begin{bmatrix} r \\ x \end{bmatrix} = \begin{bmatrix} b \\ 0 \end{bmatrix}
> \end{align}
> $$
> whose solution gives both $x$ and the residual $r$.

> [!info] Definition 2 (Scaled Augmented System)[^2]
> Since the relative scales of $r$ and $x$ are arbitrary, introduce a scaling parameter $\alpha > 0$:
> $$
> \begin{align}
> \begin{bmatrix} \alpha I & A \\ A^T & O \end{bmatrix} \begin{bmatrix} r/\alpha \\ x \end{bmatrix} = \begin{bmatrix} b \\ 0 \end{bmatrix}
> \end{align}
> $$
> $\alpha$ controls the relative weights of the two block rows when choosing pivots. A rule of thumb is $\alpha = \max_{i,j} |a_{ij}| / 1000$, though experimentation may be needed.

Drawbacks: the matrix is symmetric but not positive definite, it is larger than the original problem, and it requires storing two copies of $A$. Pivoting along the diagonal (block elimination of the $2 \times 2$ block system) just reproduces the [[Normal Equations]]. The one gain is that other [[Pivoting|pivoting]] strategies become available in a [[Symmetric Indefinite Factorization|symmetric indefinite]] or [[LU Decomposition|LU]] factorization, which can help numerically or otherwise.[^1]

# Properties
- A straightforward dense implementation costs $O((m+n)^3)$, so the special structure must be exploited; done carefully, it is effective for large [[Sparse Matrix|sparse]] least squares problems (e.g., in MATLAB).[^2]
- [[Linear Least Squares Problem]]
- [[Normal Equations]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=138)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=139)
