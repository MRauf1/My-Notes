---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Masked (Causal) Self-Attention[^1]
> [[Self-Attention]] in which each token may attend only to itself and previous tokens: the dot products $\mathbf{k}_m^T\mathbf{q}_n$ with $m > n$ are set to $-\infty$ before the softmax, so
> $$
> \begin{align}
> a[\mathbf{x}_m, \mathbf{x}_n] = 0 \quad \text{for all } m > n.
> \end{align}
> $$
> Equivalently, a mask $\mathbf{M}$ with $M_{mn} = 0$ for $m \le n$ and $-\infty$ otherwise is added to $\mathbf{K}^T\mathbf{Q}$ before the column-wise softmax.

# Properties
- **Purpose**: lets a [[Transformer Decoder|decoder]] compute every next-token log probability of a sequence in a single forward pass without "cheating". Without the mask, the term predicting token $n$ could see the answer and the context to its right. Since tokens interact only in the self-attention layers, masking them is enough to remove all access to future tokens.[^1]
- Each output embedding then depends only on the current and previous tokens, i.e. it represents a partial sentence.[^1]
- During generation, earlier embeddings never depend on later tokens, so their computation can be cached and reused as each new token is appended.[^2]
- The decoder's interaction matrix is lower triangular: about half the interactions of an encoder, but still quadratic in $N$ ([[Sparse Attention]]).[^3]

[^1]: [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=FWWCN2W4)
[^2]: [Prince, p. 224](zotero://open-pdf/library/items/BWT7FYX5?page=238&annotation=RA4LFNCM)
[^3]: [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=8DBPLMGU)
