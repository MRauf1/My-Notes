---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Neighborhood Sampling[^1]
> A remedy for the [[Graph Expansion Problem]] in which the graph feeding a batch of nodes is subsampled layer by layer: starting from the batch nodes, a fixed number of their neighbours is sampled randomly in the previous layer, then a fixed number of *their* neighbours in the layer before, and so on.

# Properties
- The graph still grows with each layer, but in a controlled way: with $S_k$ samples per node at layer $k$, a batch of $B$ nodes needs at most $B\prod_k S_k$ inputs, independent of the true degrees.[^1][^2]
- The sampling is redone for every batch, so the contributing neighbours differ even if the same batch is drawn twice; this is reminiscent of [[Dropout]] and adds some [[Regularization|regularization]].[^1]
- Introduced by GraphSAGE (Hamilton et al., 2017), which pairs it with [[Neighborhood Aggregation (Graph Neural Network)|mean, max-pooling, or LSTM aggregators]] to give an inductive model that generalizes to unseen nodes.[^2]
- Alternative: [[Graph Partitioning]].

[^1]: [Prince, p. 254](zotero://open-pdf/library/items/BWT7FYX5?page=268&annotation=JKN8P2BX)
[^2]: Added from general knowledge.
