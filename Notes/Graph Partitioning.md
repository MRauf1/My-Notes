---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Graph Partitioning[^1]
> Dividing the nodes of a [[Graph]] into disjoint subsets so that each subset induces a smaller [[Subgraph|subgraph]], chosen to maximize the number of edges internal to the subsets (equivalently, to minimize the number of edges cut between them), usually under a balance constraint on subset sizes.

# Properties
- **As a remedy for the [[Graph Expansion Problem]]**: the original graph is clustered into disjoint subgraphs before processing. Each subgraph can be treated as a batch, or a random subset of them can be combined into a batch, reinstating the edges between them from the original graph.[^1] This is the Cluster-GCN approach (Chiang et al., 2019).[^2]
- Balanced minimum-cut partitioning is NP-hard; standard algorithms are multilevel heuristics such as METIS (coarsen, partition, refine) and spectral partitioning using the Fiedler vector of the [[Graph Laplacian Matrix]].[^2]
- Alternative: [[Neighborhood Sampling]].

[^1]: [Prince, p. 254](zotero://open-pdf/library/items/BWT7FYX5?page=268&annotation=CXDHPFIQ)
[^2]: Added from general knowledge.
