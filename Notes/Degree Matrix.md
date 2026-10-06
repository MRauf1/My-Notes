---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Degree Matrix[^1]
> For a [[Graph]] with $N$ nodes, the $N \times N$ [[Diagonal Matrix|diagonal matrix]] $\mathbf{D}$ whose $n$th diagonal entry is the [[Degree of Vertex|degree]] (number of neighbours) of node $n$:
> $$
> \begin{align}
> D_{nn} = |\mathrm{ne}[n]| = \sum_{m} A_{mn}.
> \end{align}
> $$

# Properties
- $\mathbf{D} = \mathrm{diag}(\mathbf{A}\mathbf{1})$ for a symmetric [[Adjacency Matrix|adjacency matrix]] $\mathbf{A}$.[^2]
- The diagonal of $\mathbf{D}^{-1}$ holds the denominators that turn sums over neighbours into means: $\mathbf{H}\mathbf{A}\mathbf{D}^{-1}$ averages the neighbouring columns of $\mathbf{H}$ ([[Neighborhood Aggregation (Graph Neural Network)]]).[^1]
- $\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$ gives Kipf (symmetric) normalization.[^3]
- Defines the [[Graph Laplacian Matrix]] $\mathbf{L} = \mathbf{D} - \mathbf{A}$.[^4]

[^1]: [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=NVM5BP7W)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=IK2375ET)
[^4]: [Prince, p. 262](zotero://open-pdf/library/items/BWT7FYX5?page=276&annotation=8WUSBTKD)
