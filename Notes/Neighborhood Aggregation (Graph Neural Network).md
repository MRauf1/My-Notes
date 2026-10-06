---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Neighborhood Aggregation[^1]
> The permutation-[[Invariant Function|invariant]] function $\mathrm{agg}[n]$ by which a [[Graph Neural Network]] layer combines the embeddings $\{\mathbf{h}_m\}_{m \in \mathrm{ne}[n]}$ of the neighbours of node $n$ into a single vector, which is then combined with the current node's embedding $\mathbf{h}_n$.

# Types
- **Sum**: $\mathrm{agg}[n] = \sum_{m \in \mathrm{ne}[n]} \mathbf{h}_m$; in matrix form $\mathbf{H}\mathbf{A}$. Used by the simple [[Graph Convolutional Network]].[^2]
- **Mean**: with the [[Degree Matrix|degree matrix]] $\mathbf{D}$, in matrix form $\mathbf{H}\mathbf{A}\mathbf{D}^{-1}$:[^3]
$$
\begin{align}
\mathrm{agg}[n] = \frac{1}{|\mathrm{ne}[n]|}\sum_{m \in \mathrm{ne}[n]} \mathbf{h}_m.
\end{align}
$$
  Sometimes the current node is included in the mean rather than treated separately.
- **Kipf normalization** (symmetric normalization): in matrix form $\mathbf{H}\mathbf{D}^{-1/2}\mathbf{A}\mathbf{D}^{-1/2}$:[^4]
$$
\begin{align}
\mathrm{agg}[n] = \sum_{m \in \mathrm{ne}[n]} \frac{\mathbf{h}_m}{\sqrt{|\mathrm{ne}[n]|\,|\mathrm{ne}[m]|}}.
\end{align}
$$
- **[[Max Pooling|Max pooling]]**: $\mathrm{agg}[n] = \max_{m \in \mathrm{ne}[n]}[\mathbf{h}_m]$, the element-wise maximum over neighbours.[^5]
- **Attention**: data-dependent weights, as in the [[Graph Attention Network]].

# Properties
- **Sum vs mean**: the magnitude of a mean aggregate does not depend on the number of neighbours, so the mean is preferable when the embedding information matters more than the structural information.[^3]
- **Kipf rationale**: messages from high-degree nodes are down-weighted, since they have many connections and provide less unique information.[^4] In Kipf & Welling (2017), self-loops are added before normalizing, giving $\tilde{\mathbf{D}}^{-1/2}(\mathbf{A}+\mathbf{I})\tilde{\mathbf{D}}^{-1/2}$ with $\tilde{\mathbf{D}}$ the degree matrix of $\mathbf{A}+\mathbf{I}$ (the "renormalization trick"), whose eigenvalues lie in $(-1, 1]$, keeping repeated application numerically stable.[^6]
- **Expressivity** (Xu et al., 2019): sum aggregation is injective on multisets of features, whereas mean only captures the distribution of neighbour features and max only their underlying set, so sum is strictly the most discriminative of the three.[^6]
- All of these are fixed (sum, mean, max) or topology-dependent (Kipf) weightings, in contrast to attention.

[^1]: [Prince, p. 257](zotero://open-pdf/library/items/BWT7FYX5?page=271&annotation=DRM6JAUC)
[^2]: [Prince, p. 250](zotero://open-pdf/library/items/BWT7FYX5?page=264&annotation=9UURFKWR); [Prince, p. 251](zotero://open-pdf/library/items/BWT7FYX5?page=265&annotation=W9WQYMGS)
[^3]: [Prince, p. 257](zotero://open-pdf/library/items/BWT7FYX5?page=271&annotation=DRM6JAUC); [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=NVM5BP7W)
[^4]: [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=IK2375ET)
[^5]: [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=7RF6CS87)
[^6]: Added from general knowledge.
