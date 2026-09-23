---
tags:
  - mathematics
  - linear_algebra
  - computer_science
  - numerical_analysis
---

# Definition

The process, when dealing with [[Linear System of Equations|linear systems]], where we substitute the known [[Variable|variable]] values from the later [[Equation|equations]] into the earlier equations.[^1]

> [!info] Definition 2 (Back-Substitution for Upper Triangular Systems)[^2]
> For an [[Upper Triangular Matrix|upper triangular]] system $Ux = b$,
> $$
> \begin{align}
> x_n &= \frac{b_n}{u_{nn}} \\
> x_i &= \frac{b_i - \sum_{j=i+1}^{n} u_{ij} x_j}{u_{ii}}, \quad i = n-1, \dots, 1
> \end{align}
> $$

A zero diagonal entry causes the algorithm to fail, which is expected since a triangular matrix with a zero diagonal entry is singular ([[Triangular Matrix Invertibility]]).[^3]

# Properties
- [[Forward-Substitution]] (the lower triangular counterpart)
- [[Gaussian Elimination]]
- [[LU Decomposition]]

[^1]: [Linear Algebra (Cambridge Mathematical Textbooks) -- Elizabeth S_ Meckes, Mark W_ Meckes](zotero://open-pdf/library/items/HG5B3R7J?page=34)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=85)
[^3]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=86)