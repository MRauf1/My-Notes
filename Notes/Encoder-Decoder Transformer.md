---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Encoder-Decoder Transformer[^1]
> A [[Transformer]] for sequence-to-sequence tasks (e.g. machine translation) that combines a [[Transformer Encoder|encoder]], which computes a representation of the source sequence, with a [[Transformer Decoder|decoder]], which generates the target sequence. Each decoder layer consists of [[Masked Self-Attention|masked self-attention]], then [[Cross-Attention|cross-attention]] to the encoder outputs, then a per-token fully connected network.

# Properties
- Each output token is conditioned on both the previous output tokens and the entire source sequence:[^2]
  $$
  \begin{align}
  Pr(\mathbf{y}) = \prod_{n} Pr(y_n \mid y_1, \dots, y_{n-1}, \mathbf{x}_{\text{source}})
  \end{align}
  $$
- During training the decoder receives the ground-truth target sequence and predicts the following token at every position ([[Teacher Forcing]]).[^2]

[^1]: [Prince, p. 226](zotero://open-pdf/library/items/BWT7FYX5?page=240&annotation=G82WA6K9); [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=RJDDZRND)
[^2]: [Prince, p. 226](zotero://open-pdf/library/items/BWT7FYX5?page=240&annotation=ZUFHRNA9); [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=2E7M2KDU)
