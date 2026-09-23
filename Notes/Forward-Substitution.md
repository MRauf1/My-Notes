---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Forward-Substitution)[^1]
> For a [[Lower Triangular Matrix|lower triangular]] system $Lx = b$, successive substitution is called forward-substitution:
> $$
> \begin{align}
> x_1 &= \frac{b_1}{\ell_{11}} \\
> x_i &= \frac{b_i - \sum_{j=1}^{i-1} \ell_{ij} x_j}{\ell_{ii}}, \quad i = 2, \dots, n
> \end{align}
> $$

A zero diagonal entry causes the algorithm to fail, which is expected since a triangular matrix with a zero diagonal entry is singular ([[Triangular Matrix Invertibility]]).[^2]

# Properties
- [[Back-Substitution]] (the upper triangular counterpart)
- Requires about $n^2/2$ multiplications and a similar number of additions.
- [[LU Decomposition]]: $Ax = b$ is solved by forward-substitution on $Ly = b$ followed by back-substitution on $Ux = y$.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=85)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=86)
