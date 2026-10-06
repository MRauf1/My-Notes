---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Hierarchical Graph[^1]
> A [[Graph]] whose nodes are themselves graphs. For example, a table, a light, and a room may each be described by a graph of the adjacency of their components, and these three graphs are nodes in a higher-level graph representing the topology of the objects in a larger scene.

# Properties
- Mirrors a scene graph in computer graphics, where objects are composed hierarchically of parts.[^2]
- Can be processed by a [[Graph Neural Network]] that pools each lower-level graph (e.g. by [[Average Pooling|mean pooling]]) into an embedding for the corresponding higher-level node.[^2]

[^1]: [Prince, p. 243](zotero://open-pdf/library/items/BWT7FYX5?page=257&annotation=9XRUL6N6)
[^2]: Added from general knowledge.
