---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Graph Laplacian Matrix[^1]
> For a [[Graph]] with [[Adjacency Matrix|adjacency matrix]] $\mathbf{A}$ and [[Degree Matrix|degree matrix]] $\mathbf{D}$, the (combinatorial) graph Laplacian is the $N \times N$ matrix
> $$
> \begin{align}
> \mathbf{L} = \mathbf{D} - \mathbf{A}.
> \end{align}
> $$

# Types
- **Symmetric normalized Laplacian**: $\mathbf{L}_{\mathrm{sym}} = \mathbf{D}^{-1/2}\mathbf{L}\mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$, with eigenvalues in $[0, 2]$.[^2]
- **Random-walk Laplacian**: $\mathbf{L}_{\mathrm{rw}} = \mathbf{D}^{-1}\mathbf{L} = \mathbf{I} - \mathbf{D}^{-1}\mathbf{A}$, where $\mathbf{D}^{-1}\mathbf{A}$ is the transition matrix of a [[Random Walk]] on the graph.[^2]

# Properties
- **Quadratic form**: for an [[Undirected Graph]], $\mathbf{x}^T\mathbf{L}\mathbf{x} = \sum_{(i,j) \in E}(x_i - x_j)^2$, which measures how much a node signal $\mathbf{x}$ varies across edges (the Dirichlet energy).[^2]
- Hence $\mathbf{L}$ is symmetric and [[Positive Semidefinite Matrix|positive semidefinite]], and by the [[Spectral Theorem]] has an orthonormal eigenbasis with real eigenvalues $0 = \lambda_1 \le \lambda_2 \le \dots \le \lambda_N$.[^2]
- $\mathbf{L}\mathbf{1} = \mathbf{0}$, and the multiplicity of the eigenvalue $0$ equals the number of [[Graph Connected Components|connected components]]; $\lambda_2 > 0$ (the Fiedler value, or algebraic connectivity) if and only if the graph is [[Connected Graph|connected]].[^2]
- Its eigenvectors form the graph Fourier basis used by [[Spectral Graph Convolution]].[^1]
- **Discrete analogue of the [[Laplacian Operator]]**: $(\mathbf{L}\mathbf{x})_i = \sum_{j \in \mathrm{ne}[i]}(x_i - x_j)$ is the negative of a finite-difference Laplacian; on a regular grid it reduces to the standard stencil. On triangle meshes the cotangent-weighted version is the geometry-processing Laplace–Beltrami operator.[^2]
- The Fiedler vector (eigenvector of $\lambda_2$) underlies spectral clustering and spectral [[Graph Partitioning]].[^2]

[^1]: [Prince, p. 262](zotero://open-pdf/library/items/BWT7FYX5?page=276&annotation=8WUSBTKD)
[^2]: Added from general knowledge.
