---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Dot-Product Self-Attention[^1]
> A block $\mathrm{sa}[\cdot]$ that maps $N$ inputs $\mathbf{x}_1, \dots, \mathbf{x}_N \in \mathbb{R}^{D}$ to $N$ outputs of the same size. Each input is linearly transformed into a **value**, **query**, and **key**, using parameters shared across all positions:
> $$
> \begin{align}
> \mathbf{v}_m = \boldsymbol{\beta}_v + \boldsymbol{\Omega}_v \mathbf{x}_m, \qquad \mathbf{q}_n = \boldsymbol{\beta}_q + \boldsymbol{\Omega}_q \mathbf{x}_n, \qquad \mathbf{k}_m = \boldsymbol{\beta}_k + \boldsymbol{\Omega}_k \mathbf{x}_m
> \end{align}
> $$
> The $n$th output is a weighted sum of all the values,
> $$
> \begin{align}
> \mathrm{sa}_n[\mathbf{x}_1, \dots, \mathbf{x}_N] = \sum_{m=1}^{N} a[\mathbf{x}_m, \mathbf{x}_n]\, \mathbf{v}_m,
> \qquad
> a[\mathbf{x}_m, \mathbf{x}_n] = \mathrm{softmax}_m\left[\mathbf{k}_\bullet^T \mathbf{q}_n\right] = \frac{\exp\left[\mathbf{k}_m^T \mathbf{q}_n\right]}{\sum_{m'=1}^{N} \exp\left[\mathbf{k}_{m'}^T \mathbf{q}_n\right]}
> \end{align}
> $$
> where the **attention** $a[\mathbf{x}_m, \mathbf{x}_n]$ is the weight the $n$th output pays to input $\mathbf{x}_m$. For each $n$ the weights $a[\bullet, \mathbf{x}_n]$ are positive and sum to one.
>
> **Matrix form.** Storing the inputs as the columns of $\mathbf{X} \in \mathbb{R}^{D \times N}$ and with $\mathbf{1} \in \mathbb{R}^{N}$ a vector of ones,
> $$
> \begin{align}
> \mathbf{V} = \boldsymbol{\beta}_v \mathbf{1}^T + \boldsymbol{\Omega}_v \mathbf{X}, \quad \mathbf{Q} = \boldsymbol{\beta}_q \mathbf{1}^T + \boldsymbol{\Omega}_q \mathbf{X}, \quad \mathbf{K} = \boldsymbol{\beta}_k \mathbf{1}^T + \boldsymbol{\Omega}_k \mathbf{X}, \qquad
> \mathbf{Sa}[\mathbf{X}] = \mathbf{V} \cdot \mathbf{Softmax}\left[\mathbf{K}^T \mathbf{Q}\right]
> \end{align}
> $$
> where $\mathbf{Softmax}[\cdot]$ applies the [[Softmax Function|softmax]] independently to each column of the $N \times N$ matrix $\mathbf{K}^T\mathbf{Q}$.

Self-attention can be read as **routing** the values in different proportions to each output. The names "query" and "key" come from information retrieval: the [[Dot Product|dot product]] $\mathbf{k}_m^T\mathbf{q}_n$ measures the similarity of the $n$th query to each key, and the softmax makes the keys "compete" to contribute to the $n$th output.[^2]

**Are the value weights shared across inputs?** Yes. The same $\boldsymbol{\Omega}_v \in \mathbb{R}^{D \times D}$ and $\boldsymbol{\beta}_v \in \mathbb{R}^{D}$ are applied to every input $\mathbf{x}_\bullet$ (likewise for queries and keys), exactly as a [[Convolutional Layer|convolutional layer]] applies the same kernel at every image position. Viewed as one linear map from all $DN$ inputs to all $DN$ values, the value computation is a block-diagonal [[Sparse Matrix|sparse matrix]] with the same $D\times D$ block repeated $N$ times.[^3]

![[Self-Attention Values and Attention Weights.png]]

![[Self-Attention Queries and Keys.png]]

![[Self-Attention Matrix Form.png]]

# Types
- [[Scaled Dot-Product Self-Attention]]
- [[Multi-Head Self-Attention]]
- [[Masked Self-Attention]]
- [[Cross-Attention]]
- [[Sparse Attention]]
- [[Graph Attention Network]] (attention masked to graph neighbours)

