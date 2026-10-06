---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Oversquashing[^1]
> The bottleneck in a deep [[Graph Neural Network]] whereby, because the number of nodes in a $K$-hop neighbourhood grows exponentially with $K$, too much information from long paths is "squashed" into fixed-size node embeddings, so deeper networks fail to make use of long-range interactions (Alon & Yahav, 2021).

# Properties
- Explains why adding depth, which in principle lets information be aggregated from longer paths, often does not improve performance.[^1]
- Formalized via the sensitivity $\left\|\partial \mathbf{h}_K^{(n)} / \partial \mathbf{x}^{(m)}\right\|$, which is bounded by powers of the normalized adjacency matrix and decays across structural bottlenecks; edges with negative (Ricci) curvature cause it, and rewiring the graph to add shortcut edges alleviates it (Topping et al., 2022).[^2]
- Alon & Yahav found that making the last layer fully adjacent (every pair of nodes connected) helps, which also motivates graph transformers that attend over all nodes.[^2]
- Contrast with [[Oversmoothing]].

[^1]: [Prince, p. 266](zotero://open-pdf/library/items/BWT7FYX5?page=280&annotation=X2CIB63G)
[^2]: Added from general knowledge.
