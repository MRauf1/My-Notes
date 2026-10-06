---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Graph Attention Layer[^1]
> A [[Graph Neural Network]] layer whose neighbour weights depend on the data at the nodes. The node embeddings are linearly transformed,
> $$
> \begin{align}
> \mathbf{H}'_k = \boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{H}_k,
> \end{align}
> $$
> the similarity of each pair of transformed embeddings is computed with a learned vector $\boldsymbol{\phi}_k$ and an activation $\mathrm{a}[\cdot]$, and stored in the $N \times N$ matrix $\mathbf{S}$,
> $$
> \begin{align}
> s_{mn} = \mathrm{a}\left[\boldsymbol{\phi}_k^T \begin{bmatrix}\mathbf{h}'_m \\ \mathbf{h}'_n\end{bmatrix}\right],
> \end{align}
> $$
> and the output is
> $$
> \begin{align}
> \mathbf{H}_{k+1} = \mathrm{a}\left[\mathbf{H}'_k \cdot \mathbf{Softmask}[\mathbf{S}, \mathbf{A} + \mathbf{I}]\right],
> \end{align}
> $$
> where $\mathbf{Softmask}[\mathbf{S}, \mathbf{M}]$ sets the entries of $\mathbf{S}$ where $\mathbf{M}$ is zero to $-\infty$ and then applies the [[Softmax Function|softmax]] to each column, so each node attends only to itself and its neighbours, with weights that are positive and sum to one.

![[Graph Attention Network.png]]

# Properties
- **Contrast with other aggregations**: sum, mean, and max [[Neighborhood Aggregation (Graph Neural Network)|aggregation]] weight neighbours equally, and Kipf normalization weights them by the graph topology; attention weights them by the node data.[^2]
- **Relation to [[Self-Attention|dot-product self-attention]]**: very similar, except that (i) keys, queries, and values are all the same, $\mathbf{H}'_k$; (ii) the similarity measure is a learned linear function of the concatenated pair rather than a dot product; and (iii) the attention is masked by $\mathbf{A} + \mathbf{I}$, comparable to how [[Masked Self-Attention]] masks future tokens.[^1]
- Like transformers, it extends to [[Multi-Head Self-Attention|multiple heads]] run in parallel and recombined.[^1]
- Permutation [[Equivariant Function|equivariant]], since $\mathbf{S}$ and the mask $\mathbf{A} + \mathbf{I}$ are permuted consistently.
- In the original GAT (Veličković et al., 2018), $\mathrm{a}$ in $s_{mn}$ is a [[Leaky ReLU]].[^3]
- **Static attention** (Brody, Alon & Yahav, 2022): since $s_{mn} = \mathrm{a}[\boldsymbol{\phi}_1^T\mathbf{h}'_m + \boldsymbol{\phi}_2^T\mathbf{h}'_n]$ with monotonic $\mathrm{a}$, the ranking of neighbours $m$ is the same for every query node $n$. GATv2 fixes this by applying the nonlinearity before the dot product with $\boldsymbol{\phi}$, i.e. $s_{mn} = \boldsymbol{\phi}^T \mathrm{a}[\boldsymbol{\Omega}[\mathbf{h}_m; \mathbf{h}_n]]$, giving *dynamic* attention.[^3]

[^1]: [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=GYHYAJP9); [Prince, p. 259](zotero://open-pdf/library/items/BWT7FYX5?page=273&annotation=8CLJPIPA); [Prince, p. 260](zotero://open-pdf/library/items/BWT7FYX5?page=274&annotation=FBDFJ2X9)
[^2]: [Prince, p. 258](zotero://open-pdf/library/items/BWT7FYX5?page=272&annotation=GYHYAJP9)
[^3]: Added from general knowledge.
