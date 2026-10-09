---
tags:
  - computer_science
  - numerical_analysis
---

# Definition
> [!info] Definition 1 (Numerical Rank)[^1]
> The numerical rank of a matrix $A$ is the number of its [[Singular Value|singular values]] that exceed a given threshold relative to the largest singular value $\sigma_{\max}$; singular values below the threshold are treated as negligible.

The exact [[Rank]] equals the number of nonzero singular values, but in practice some singular values may be very small yet nonzero, so the rank is not well-determined. A numerical rank of $k$ means $A$ is within the given threshold of a matrix of rank $k$ (see [[Low-Rank Matrix Approximation Theorem]]).[^1]

# Properties
- Using the [[Singular Value Decomposition Theorem|SVD]] to determine numerical rank is more reliable, though more expensive, than [[QR Factorization with Column Pivoting]].[^1]
- A nearly rank-deficient [[Linear Least Squares Problem|least squares problem]] has a solution that is sensitive to perturbations in the data.[^2]
- [[Condition Number of a Matrix]] ($\operatorname{cond}_2(A) = \sigma_{\max}/\sigma_{\min}$ measures closeness to rank deficiency)

[^1]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=160)
[^2]: [Scientific Computing](zotero://open-pdf/library/items/EP5UUXW5?page=156)
