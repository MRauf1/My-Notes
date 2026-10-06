---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Line Graph (Edge Graph, Adjoint Graph)[^1]
> The line graph $L(G)$ of a [[Graph]] $G$ has one node for each [[Edge|edge]] of $G$, and two of its nodes are adjacent if and only if the corresponding edges of $G$ share a common [[Vertex|vertex]].

# Properties
- **Recoverability** (Whitney's theorem, 1932): two connected graphs with isomorphic line graphs are themselves isomorphic, with the single exception of the triangle $K_3$ and the star $K_{1,3}$, which both have $K_3$ as line graph. So a graph can generally be recovered from its line graph and the two representations can be swapped.[^2]
- **Processing edge embeddings in a [[Graph Neural Network]]**: the graph is translated to its line graph, whose node embeddings are the original edge embeddings, and the usual node-aggregation machinery is applied. With both node and edge embeddings, translating back and forth gives four updates (nodes→nodes, nodes→edges, edges→nodes, edges→edges), which can be alternated or, with minor modifications, applied simultaneously.[^3]
- A vertex of degree $d$ in $G$ creates a clique of $\binom{d}{2}$ edges in $L(G)$, so line graphs of graphs with high-degree vertices are much denser.[^2]

[^1]: [Prince, p. 260](zotero://open-pdf/library/items/BWT7FYX5?page=274&annotation=NWNVLSIR)
[^2]: Added from general knowledge (Whitney, 1932, refines Prince's "in general").
[^3]: [Prince, p. 260](zotero://open-pdf/library/items/BWT7FYX5?page=274&annotation=7RDV4PXK); [Prince, p. 261](zotero://open-pdf/library/items/BWT7FYX5?page=275&annotation=7DKYEJ3V)
