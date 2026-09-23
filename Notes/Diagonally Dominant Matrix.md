---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Diagonally Dominant by Columns)[^1]
> A matrix $A \in \mathbb{R}^{n \times n}$ is diagonally dominant by columns if each diagonal entry is larger in magnitude than the sum of the magnitudes of the other entries in its column:
> $$
> \begin{align}
> \sum_{i=1, i \neq j}^{n} |a_{ij}| < |a_{jj}|, \quad j = 1, \dots, n
> \end{align}
> $$

# Properties
- [[Gaussian Elimination]] (LU factorization) is stable without [[Pivoting]] for such matrices. If [[Partial Pivoting]] is used anyway, no row interchanges occur.[^1]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=97)
