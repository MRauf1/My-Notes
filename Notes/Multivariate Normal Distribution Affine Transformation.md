---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!abstract] Theorem 1 (Affine Transformation)[^1]
> If $\mathbf{X} \sim N_n(\boldsymbol{\mu}, \Sigma)$, $A$ is an $m \times n$ matrix, and $\mathbf{b} \in \mathbb{R}^m$, then
> $$
> \begin{align}
> \mathbf{Y} = A\mathbf{X} + \mathbf{b} \sim N_m(A\boldsymbol{\mu} + \mathbf{b}, A\Sigma A^T)
> \end{align}
> $$

Proof: $M_{\mathbf{Y}}(\mathbf{t}) = e^{\mathbf{t}^T\mathbf{b}} M_{\mathbf{X}}(A^T\mathbf{t}) = \exp\{\mathbf{t}^T(A\boldsymbol{\mu} + \mathbf{b}) + \frac12\mathbf{t}^T A\Sigma A^T\mathbf{t}\}$, the [[Multivariate Normal Distribution|multivariate normal]] mgf. The mean and covariance agree with the general rules for a [[Covariance Matrix]]; what is special is that normality is preserved. No rank condition on $A$ is needed, since the mgf definition allows a singular $A\Sigma A^T$.

> [!abstract] Corollary 1 (Marginal Distributions)[^2]
> Partition $\mathbf{X} = \begin{bmatrix}\mathbf{X}_1 \\ \mathbf{X}_2\end{bmatrix}$ with $\mathbf{X}_1$ of dimension $m$, and correspondingly $\boldsymbol{\mu} = \begin{bmatrix}\boldsymbol{\mu}_1 \\ \boldsymbol{\mu}_2\end{bmatrix}$ and $\Sigma = \begin{bmatrix}\Sigma_{11} & \Sigma_{12} \\ \Sigma_{21} & \Sigma_{22}\end{bmatrix}$. Then $\mathbf{X}_1 \sim N_m(\boldsymbol{\mu}_1, \Sigma_{11})$.

Take $A = [I_m \;\; O_{mp}]$. Any subvector (after reordering) is normal, with the mean and covariance of that subvector: the [[Marginal Distribution|marginals]] are read off by deleting rows and columns.

# Properties
- Every linear combination $\mathbf{a}^T\mathbf{X} \sim N(\mathbf{a}^T\boldsymbol{\mu}, \mathbf{a}^T\Sigma\mathbf{a})$; conversely, $\mathbf{X}$ is multivariate normal iff every linear combination is univariate normal (Cramér-Wold).
- Generalizes [[Normal Distribution Linear Combination]] to dependent components.
- Marginal normality does not imply joint normality: the converse of Corollary 1 fails.

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=218)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=219)
