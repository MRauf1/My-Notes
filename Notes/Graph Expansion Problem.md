---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Graph Expansion Problem[^1]
> When training a $K$-layer [[Graph Neural Network]] on a single large graph with batches of nodes, each batch node depends on its $K$-hop neighbourhood (its [[Receptive Field|receptive field]]), so a gradient step needs the union of the $K$-hop neighbourhoods of the batch nodes. If there are many layers and the graph is densely connected, every input node may lie in the receptive field of every output, so batching does not reduce the graph size at all.

# Properties
- **Context**: training on one huge graph raises two problems: storing the node embeddings of every layer for the forward pass requires a structure several times the size of the whole graph, and with a single object it is not obvious how to form batches for [[Stochastic Gradient Descent]]. Batching random subsets of labelled nodes together with their $K$-hop neighbourhoods addresses both, until graph expansion sets in.[^2]
- The $K$-hop neighbourhood grows roughly like $d^K$ for average degree $d$, the same exponential growth behind [[Oversquashing]].[^3]
- **Remedies**: [[Neighborhood Sampling]] and [[Graph Partitioning]].[^1]

[^1]: [Prince, p. 254](zotero://open-pdf/library/items/BWT7FYX5?page=268&annotation=FJDECFJA); [Prince, p. 254](zotero://open-pdf/library/items/BWT7FYX5?page=268&annotation=JKSCRQ42)
[^2]: [Prince, p. 253](zotero://open-pdf/library/items/BWT7FYX5?page=267&annotation=UBHTYJ4V); [Prince, p. 253](zotero://open-pdf/library/items/BWT7FYX5?page=267&annotation=4TVT38UU)
[^3]: Added from general knowledge.
