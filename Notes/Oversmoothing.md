---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Oversmoothing[^1]
> The degradation of a deep [[Graph Neural Network]] in which each layer incorporates information from a larger neighbourhood, until (important) local information dissolves and the node embeddings become nearly indistinguishable.

# Properties
- **Random-walk view** (Xu et al., 2018): the influence of one node on another after $K$ layers is proportional to the probability of reaching it in a $K$-step [[Random Walk]]. As $K$ grows this approaches the stationary distribution of the walk, which does not depend on the starting node, so the local neighbourhood is washed out.[^1]
- **Spectral view**: repeated application of a normalized propagation matrix such as $\mathbf{D}^{-1/2}(\mathbf{A}+\mathbf{I})\mathbf{D}^{-1/2}$ is a power iteration that kills every component except the top eigenvector, i.e. a repeated low-pass filter ([[Spectral Graph Convolution]]); on a connected graph the embeddings converge to a subspace carrying only degree information (Li, Han & Wu, 2018).[^2]
- One reason early GNNs used only two to five layers; mitigated by [[Residual Connection|residual]] and jumping-knowledge connections, which give access to earlier, more local representations.[^3]
- Distinct from [[Oversquashing]], which is about a bottleneck of too much information rather than too little distinction.

[^1]: [Prince, p. 265](zotero://open-pdf/library/items/BWT7FYX5?page=279&annotation=5ZVEBSWA); [Prince, p. 266](zotero://open-pdf/library/items/BWT7FYX5?page=280&annotation=X2CIB63G)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 266](zotero://open-pdf/library/items/BWT7FYX5?page=280&annotation=X2CIB63G); jumping knowledge added from general knowledge.
