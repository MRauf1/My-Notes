---
tags:
  - statistics
  - mathematical_statistics
---

# Definition
> [!info] Principal Components[^1]
> Let $\mathbf{X} \sim N_n(\boldsymbol{\mu}, \Sigma)$ with $\Sigma$ positive definite and spectral decomposition $\Sigma = V\Lambda V^T$, where the columns $\mathbf{v}_1, \dots, \mathbf{v}_n$ of the [[Orthogonal Matrix|orthogonal]] $V$ are [[Eigenvector|eigenvectors]] with eigenvalues $\lambda_1 \geq \dots \geq \lambda_n > 0$. The vector of principal components is
> $$
> \begin{align}
> \mathbf{Y} = V^T(\mathbf{X} - \boldsymbol{\mu}) \sim N_n(\mathbf{0}, \Lambda)
> \end{align}
> $$
> so $Y_1, \dots, Y_n$ are independent with $Y_i = \mathbf{v}_i^T(\mathbf{X} - \boldsymbol{\mu}) \sim N(0, \lambda_i)$. $Y_i$ is the $i$th principal component.

(Hogg et al. write $\Sigma = \Gamma^T\Lambda\Gamma$ and $\mathbf{Y} = \Gamma(\mathbf{X} - \boldsymbol{\mu})$, with $\Gamma = V^T$.) The distribution of $\mathbf{Y}$ follows from the [[Multivariate Normal Distribution Affine Transformation]], since $V^T\Sigma V = \Lambda$, and independence from the [[Multivariate Normal Distribution Independence|diagonal covariance]]. Geometrically, $\mathbf{Y}$ expresses $\mathbf{X} - \boldsymbol{\mu}$ in the orthonormal basis of the principal axes of the density's ellipsoidal contours.

> [!abstract] Theorem 1 (Total Variation Is Preserved)[^1]
> The total variation $TV(\mathbf{X}) = \sum_i \text{Var}(X_i)$ satisfies
> $$
> \begin{align}
> TV(\mathbf{X}) = \text{tr}\,\Sigma = \text{tr}\,V\Lambda V^T = \text{tr}\,\Lambda V^T V = \sum_{i=1}^n \lambda_i = TV(\mathbf{Y})
> \end{align}
> $$

> [!abstract] Theorem 2 (Variance Maximization)[^2]
> $Y_1$ has the maximum variance among all unit-norm linear combinations: for every $\mathbf{a}$ with $\lVert\mathbf{a}\rVert = 1$,
> $$
> \begin{align}
> \text{Var}(\mathbf{a}^T\mathbf{X}) = \mathbf{a}^T\Sigma\mathbf{a} = \sum_{i=1}^n \lambda_i(\mathbf{a}^T\mathbf{v}_i)^2 \leq \lambda_1 = \text{Var}(Y_1)
> \end{align}
> $$
> More generally, for $j = 2, \dots, n$, $\text{Var}(\mathbf{a}^T\mathbf{X}) \leq \lambda_j = \text{Var}(Y_j)$ for all unit $\mathbf{a}$ orthogonal to $\mathbf{v}_1, \dots, \mathbf{v}_{j-1}$.

Expanding $\mathbf{a} = \sum_j a_j\mathbf{v}_j$ in the orthonormal eigenbasis gives $\mathbf{a}^T\mathbf{v}_i = a_i$ and $\sum_i a_i^2 = 1$, so $\mathbf{a}^T\Sigma\mathbf{a} = \sum_i \lambda_i a_i^2$ is a weighted average of the eigenvalues, maximized by putting all weight on $\lambda_1$ (the Rayleigh quotient).

# Properties
- The fraction $\lambda_i / \sum_j \lambda_j$ is the share of total variation carried by the $i$th component; keeping the first $k$ components gives the best $k$-dimensional linear approximation in mean squared error, which is the basis of dimensionality reduction.
- Decorrelation (diagonal $\Lambda$) holds for any distribution with covariance $\Sigma$; independence of the components requires normality.
- In practice $\Sigma$ is replaced by the sample covariance matrix, and the eigenvectors are computed from the [[Eigendecomposition]] (or the SVD of the centered data matrix).
- Dividing each component by $\sqrt{\lambda_i}$ gives $\Lambda^{-1/2}V^T(\mathbf{X} - \boldsymbol{\mu}) \sim N_n(\mathbf{0}, I)$, a whitening transform ([[Matrix Square Root]]).

[^1]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=222)
[^2]: [Introduction to Mathematical Statistics](zotero://open-pdf/library/items/P3TUBR4A?page=223)
