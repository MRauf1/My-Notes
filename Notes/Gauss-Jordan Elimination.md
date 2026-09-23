---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Gauss-Jordan Elimination)[^1]
> Gauss-Jordan elimination is a variation of [[Gaussian Elimination]] in which the matrix is reduced to [[Diagonal Matrix|diagonal]] form rather than merely to triangular form. Entries both below *and above* the diagonal are annihilated in each column. The resulting diagonal system is solved by $x_i = b_i / d_{ii}$.

# Properties
- Costs about $n^3/2$ multiplications and a similar number of additions, which is 50% more than Gaussian elimination.[^2]
- The final solution phase needs only $n$ divisions. That is much cheaper than solving a triangular system, but not enough to make up for the costlier elimination phase.[^2]
- Multipliers can exceed 1 in magnitude even with [[Pivoting]], which is a numerical disadvantage.[^2]
- It may still be preferred in some situations because of the extreme simplicity of its final solution phase.[^2]
- Computing the inverse: reducing $[A \mid I]$ to $[I \mid A^{-1}]$ gives $A^{-1}$ ([[Matrix Inverse Algorithm]], i.e., reduction to [[Reduced Row Echelon Form]]). The operation count is about the same as inverting via [[LU Decomposition]] followed by forward- and back-substitution.[^2]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=99)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=100)
