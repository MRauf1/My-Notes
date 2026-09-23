---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Rank-One Modification)[^1]
> A rank-one modification of an $n \times n$ matrix $A$ is the addition or subtraction of an outer product $uv^T$ of two nonzero $n$-vectors $u, v$. The outer product has [[Rank]] one, and every rank-one matrix can be written this way. For example, changing the single entry $a_{jk}$ to $\tilde{a}_{jk}$ gives $A - \alpha e_j e_k^T$ with $\alpha = a_{jk} - \tilde{a}_{jk}$.

> [!abstract] Theorem 2 (Sherman-Morrison Formula)[^1]
> $$
> \begin{align}
> (A - uv^T)^{-1} = A^{-1} + A^{-1}u\,(1 - v^T A^{-1} u)^{-1}\, v^T A^{-1}
> \end{align}
> $$
> This gives the inverse of a rank-one modification of a matrix whose inverse is already known. It can be verified by direct multiplication.

Evaluating it takes only $O(n^2)$ work (matrix-vector products), instead of the $O(n^3)$ needed to invert the modified matrix from scratch.[^2]

> [!abstract] Theorem 3 (Rank-One Updating of a Solution)[^2]
> Applied to $(A - uv^T)x = b$,
> $$
> \begin{align}
> x = A^{-1}b + A^{-1}u\,(1 - v^T A^{-1} u)^{-1}\, v^T A^{-1} b
> \end{align}
> $$
> To avoid explicit inverses, given the [[LU Decomposition]] of $A$:
> 1. Solve $Az = u$ for $z$ (independent of $b$, so it can be reused for multiple right-hand sides).
> 2. Solve $Ay = b$ for $y$.
> 3. $x = y + \dfrac{v^T y}{1 - v^T z}\, z$.
>
> This takes only triangular solves and inner products, so $O(n^2)$ work.

The factorization itself can be updated with similar techniques. Successive updates carry no general guarantee of numerical stability, so these formulas should be used with caution.[^2]

# Properties
- [[Woodbury Formula]] (generalization to rank-$k$ modifications)
- [[Matrix Inverse]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=101)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=102)
