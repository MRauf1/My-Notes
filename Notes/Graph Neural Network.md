---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Graph Neural Network[^1]
> A model that takes the node embeddings $\mathbf{X} \in \mathbb{R}^{D \times N}$ and the [[Adjacency Matrix|adjacency matrix]] $\mathbf{A} \in \{0,1\}^{N \times N}$ of a [[Graph]] with $N$ nodes and passes them through $K$ layers $\mathbf{F}[\cdot]$ with parameters $\boldsymbol{\phi}_k$, updating the node embeddings at each layer:
> $$
> \begin{align}
> \mathbf{H}_1 &= \mathbf{F}[\mathbf{X}, \mathbf{A}, \boldsymbol{\phi}_0] \\
> \mathbf{H}_{k+1} &= \mathbf{F}[\mathbf{H}_k, \mathbf{A}, \boldsymbol{\phi}_k], \qquad k = 1, \dots, K-1
> \end{align}
> $$
> where the hidden representations $\mathbf{H}_k$ end in the output embeddings $\mathbf{H}_K$. Every layer must be [[Equivariant Function|equivariant]] to permutations of the node indices: for every [[Permutation Matrix|permutation matrix]] $\mathbf{P}$,
> $$
> \begin{align}
> \mathbf{H}_{k+1}\mathbf{P} = \mathbf{F}[\mathbf{H}_k\mathbf{P}, \mathbf{P}^T\mathbf{A}\mathbf{P}, \boldsymbol{\phi}_k].
> \end{align}
> $$

