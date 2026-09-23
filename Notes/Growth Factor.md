---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Growth Factor)[^1]
> For [[LU Decomposition|LU factorization]] by [[Gaussian Elimination]], the growth factor $\rho$ is the ratio of the largest entry (in magnitude) produced at any stage of the factorization (typically $U$) to the largest entry of $A$.

> [!abstract] Theorem 2 (Wilkinson's Backward Error Bound)[^1]
> The computed factorization is the exact factorization of $A + E$, where
> $$
> \begin{align}
> \frac{\lVert E \rVert}{\lVert A \rVert} \leq \rho\, n^2\, \epsilon_{mach}
> \end{align}
> $$

# Properties
- Without [[Pivoting]], $\rho$ can be arbitrarily large, so Gaussian elimination without pivoting is unstable.[^1]
- With [[Partial Pivoting]], $\rho$ can be as large as $2^{n-1}$ (entries can double at each stage), but this is extremely rare. In practice there is little or no growth, and a realistic bound is $\frac{\lVert E \rVert}{\lVert A \rVert} \lesssim n\, \epsilon_{mach}$.[^1]
- With [[Complete Pivoting]], $\rho$ is even smaller.
- Since the [[Backward Error]] is small, the relative [[Residual of Linear System|residual]] is small regardless of conditioning. So a small residual alone does not mean an accurate solution unless the system is well-conditioned ([[Condition Number of a Matrix]]).[^1]
- [[Machine Epsilon]]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=96)
