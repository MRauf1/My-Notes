---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Row and Column Scaling)[^1]
> For nonsingular [[Diagonal Matrix|diagonal matrices]] $D_1, D_2$, the system $Ax = b$ can be scaled to
> $$
> \begin{align}
> (D_1 A D_2)\, (D_2^{-1} x) = D_1 b
> \end{align}
> $$
> Row scaling ($D_1$) leaves the solution unchanged. Column scaling ($D_2$) changes it to $D_2^{-1}x$, from which $x$ is easily recovered.

In practice, scaling affects the [[Condition Number of a Matrix|conditioning]] of the system and the choice of pivots in [[Gaussian Elimination]], and both affect the accuracy of the computed solution. So scaling can improve or degrade stability and accuracy.[^1]

A well-formulated problem should have:[^2]
- commensurate units for the unknowns (column scaling),
- weights on the equations that reflect their relative importance (row scaling),
- scaling that accounts for the relative accuracy of the input data.

Under these conditions, [[Pivoting]] usually produces a solution as accurate as the problem warrants. A badly skewed scaling, however, can make the system ill-conditioned.

# Properties
- Accuracy is usually better when all matrix entries have about the same order of magnitude, or better still, when the uncertainties in the entries are all about the same size.[^1]
- Scaling can itself introduce rounding errors unless care is taken, e.g., by using only powers of the arithmetic base as scaling factors.[^1]
- A large condition number caused by poor scaling can be fixed by rescaling; one caused by near singularity cannot.

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=103)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=96)
