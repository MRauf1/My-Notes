---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Normal Equations)[^1]
> For a [[Linear Least Squares Problem|linear least squares problem]] $Ax \cong b$ with $A \in \mathbb{R}^{m \times n}$, the system of normal equations is the $n \times n$ symmetric linear system
> $$
> \begin{align}
> A^T A x = A^T b
> \end{align}
> $$
> The matrix $A^TA$, whose $(i,j)$ entry is the inner product of the $i$-th and $j$-th columns of $A$, is called the cross-product matrix of $A$.

> [!abstract] Theorem 2 (Derivation and Sufficiency)[^2]
> Setting the gradient of $\varphi(x) = \lVert b - Ax \rVert_2^2 = b^Tb - 2x^TA^Tb + x^TA^TAx$ to zero shows every minimizer satisfies $A^TAx = A^Tb$. The [[Hessian Matrix]] of $\varphi$ is $2A^TA$, and
> $$
> \begin{align}
> A^TA \text{ is } \text{positive definite} \iff \operatorname{rank}(A) = n
> \end{align}
> $$
> so when $A$ has full column rank the solution of the normal equations is the unique least squares solution.

The same equations follow geometrically: the residual $r = b - Ax$ must be orthogonal to $\operatorname{span}(A)$, i.e., $A^Tr = 0$.[^3]

> [!info] Definition 3 (Normal Equations Method)[^4]
> If $A$ has full column rank, solve $Ax \cong b$ by computing the [[Cholesky Decomposition]] $A^TA = LL^T$ and then solving the triangular systems $Ly = A^Tb$ ([[Forward-Substitution]]) and $L^Tx = y$ ([[Back-Substitution]]).

The method illustrates that a problem transformation that is legitimate in theory is not always advisable numerically. It can be disappointingly inaccurate for two reasons:[^5]
- Information can be lost (rounded away) in forming $A^TA$ and $A^Tb$ in floating-point arithmetic.
- $\operatorname{cond}(A^TA) = [\operatorname{cond}(A)]^2$. The least squares problem itself only has a condition-squaring effect when the residual is large ([[Sensitivity of Linear Least Squares Problem]]), but the normal equations suffer it even when the fit is good and the residual small. In this sense the normal equations method is not a [[Stable Algorithm|stable algorithm]].

# Properties
- Cost: forming $A^TA$ (exploiting symmetry) takes about $mn^2/2$ multiplications and as many additions; the Cholesky factorization takes about $n^3/6$ of each. Reducing to an $n \times n$ system is very attractive when $m \gg n$.[^6]
- Relative error of the computed solution is proportional to $[\operatorname{cond}(A)]^2$, and the Cholesky factorization can be expected to break down if $\operatorname{cond}(A) \approx 1/\sqrt{\epsilon_{mach}}$ or worse ([[Machine Epsilon]]).[^6]
- Fails outright for rank-deficient $A$, since $A^TA$ is then singular.[^7]
- Pivoting along the diagonal of the [[Augmented System Method|augmented system]] reproduces the normal equations.
- [[Positive Definite Matrix]]
- [[Householder QR Factorization]] (the stable alternative)

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=130)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=130)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=131)
[^4]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=137)
[^5]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=138)
[^6]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=163)
[^7]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=164)
