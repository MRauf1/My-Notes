---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Cross-Attention (Encoder-Decoder Attention)[^1]
> [[Self-Attention]] in which the queries come from one sequence and the keys and values from another. In an [[Encoder-Decoder Transformer]], with decoder embeddings $\mathbf{X}_{dec} \in \mathbb{R}^{D \times N_d}$ and encoder embeddings $\mathbf{X}_{enc} \in \mathbb{R}^{D \times N_e}$:
> $$
> \begin{align}
> \mathbf{Q} = \boldsymbol{\beta}_q\mathbf{1}^T + \boldsymbol{\Omega}_q\mathbf{X}_{dec}, \quad
> \mathbf{K} = \boldsymbol{\beta}_k\mathbf{1}^T + \boldsymbol{\Omega}_k\mathbf{X}_{enc}, \quad
> \mathbf{V} = \boldsymbol{\beta}_v\mathbf{1}^T + \boldsymbol{\Omega}_v\mathbf{X}_{enc}, \qquad
> \mathbf{Ca}[\mathbf{X}_{dec}, \mathbf{X}_{enc}] = \mathbf{V} \cdot \mathbf{Softmax}\left[\mathbf{K}^T\mathbf{Q}\right]
> \end{align}
> $$
> The attention matrix is $N_e \times N_d$ and the output is $D \times N_d$, the same size as the decoder input.

![[Cross-Attention.png]]

# Properties
- Lets each decoder token draw on the whole encoded source. In translation, the encoder carries the source-language statistics and the decoder the target-language statistics.[^1]
- Inserted between the [[Masked Self-Attention|masked self-attention]] and the per-token fully connected network in each decoder [[Transformer Layer|layer]].[^2]
- The same mechanism conditions generative models on other modalities (e.g. text prompts in text-to-image diffusion models).[^3]

[^1]: [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=N8P64PDU)
[^2]: [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=RJDDZRND)
[^3]: Added from general knowledge.