# Properties
- **Motivation from text**: encoded text is large (e.g. $37$ words $\times$ $1024$-dimensional [[Word Embedding|embeddings]] $= 37888$ inputs) and of varying length, so a [[Linear Layer|fully connected]] network is impractical; the network should instead (i) share parameters across positions and (ii) contain connections between words whose strength depends on the words themselves and that extend over long spans. Self-attention satisfies both.[^4]
- **Parameters independent of $N$**: the single shared parameter set $\boldsymbol{\phi} = \{\boldsymbol{\beta}_v, \boldsymbol{\Omega}_v, \boldsymbol{\beta}_q, \boldsymbol{\Omega}_q, \boldsymbol{\beta}_k, \boldsymbol{\Omega}_k\}$ does not depend on the number of inputs, so the block applies to sequences of any length.[^5]
- **Quadratic attention weights**: there is one attention weight per ordered pair $(\mathbf{x}_m, \mathbf{x}_n)$, so the number of attention weights is $N^2$, independent of $D$; the attention matrix relating values to outputs is also sparse (each weight multiplies an identity block).[^6]
- **Nonlinear without an activation function**: the output comes from two chained linear operations (values, then a linear combination by the attentions), but the attentions are themselves nonlinear functions of the input through the dot product and softmax. One branch computes the weights of another, so self-attention is an instance of a [[Hypernetwork]]. It can also be seen as a kind of triple product of the input with itself.[^7]
- **Dimensions**: queries and keys must have the same dimension $D_q$, which may differ from that of the values; the values are usually the same size as the input so the representation does not change size.[^8]
- **Permutation [[Equivariant Function|equivariance]]**: permuting the inputs permutes the outputs in the same way, i.e. $\mathbf{Sa}[\mathbf{X}\mathbf{P}] = \mathbf{Sa}[\mathbf{X}]\mathbf{P}$ for any [[Permutation Matrix|permutation matrix]] $\mathbf{P}$, so word order is ignored; this is fixed by a [[Positional Encoding]].[^9]
- Large dot products saturate the softmax and give tiny gradients, which motivates [[Scaled Dot-Product Self-Attention]].
- The core building block of the [[Transformer Layer]].

[^1]: [Prince, p. 208](zotero://open-pdf/library/items/BWT7FYX5?page=222&annotation=XMS46XET); [Prince, p. 208](zotero://open-pdf/library/items/BWT7FYX5?page=222&annotation=2SG7KM2Z); [Prince, p. 210](zotero://open-pdf/library/items/BWT7FYX5?page=224&annotation=MHKTK5DE); [Prince, p. 212](zotero://open-pdf/library/items/BWT7FYX5?page=226&annotation=G9WD3C93); [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=SE4ZJEIL); [Prince, p. 212](zotero://open-pdf/library/items/BWT7FYX5?page=226&annotation=Y9LWTK96)
[^2]: [Prince, p. 210](zotero://open-pdf/library/items/BWT7FYX5?page=224&annotation=GBYNFT7Z); [Prince, p. 211](zotero://open-pdf/library/items/BWT7FYX5?page=225&annotation=YGVC947M); [Prince, p. 211](zotero://open-pdf/library/items/BWT7FYX5?page=225&annotation=3DFRH576)
[^3]: [Prince, p. 209](zotero://open-pdf/library/items/BWT7FYX5?page=223&annotation=22K9V7G9); [Prince, p. 210](zotero://open-pdf/library/items/BWT7FYX5?page=224&annotation=KHPU72U8)
[^4]: [Prince, p. 207](zotero://open-pdf/library/items/BWT7FYX5?page=221&annotation=9NUT5KDE); [Prince, p. 208](zotero://open-pdf/library/items/BWT7FYX5?page=222&annotation=D7SSHNJ3); [Prince, p. 208](zotero://open-pdf/library/items/BWT7FYX5?page=222&annotation=SQTARDMN)
[^5]: [Prince, p. 211](zotero://open-pdf/library/items/BWT7FYX5?page=225&annotation=LUJE95J2); [Prince, p. 212](zotero://open-pdf/library/items/BWT7FYX5?page=226&annotation=VUWRQH95)
[^6]: [Prince, p. 209](zotero://open-pdf/library/items/BWT7FYX5?page=223&annotation=3JCS74II)
[^7]: [Prince, p. 209](zotero://open-pdf/library/items/BWT7FYX5?page=223&annotation=BCCM9EHH); [Prince, p. 211](zotero://open-pdf/library/items/BWT7FYX5?page=225&annotation=YGVC947M)
[^8]: [Prince, p. 210](zotero://open-pdf/library/items/BWT7FYX5?page=224&annotation=GBYNFT7Z); [Prince, p. 211](zotero://open-pdf/library/items/BWT7FYX5?page=225&annotation=VRV8BQNZ)
[^9]: [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=QUSJZKJ7); [Prince, p. 213](zotero://open-pdf/library/items/BWT7FYX5?page=227&annotation=LS2XE8XW)
