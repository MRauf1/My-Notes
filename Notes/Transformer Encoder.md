---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Transformer Encoder[^1]
> A [[Transformer]] whose layers use full (unmasked) [[Self-Attention|self-attention]], so every token attends to every other, transforming the text embeddings into a representation that supports a variety of downstream tasks. Example: BERT.

# Properties
- **Pre-training**: trained with [[Self-Supervised Learning|self-supervision]], which allows enormous amounts of unlabelled data. For BERT the task is predicting missing (masked) words in sentences from a large internet corpus.[^2]
- **Fine-tuning**: the parameters are then adjusted to specialize the network to a particular task, with an extra layer appended to convert the output vectors to the desired format ([[Transfer Learning]]).[^3]
- A special <cls> token, which represents no word, can be prepended; its output embedding summarizes the whole sequence and is mapped to class probabilities for sequence classification ([[Vision Transformer]]).
- Computation scales quadratically with sequence length ([[Sparse Attention]]).

[^1]: [Prince, p. 218](zotero://open-pdf/library/items/BWT7FYX5?page=232&annotation=NY3HXNU5)
[^2]: [Prince, p. 220](zotero://open-pdf/library/items/BWT7FYX5?page=234&annotation=BLT8K4BQ)
[^3]: [Prince, p. 221](zotero://open-pdf/library/items/BWT7FYX5?page=235&annotation=LLWRR3BW)
