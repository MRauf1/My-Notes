---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!abstract] Theorem 1 (Cholesky Factorization of a Positive Semidefinite Matrix)[^1]
> Every symmetric [[Positive Semidefinite Matrix|positive semidefinite]] $A \in \mathbb{R}^{n \times n}$ has a factorization $A = LL^T$ with $L$ lower triangular with nonnegative diagonal. If $\operatorname{rank}(A) = r < n$, this factorization is not unique.

> [!info] Definition 2 (Pivoted Cholesky Factorization)[^1][^2]
> Cholesky with complete (diagonal) [[Pivoting]]: at step $k$, symmetrically swap the largest remaining diagonal entry into the pivot position, and stop once all remaining diagonal entries are below a tolerance. For $A$ of rank $r$ this gives
> $$
> \begin{align}
> P^T A P = R^T R, \qquad R = \begin{bmatrix} R_{11} & R_{12} \\ 0 & 0 \end{bmatrix}
> \end{align}
> $$
> where $P$ is a [[Permutation Matrix]] and $R_{11} \in \mathbb{R}^{r \times r}$ is upper triangular with positive diagonal. The rank is thereby revealed as the number of steps taken.

The standard [[Cholesky Decomposition|Cholesky]] algorithm for strictly positive definite matrices fails on a semidefinite matrix. It meets a zero pivot (division by zero), or rounding turns a zero pivot slightly negative, and the square root of a negative number is undefined.

# Properties
- Work, for rank $r$, with the full right-looking algorithm: step $k$ performs a symmetric rank-1 update of the $(n-k) \times (n-k)$ trailing submatrix, so the total is
$$
\begin{align}
\sum_{k=1}^{r} (n-k)^2 \approx n^2 r - n r^2 + \frac{r^3}{3} \ \text{flops}
\end{align}
$$
  That is about half as many multiplications and half as many additions, plus $r$ square roots and $O(nr)$ comparisons for the pivot search. For $r = n$ this recovers Cholesky's $n^3/6$ multiplications and $n^3/6$ additions.
- Low-rank (partial) variant: only the diagonal of $A$ and the $r$ selected columns are accessed. This costs about $n r^2$ flops and $O(nr)$ storage, versus $n(n+1)/2$ for the full factor. It is a greedy low-rank approximation $A \approx L_r L_r^T$, used e.g. for kernel matrices in Gaussian processes.
- Storage for the full algorithm: $n(n+1)/2$ entries (the lower triangle, overwritten in place). The factor $R_{11}, R_{12}$ has $r(r+1)/2 + r(n-r)$ entries.
- Solving a consistent system $Ax = b$: two triangular solves of size $r$ (about $r^2$ multiplications) plus $O(nr)$ for the $R_{12}$ block.
- Backward stability: the computed factor is exact for $A + E$ with $\lVert E \rVert \le 4r(r+1)(\lVert W \rVert + 1)^2 \epsilon_{mach} \lVert A \rVert + O(\epsilon_{mach}^2)$, where $W = A_{11}^{-1} A_{12}$. With complete pivoting $\lVert W \rVert_2^2 \le \tfrac{1}{3}(n - r)(4^r - 1)$, and $\lVert W \rVert$ is small in practice.[^1]
- Implemented in LAPACK as `xPSTRF`.
- Alternatives for semidefinite matrices:
	- The [[LDLT Factorization]] with $D \geq 0$.
	- Regularizing to a strictly positive definite matrix, e.g., $A + \epsilon I$.
	- Removing the null space, then applying standard Cholesky.

## Application: Laplace–Beltrami Operator
- With the sign convention $\Delta = -\operatorname{div}\nabla$, the Laplace–Beltrami operator on a closed, connected surface is symmetric positive semidefinite but not positive definite. Its kernel is the constant functions.
- Removing the constant mode (restricting to mean-zero functions) makes it symmetric strictly positive definite.
- The discrete cotan Laplacian (stiffness matrix) of a connected mesh behaves the same way: it is symmetric PSD with $\ker L = \operatorname{span}\{\mathbf{1}\}$.
- In practice the constant mode is removed by pinning one vertex (deleting its row and column), by adding a small multiple of the mass matrix ($L + \epsilon M$), or by using a boundary with Dirichlet conditions. The result is symmetric positive definite, so standard sparse Cholesky applies (see [[Sparse Matrix]]).

[^1]: [Analysis of the Cholesky Decomposition of a Semi-definite Matrix (Higham 1990)](https://eprints.maths.manchester.ac.uk/1193/1/high90c.pdf)
[^2]: [Cholesky Factorization (Higham 2008)](https://people.tamu.edu/~rojas//higham-choleskyfactorization.pdf)
