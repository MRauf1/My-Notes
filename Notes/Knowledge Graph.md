---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Knowledge Graph[^1]
> A [[Graph]] that encodes a set of facts about entities by defining typed relations between them. Formally, a directed heterogeneous [[Multigraph|multigraph]]:
> - **[[Directed Graph|directed]]**: relations have a direction (subject → object);
> - **heterogeneous**: nodes represent different types of entity (e.g. people, countries, companies);
> - **multigraph**: there can be multiple edges, of different types, between the same two nodes.

Each fact is commonly written as a triple $(h, r, t)$: head entity, relation type, tail entity.[^2]

# Properties
- A structured form of [[Knowledge Representation (Artificial Intelligence)|knowledge representation]].[^2]
- Edge prediction on a knowledge graph (*knowledge graph completion*) infers missing facts; a [[Graph Neural Network]] handles the multiple relation types with relation-specific weights (e.g. R-GCN), or with relation types as [[Line Graph|edge]] embeddings.[^2]

[^1]: [Prince, p. 241](zotero://open-pdf/library/items/BWT7FYX5?page=255&annotation=3QY5Y9QL)
[^2]: Added from general knowledge.
