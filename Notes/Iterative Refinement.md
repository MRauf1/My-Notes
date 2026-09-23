---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Iterative Refinement)[^1]
> Given an approximate solution $x_0$ to $Ax = b$ (e.g., from an [[LU Decomposition]]), repeat for $k = 0, 1, 2, \dots$:
> 1. Compute the [[Residual of Linear System|residual]] $r_k = b - Ax_k$.
> 2. Solve $As_k = r_k$ for $s_k$ using the existing LU factors.
> 3. Set $x_{k+1} = x_k + s_k$.
>
> In exact arithmetic, $Ax_1 = Ax_0 + As_0 = (b - r_0) + r_0 = b$. Repeating until convergence can produce a residual as small as the arithmetic precision allows.

# Properties
- It needs double the storage, since both $A$ (for the residual) and its LU factors (for the solves) must be kept.[^1]
- For maximum benefit, the residual usually has to be computed in higher precision than the initial solution was.[^1]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=104)
