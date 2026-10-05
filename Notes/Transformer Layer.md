---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Transformer Layer[^1]
> A layer mapping a $D \times N$ matrix $\mathbf{X}$ of token embeddings to a matrix of the same size, made of a [[Multi-Head Self-Attention|multi-head self-attention]] unit (where the tokens interact) followed by a fully connected network $\mathrm{mlp}[\cdot]$ applied separately to each token. Both are [[Residual Connection|residual]] blocks, each followed by [[Layer Normalization|LayerNorm]]:
> $$
> \begin{align}
> \mathbf{X} &\leftarrow \mathbf{X} + \mathbf{MhSa}[\mathbf{X}] \\
> \mathbf{X} &\leftarrow \mathbf{LayerNorm}[\mathbf{X}] \\
> \mathbf{x}_n &\leftarrow \mathbf{x}_n + \mathrm{mlp}[\mathbf{x}_n] \qquad \forall\, n \in \{1, \dots, N\} \\
> \mathbf{X} &\leftarrow \mathbf{LayerNorm}[\mathbf{X}]
> \end{align}
> $$
> where $\mathbf{x}_n$ are the columns of $\mathbf{X}$.

![[Transformer Layer.png]]

# Properties
- The same [[Multilayer Perceptron|MLP]] is shared by all $N$ tokens, so tokens interact only in the self-attention unit.[^1]
- LayerNorm normalizes each embedding separately using statistics over its $D$ dimensions, rather than over the batch as in [[Batch Normalization|BatchNorm]].[^1]
- **Post-LN vs. Pre-LN**: the layout above (normalization after the residual addition) is the original "Post-LN" layout. Placing the LayerNorm outside the residual path makes gradients shrink as they pass back through the network (Xiong et al., 2020), contributing to the need for [[Learning Rate Warm-Up]]. Most modern large transformers instead use "Pre-LN", normalizing the input of each residual branch: $\mathbf{X} \leftarrow \mathbf{X} + \mathbf{MhSa}[\mathbf{LayerNorm}[\mathbf{X}]]$.[^2]
- A stack of $K$ such layers forms a [[Transformer]].

[^1]: [Prince, p. 215](zotero://open-pdf/library/items/BWT7FYX5?page=229&annotation=8CZVQDHB); [Prince, p. 216](zotero://open-pdf/library/items/BWT7FYX5?page=230&annotation=6BNL3GQ9); [Prince, p. 216](zotero://open-pdf/library/items/BWT7FYX5?page=230&annotation=89AW73IT)
[^2]: [Prince, p. 237](zotero://open-pdf/library/items/BWT7FYX5?page=251&annotation=X6CE7KIZ); Pre-LN convention added from general knowledge.
