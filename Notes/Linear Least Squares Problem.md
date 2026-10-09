---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Linear Least Squares Problem)[^1]
> Let $A \in \mathbb{R}^{m \times n}$, $b \in \mathbb{R}^m$. The linear least squares problem, written
> $$
> \begin{align}
> Ax \cong b
> \end{align}
> $$
> is to find $x \in \mathbb{R}^n$ minimizing the 2-norm of the [[Residual of Linear System|residual]] $r = b - Ax$:
> $$
> \begin{align}
> \min_x \lVert r \rVert_2^2 = \min_x \lVert b - Ax \rVert_2^2 = \min_x \sum_{i=1}^m \left( b_i - \sum_{j=1}^n a_{ij} x_j \right)^2
> \end{align}
> $$

The typical case is an overdetermined [[Linear System of Equations|system]] ($m > n$): more equations than unknowns, so $b$ generally does not lie in $\operatorname{span}(A)$ and there is no exact solution. Rather than fitting noisy data exactly (as in interpolation, where #parameters = #data points), one deliberately uses more measurements than parameters and forgoes an exact fit to smooth out measurement errors. More generally, least squares is the canonical way to project a vector from a higher-dimensional space onto a lower-dimensional subspace, i.e., to get a lower-dimensional approximation of a higher-dimensional object.[^2]

Any norm of the residual could be minimized, but the 2-norm is preferred because of its relationship with the [[Inner Product]] and orthogonality, its smoothness and strict convexity, and its computational convenience.[^1]

> [!abstract] Theorem 2 (Existence and Uniqueness)[^3]
> A solution of $Ax \cong b$ always exists. The closest point $y = Ax \in \operatorname{span}(A)$ to $b$ is unique, and the solution $x$ is unique if and only if $A$ has full column rank, i.e., $\operatorname{rank}(A) = n$.

Existence: $\varphi(y) = \lVert b - y \rVert_2$ is continuous and coercive on $\mathbb{R}^m$, so it attains a minimum on the closed set $\operatorname{span}(A)$; it is strictly [[Convex Function|convex]] on the [[Convex Set|convex set]] $\operatorname{span}(A)$, so the minimizer $y$ is unique. Uniqueness of $x$: if $Ax_1 = y = Ax_2$, then $z = x_2 - x_1$ satisfies $Az = 0$, and $z \neq 0$ forces the columns of $A$ to be [[Linearly Independent|linearly dependent]]. If $\operatorname{rank}(A) < n$, $A$ is called rank-deficient.[^3]

> [!abstract] Theorem 3 (Orthogonality Characterization)[^4]
> $x$ solves $Ax \cong b$ if and only if the residual is orthogonal to $\operatorname{span}(A)$:
> $$
> \begin{align}
> A^T r = A^T(b - Ax) = 0 \iff A^T A x = A^T b
> \end{align}
> $$
> i.e., $x$ satisfies the [[Normal Equations]]. Equivalently, $y = Ax$ is the [[Orthogonal Projection]] of $b$ onto $\operatorname{span}(A)$, and
> $$
> \begin{align}
> b = Pb + P_\perp b = Ax + (b - Ax) = y + r, \qquad y \in \operatorname{span}(A),\ r \in \operatorname{span}(A)^\perp
> \end{align}
> $$
> where $P$ is the [[Projector|orthogonal projector]] onto $\operatorname{span}(A)$.

This is the [[Best Approximation Theorem]] applied to the subspace $\operatorname{span}(A) = $ [[Matrix Column Space|column space]] of $A$. Replacing $b$ by $Pb$ gives the consistent overdetermined system $Ax = Pb$; premultiplying by $A^T$ (using $A^TP = A^TP^T = (PA)^T = A^T$) gives the normal equations, while premultiplying by $Q^T$, where $Q \in \mathbb{R}^{m \times n}$ has orthonormal columns spanning $\operatorname{span}(A)$ (so $P = QQ^T$ and $Q^TP = Q^T$), gives the square system $Q^TAx = Q^Tb$. Choosing $Q$ so that this system is upper triangular is the idea behind [[QR Decomposition|QR]] methods.[^5]

> [!abstract] Theorem 4 (Triangular Least Squares Problem)[^6]
> If $m > n$ and $R \in \mathbb{R}^{n \times n}$ is [[Upper Triangular Matrix|upper triangular]], then for
> $$
> \begin{align}
> \begin{bmatrix} R \\ O \end{bmatrix} x \cong \begin{bmatrix} c_1 \\ c_2 \end{bmatrix}, \qquad \lVert r \rVert_2^2 = \lVert c_1 - Rx \rVert_2^2 + \lVert c_2 \rVert_2^2
> \end{align}
> $$
> the solution is obtained by solving $Rx = c_1$ by [[Back-Substitution]], and the minimum residual is $\lVert r \rVert_2 = \lVert c_2 \rVert_2$.

Since [[Orthogonal Matrix|orthogonal transformations]] preserve the 2-norm, multiplying both sides of $Ax \cong b$ by an orthogonal $Q^T$ leaves the solution unchanged, so the goal of the orthogonalization methods is to reach this triangular form. [[Gaussian Elimination]] cannot be used, since it does not preserve the Euclidean norm and hence does not preserve the least squares solution.[^7]

> [!abstract] Theorem 5 (Minimum-Norm Solution via SVD)[^8]
> For $A$ of any shape or rank with [[Singular Value Decomposition Theorem|SVD]] $A = U\Sigma V^T$, the least squares solution of $Ax \cong b$ with minimum Euclidean norm is
> $$
> \begin{align}
> x = \sum_{\sigma_i \neq 0} \frac{u_i^T b}{\sigma_i} v_i = A^+ b
> \end{align}
> $$
> where $A^+$ is the [[Pseudoinverse]]. In the full-column-rank case with reduced SVD $A = U_1 \Sigma_1 V^T$, this is $x = V \Sigma_1^{-1} U_1^T b$.

Rank deficiency (non-unique solutions, singular $R$ and $A^TA$) usually signals a poorly designed experiment, insufficient data, or an inadequate or redundant model, so the problem should ideally be reformulated. If one proceeds anyway, the standard choice is the minimum-norm solution, computed by [[QR Factorization with Column Pivoting]] or by the SVD; this also handles underdetermined problems ($m < n$), whose columns are necessarily dependent. Since rank is rarely clear-cut in practice, a relative tolerance is used to detect near rank deficiency ([[Numerical Rank]]); a nearly rank-deficient problem has a solution sensitive to data perturbations. For ill-conditioned or nearly rank-deficient problems, dropping relatively tiny $\sigma_i$ from the SVD sum makes the solution much less sensitive.[^9]

# Types
- [[Total Least Squares]] (errors in both $A$ and $b$)
- [[Linear Regression]] (statistical counterpart)

# Algorithm
Comparison of methods for dense problems with $m \geq n$:[^10]
- [[Normal Equations]] + [[Cholesky Decomposition|Cholesky]]: about $mn^2/2 + n^3/6$ multiplications. Relative error $\propto [\operatorname{cond}(A)]^2$; breaks down when $\operatorname{cond}(A) \approx 1/\sqrt{\epsilon_{mach}}$.
- [[Augmented System Method]]: useful for large sparse problems.
- [[Householder QR Factorization]]: about $mn^2 - n^3/3$ multiplications. Relative error $\propto \operatorname{cond}(A) + \lVert r \rVert_2 [\operatorname{cond}(A)]^2$, which is optimal since it matches the inherent [[Sensitivity of Linear Least Squares Problem|sensitivity of the problem]]; breaks down only when $\operatorname{cond}(A) \approx 1/\epsilon_{mach}$. The most efficient and accurate orthogonalization method for dense problems.
- [[Givens Rotation|Givens QR]]: about 50% more work than Householder; used when selectivity (sparsity) matters.
- [[Modified Gram-Schmidt Algorithm|Modified Gram-Schmidt]]: gives explicit $Q_1$, but needs separate storage.
- [[QR Factorization with Column Pivoting]]: handles (near) rank deficiency.
- [[Singular Value Decomposition Theorem|SVD]]: most expensive (cost $\propto mn^2 + n^3$ with a constant of 4 to 10 or more), but most robust and reliable.

For $m \approx n$, normal equations and Householder cost about the same; for $m \gg n$, Householder costs about twice as much. The extra cost may not be worth it when the problem is well-conditioned enough that the normal equations give adequate accuracy, but for (nearly) rank-deficient problems Householder with column pivoting succeeds where the normal equations fail outright.[^11]

# Properties
- [[Normal Equations]]
- [[Sensitivity of Linear Least Squares Problem]]
- [[QR Decomposition]]
- [[Orthogonal Projection]]
- [[Projector]]
- [[Best Approximation Theorem]]
- [[Pseudoinverse]]
- [[Residual Sum of Squares]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=126)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=125)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=129)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=131)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=132)
[^6]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=140)
[^7]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=139)
[^8]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=158)
[^9]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=155)
[^10]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=163)
[^11]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=164)
