---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Teacher Forcing[^1]
> Training a sequence model by conditioning each prediction on the **ground-truth** previous tokens, rather than on the model's own previous outputs.

# Properties
- Allows all next-token predictions of a sequence to be trained in parallel ([[Masked Self-Attention]], [[Transformer Decoder]]).
- Causes a train/deployment mismatch (**exposure bias**): at deployment the model conditions on its own possibly erroneous outputs, which it never saw during training. This partly explains why naive [[Decoding (Language Model)|decoding]] works poorly.[^1]

[^1]: [Prince, p. 235](zotero://open-pdf/library/items/BWT7FYX5?page=249&annotation=XMQF7NH8)
