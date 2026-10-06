---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] (Spatial-Based) Graph Convolutional Network[^1]
> A [[Graph Neural Network]] whose layers update each node by aggregating the embeddings of its neighbours $\mathrm{ne}[n]$ in the original graph. The simple GCN layer sums the neighbours,
> $$
> \begin{align}
> \mathrm{agg}[n, k] = \sum_{m \in \mathrm{ne}[n]} \mathbf{h}_k^{(m)},
> \end{align}
> $$
> applies the same linear transform $\boldsymbol{\Omega}_k$ to the current node and to the aggregate, adds a bias $\boldsymbol{\beta}_k$, and applies a pointwise [[Activation Layer|activation]] $\mathrm{a}[\cdot]$:
> $$
> \begin{align}
> \mathbf{h}_{k+1}^{(n)} = \mathrm{a}\left[\boldsymbol{\beta}_k + \boldsymbol{\Omega}_k \mathbf{h}_k^{(n)} + \boldsymbol{\Omega}_k\, \mathrm{agg}[n, k]\right].
> \end{align}
> $$
> Since column $n$ of $\mathbf{A}$ has ones exactly at the neighbours of $n$, column $n$ of $\mathbf{H}_k\mathbf{A}$ is $\mathrm{agg}[n,k]$, so in matrix form ($\mathbf{1} \in \mathbb{R}^N$ a vector of ones)
> $$
> \begin{align}
> \mathbf{H}_{k+1} = \mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k + \boldsymbol{\Omega}_k\mathbf{H}_k\mathbf{A}\right] = \mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k(\mathbf{A} + \mathbf{I})\right].
> \end{align}
> $$

**Naming.** *Convolutional* because each node is updated from nearby nodes; *spatial-based* because it uses the original graph structure, in contrast to [[Spectral Graph Convolution|spectral-based]] methods, which convolve in the graph Fourier domain.[^1]

# Types
Variants differ in how they combine the current node with its neighbours, and in the [[Neighborhood Aggregation (Graph Neural Network)|aggregation function]]:[^2]
- **Diagonal enhancement**: the current node is weighted by $(1+\varepsilon_k)$, a learned scalar per layer (this is the GIN layer of Xu et al., 2019):
$$
\begin{align}
\mathbf{H}_{k+1} = \mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k(\mathbf{A} + (1+\varepsilon_k)\mathbf{I})\right].
\end{align}
$$
- **Separate transform for the current node** $\boldsymbol{\Psi}_k$, equivalently one transform $\boldsymbol{\Omega}'_k = [\boldsymbol{\Omega}_k \; \boldsymbol{\Psi}_k]$ applied to the stacked matrix:
$$
\begin{align}
\mathbf{H}_{k+1} = \mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k\mathbf{A} + \boldsymbol{\Psi}_k\mathbf{H}_k\right] = \mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}'_k \begin{bmatrix}\mathbf{H}_k\mathbf{A} \\ \mathbf{H}_k\end{bmatrix}\right].
\end{align}
$$
- **[[Residual Connection|Residual]]**: the aggregated neighbours are transformed and activated *before* being summed or concatenated with the current node; for concatenation,
$$
\begin{align}
\mathbf{H}_{k+1} = \begin{bmatrix}\mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k\mathbf{A}\right] \\ \mathbf{H}_k\end{bmatrix}.
\end{align}
$$
- **Mean aggregation**: $\mathbf{H}_{k+1} = \mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k(\mathbf{A}\mathbf{D}^{-1} + \mathbf{I})\right]$ with [[Degree Matrix|degree matrix]] $\mathbf{D}$.
- **Kipf normalization**: $\mathbf{H}_{k+1} = \mathrm{a}\left[\boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k(\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2} + \mathbf{I})\right]$.
- [[Graph Attention Network]]: data-dependent neighbour weights.

# Properties
- **Design criteria satisfied**: the simple layer is permutation [[Equivariant Function|equivariant]] (since $\mathbf{H}\mathbf{P}(\mathbf{P}^T\mathbf{A}\mathbf{P} + \mathbf{I}) = \mathbf{H}(\mathbf{A}+\mathbf{I})\mathbf{P}$), copes with any number of neighbours, exploits the graph structure, and shares parameters across the graph.[^3]
- **Relational [[Inductive Bias|inductive bias]]**: a bias toward prioritizing information from neighbours.[^1]
- **Parameter sharing**: the same parameters are used at every node, reducing the parameter count and sharing what is learned at each node across the whole graph, as a [[Convolutional Layer|convolutional layer]] shares its kernel across image positions.[^4]
- **[[Receptive Field]]**: after $K$ layers a node's output depends on its $K$-hop neighbourhood, i.e. on nodes within [[Graph Distance|graph distance]] $K$, which is exactly the sparsity pattern of $(\mathbf{A} + \mathbf{I})^K$.[^5]
- The Kipf & Welling (2017) GCN arises as a first-order approximation of a [[Spectral Graph Convolution]], bridging spectral and spatial methods.
- Being spatial, GCNs transfer to unseen graphs, whereas spectral methods depend on a particular graph's Laplacian.[^6]
- Depth is limited by [[Oversmoothing]] and [[Oversquashing]].

[^1]: [Prince, p. 248](zotero://open-pdf/library/items/BWT7FYX5?page=262&annotation=V6VVW959); [Prince, p. 250](zotero://open-pdf/library/items/BWT7FYX5?page=264&annotation=9UURFKWR); [Prince, p. 251](zotero://open-pdf/library/items/BWT7FYX5?page=265&annotation=W9WQYMGS)
[^2]: [Prince, p. 257](zotero://open-pdf/library/items/BWT7FYX5?page=271&annotation=L3VWYQXE); [Prince, p. 257](zotero://open-pdf/library/items/BWT7FYX5?page=271&annotation=RPGSV7IR); [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=NVM5BP7W); [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=IK2375ET). GIN identification added from general knowledge.
[^3]: [Prince, p. 251](zotero://open-pdf/library/items/BWT7FYX5?page=265&annotation=W9WQYMGS)
[^4]: [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=K4ITAPU3)
[^5]: [Prince, p. 254](zotero://open-pdf/library/items/BWT7FYX5?page=268&annotation=FJDECFJA); matrix characterization added from general knowledge.
[^6]: [Prince, p. 262](zotero://open-pdf/library/items/BWT7FYX5?page=276&annotation=NF4XCUQI)
