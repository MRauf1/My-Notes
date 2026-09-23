---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Complete Pivoting)[^1]
> In [[Gaussian Elimination]], complete pivoting searches the entire remaining unreduced submatrix for its largest-magnitude entry and permutes it into the diagonal pivot position. This interchanges columns as well as rows, giving
> $$
> \begin{align}
> PAQ = LU
> \end{align}
> $$
> where $L$ is unit lower triangular, $U$ is upper triangular, and $P, Q$ are [[Permutation Matrix|permutation matrices]] reordering rows and columns. $Ax = b$ is solved by [[Forward-Substitution]] on $Ly = Pb$, then [[Back-Substitution]] on $Uz = y$, and finally $x = Qz$.

# Properties
- It is theoretically more stable than [[Partial Pivoting]] and yields an even smaller [[Growth Factor]], in theory and in practice. The pivot search is much more expensive, though, and the extra stability is usually not worth it.[^1][^2]

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=95)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=96)