**Encoding a graph.** A graph with $N$ nodes and $E$ edges is encoded by three matrices:[^2]
- $\mathbf{A}$ ($N \times N$): the graph structure; for large sparse graphs, stored as a list of connections $(m, n)$ instead ([[Adjacency Lists]]).
- $\mathbf{X}$ ($D \times N$): column $n$ is the **node embedding** $\mathbf{x}^{(n)}$ of length $D$, the information attached to node $n$ (e.g. a user's interests in a social network).
- $\mathbf{E}$ ($D_E \times E$): column $e$ is the **edge embedding** $\mathbf{e}^{(e)}$ of length $D_E$, the information attached to edge $e$ (e.g. length, lanes, and speed limit of a road). Edge embeddings are processed via the [[Line Graph]].

**Why permutation equivariance.** Node indexing is arbitrary. Re-indexing with $\mathbf{P}$, where $P_{mn} = 1$ means node $m$ becomes node $n$, maps $\mathbf{X}' = \mathbf{X}\mathbf{P}$ (permute columns) and $\mathbf{A}' = \mathbf{P}^T\mathbf{A}\mathbf{P}$ (permute rows and columns), yet the underlying graph is unchanged. This is unlike images or text, where permuting pixels or words changes the content. Any processing must therefore not depend on the choice of indices.[^3]

**Contextual embeddings.** Each column of $\mathbf{X}$ describes only its own node; each column of $\mathbf{H}_K$ describes the node *in its context within the graph*, analogous to word embeddings passing through a [[Transformer]].[^4]

# Types
- [[Graph Convolutional Network]] (spatial-based)
- [[Spectral Graph Convolution]] (spectral-based)
- [[Graph Attention Network]]

# Properties
## Novel challenges of graphs[^5]
- **Variable topology**: hard to design networks that are both expressive enough and able to cope with the variation.
- **Size**: graphs may be enormous (a social network may have a billion nodes); see [[Graph Expansion Problem]].
- **A single monolithic graph**: the usual protocol of training on many examples and testing on new ones may not apply; see [[Transductive Learning]].

## Tasks and output heads
- **Graph-level tasks**: output embeddings are combined (e.g. [[Average Pooling|mean pooling]]) and mapped to a fixed-size vector, trained with [[Mean Squared Error|least squares]] for regression or with a [[Sigmoid Function|sigmoid]] and [[Binary Cross-Entropy Loss]] for binary classification. With scalar $\beta_K$ and $1 \times D$ vector $\boldsymbol{\omega}_K$,[^6]
$$
\begin{align}
Pr(y = 1 \mid \mathbf{X}, \mathbf{A}) = \mathrm{sig}\left[\beta_K + \boldsymbol{\omega}_K \mathbf{H}_K \mathbf{1}/N\right],
\end{align}
$$
  where post-multiplying by the vector of ones $\mathbf{1}$ sums the embeddings. Since $\mathbf{P}\mathbf{1} = \mathbf{1}$, this head is permutation [[Invariant Function|invariant]]: $\mathbf{H}_K\mathbf{P}\mathbf{1}/N = \mathbf{H}_K\mathbf{1}/N$.[^7]
- **Node-level tasks**: classification or regression at every node, with the same loss applied independently per node; the output must be permutation *equivariant*:[^8]
$$
\begin{align}
Pr(y^{(n)} = 1 \mid \mathbf{X}, \mathbf{A}) = \mathrm{sig}\left[\beta_K + \boldsymbol{\omega}_K \mathbf{h}_K^{(n)}\right].
\end{align}
$$
- **Edge prediction**: binary classification of whether an edge should exist between nodes $m$ and $n$. One option is the sigmoid of the [[Dot Product|dot product]] of the two output embeddings:[^9]
$$
\begin{align}
Pr(y^{(mn)} = 1 \mid \mathbf{X}, \mathbf{A}) = \mathrm{sig}\left[\mathbf{h}^{(m)T}\mathbf{h}^{(n)}\right].
\end{align}
$$

## Training
- **Batching in the inductive setting**: a batch of graphs is processed in parallel by treating them as disjoint [[Graph Connected Components|components]] of one large graph (a block-diagonal $\mathbf{A}$), running the network equations once, and mean pooling over each graph separately to get one representation per graph for the loss.[^10]
- **Single-graph (transductive) setting**: a batch is a random subset of labelled nodes together with their $K$-hop neighbourhoods; this runs into the [[Graph Expansion Problem]], tackled by [[Neighborhood Sampling]] and [[Graph Partitioning]].

## Depth
- Until recently GNNs did not benefit much from depth: the original GCN (Kipf & Welling, 2017) and GraphSAGE use two layers, and Cluster-GCN reached state-of-the-art on PPI with five.[^11] Explanations:
	- [[Oversmoothing]]: local information washes out as the neighbourhood grows.
	- [[Oversquashing]]: exponentially many neighbours are squashed into a fixed-size embedding.
	- **Suspended animation**: beyond a certain depth, gradients no longer propagate back and learning fails on both training and test data, like naively deepened [[Convolutional Neural Network|CNNs]]; [[Vanishing Gradients]] have also been identified as a limitation.[^12]
- Deeper GNNs are now trainable with various forms of [[Residual Connection|residual connections]]; a model with more than $1000$ layers has been trained using a reversible (invertible) network to cut the memory needed for training.[^12]

## Relation to other frameworks
- Most spatial GNNs fit the **message passing** framework (Gilmer et al., 2017): each node aggregates messages from its neighbours with a permutation-invariant function and then updates its own state.[^13]
- The expressive power of message-passing GNNs at distinguishing non-isomorphic graphs is bounded by the 1-dimensional Weisfeiler–Lehman test ([[Graph Isomorphism]]); sum aggregation with an injective update reaches this bound (GIN; Xu et al., 2019).[^13]
- A [[Transformer]] can be viewed as a GNN on a complete graph, with positional encodings supplying the structure.[^13]

[^1]: [Prince, p. 245](zotero://open-pdf/library/items/BWT7FYX5?page=259&annotation=CXP9J6CV); [Prince, p. 248](zotero://open-pdf/library/items/BWT7FYX5?page=262&annotation=9GILD2GJ); [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=FQRNJX4J)
[^2]: [Prince, p. 243](zotero://open-pdf/library/items/BWT7FYX5?page=257&annotation=VYAUTAPL); [Prince, p. 243](zotero://open-pdf/library/items/BWT7FYX5?page=257&annotation=BLFWJBFU); [Prince, p. 244](zotero://open-pdf/library/items/BWT7FYX5?page=258&annotation=5QY63N6U); [Prince, p. 244](zotero://open-pdf/library/items/BWT7FYX5?page=258&annotation=EVQ7QV4V)
[^3]: [Prince, p. 245](zotero://open-pdf/library/items/BWT7FYX5?page=259&annotation=L8K8A7FI); [Prince, p. 245](zotero://open-pdf/library/items/BWT7FYX5?page=259&annotation=HJBQDXZN)
[^4]: [Prince, p. 245](zotero://open-pdf/library/items/BWT7FYX5?page=259&annotation=AMVYH9VH)
[^5]: [Prince, p. 240](zotero://open-pdf/library/items/BWT7FYX5?page=254&annotation=QU6H6DWW)
[^6]: [Prince, p. 246](zotero://open-pdf/library/items/BWT7FYX5?page=260&annotation=RY8SLI5G)
[^7]: [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=PPRKSFIE)
[^8]: [Prince, p. 248](zotero://open-pdf/library/items/BWT7FYX5?page=262&annotation=TDU9W9MB); [Prince, p. 249](zotero://open-pdf/library/items/BWT7FYX5?page=263&annotation=PPRKSFIE)
[^9]: [Prince, p. 248](zotero://open-pdf/library/items/BWT7FYX5?page=262&annotation=ED2HHYZZ)
[^10]: [Prince, p. 252](zotero://open-pdf/library/items/BWT7FYX5?page=266&annotation=I7YU693C)
[^11]: [Prince, p. 265](zotero://open-pdf/library/items/BWT7FYX5?page=279&annotation=5ZVEBSWA)
[^12]: [Prince, p. 266](zotero://open-pdf/library/items/BWT7FYX5?page=280&annotation=X2CIB63G)
[^13]: Added from general knowledge.
