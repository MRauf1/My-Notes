---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Total Least Squares)[^1]
> Ordinary [[Linear Least Squares Problem|least squares]] seeks the closest compatible system by perturbing only the right-hand side: minimize $\lVert b - y \rVert_2$ subject to $y \in \operatorname{span}(A)$. Total least squares seeks the closest compatible system $[\hat{A} \ y]$ (i.e., $y \in \operatorname{span}(\hat{A})$) to $[A \ b]$, allowing both the matrix and the right-hand side to vary.

Ordinary least squares implicitly assumes $A$ is exact and only $b$ is noisy, which justifies minimizing vertical distances between data points and the fitted curve. When all variables carry measurement error, minimizing orthogonal distances to the curve, i.e., total least squares, may make more sense.[^1]

> [!abstract] Theorem 2 (Solution via SVD)[^2]
> Let $[A \ b] = U\Sigma V^T$ be the [[Singular Value Decomposition Theorem|SVD]] of the $m \times (n+1)$ matrix. If $\sigma_{n+1} < \sigma_n$ and $v_{n+1,n+1} \neq 0$, the total least squares solution is
> $$
> \begin{align}
> x = -\frac{1}{v_{n+1,n+1}} \begin{bmatrix} v_{1,n+1} \\ \vdots \\ v_{n,n+1} \end{bmatrix}
> \end{align}
> $$

A compatible $[\hat{A} \ y]$ must have rank at most $n$, and the closest such matrix (by the [[Low-Rank Matrix Approximation Theorem]]) drops $\sigma_{n+1}$. Its solution satisfies $[\hat{A} \ y] \begin{bmatrix} x \\ -1 \end{bmatrix} = 0$, so $[x^T, -1]^T$ lies in the [[Kernel|null space]] and is proportional to $v_{n+1}$; scale $v_{n+1}$ so its last component is $-1$.[^2]

# Properties
- [[Linear Least Squares Problem]]
- [[Principal Component Analysis]] (also minimizes orthogonal distances to a subspace)
- [[Low-Rank Matrix Approximation Theorem]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=161)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=162)
