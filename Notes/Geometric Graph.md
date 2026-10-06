---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Geometric Graph[^1]
> A [[Graph]] in which each node is associated with a position in space (e.g. $\mathbb{R}^3$). A point set (point cloud) becomes a geometric graph by connecting each point to its $K$ nearest neighbours.

# Properties
- The $K$-nearest-neighbour graph is generally [[Directed Graph|directed]] (being among $m$'s $K$ nearest neighbours is not symmetric) and is often symmetrized; the neighbourhood structure is the same one used by the [[K Nearest Neighbor Classifier]].[^2]
- Lets a [[Graph Neural Network]] perform node-level tasks such as part segmentation of a 3D shape, where each point is classified (e.g. wing vs fuselage of an airplane).[^3]
- Since positions live in space, a model should usually be [[Equivariant Function|equivariant]] or [[Invariant Function|invariant]] to rigid motions as well as to node permutations, motivating $E(3)$-equivariant GNNs; dynamic graph CNNs instead rebuild the $K$-NN graph in feature space at every layer.[^2]

[^1]: [Prince, p. 243](zotero://open-pdf/library/items/BWT7FYX5?page=257&annotation=9XRUL6N6)
[^2]: Added from general knowledge.
[^3]: [Prince, p. 248](zotero://open-pdf/library/items/BWT7FYX5?page=262&annotation=TDU9W9MB)
