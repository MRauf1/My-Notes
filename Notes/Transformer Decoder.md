---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Transformer Decoder[^1]
> A [[Transformer]] implementing an [[Autoregressive Language Model|autoregressive language model]]: input text is tokenized and embedded, passed through transformer layers that use [[Masked Self-Attention|masked self-attention]] (each token attends only to itself and previous tokens), and a single [[Linear Layer|linear layer]] followed by a [[Softmax Function|softmax]] maps each output embedding to a distribution over the vocabulary for the next token. Example: GPT3.

# Properties
- **Training**: maximize the sum over all positions of the log probability of the next ground-truth token, i.e. a multiclass [[Cross-Entropy Loss|cross-entropy loss]]. The masking lets all positions be trained in one forward pass, each output embedding representing a partial sentence.[^1]
- **Generation**: start from an input sequence (possibly just a <start> token), compute the next-token distribution, choose or sample a token, append it, and repeat ([[Decoding (Language Model)]]). Since earlier embeddings do not depend on later tokens, earlier computation can be reused as the sequence grows.[^2]
- Trained with ground-truth prefixes ([[Teacher Forcing]]) but fed its own outputs at deployment.
- Each token interacts only with previous ones: about half the interactions of an encoder, but still quadratic in sequence length.[^3]

[^1]: [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=FWWCN2W4)
[^2]: [Prince, p. 223](zotero://open-pdf/library/items/BWT7FYX5?page=237&annotation=5BVXXUTC); [Prince, p. 224](zotero://open-pdf/library/items/BWT7FYX5?page=238&annotation=RA4LFNCM)
[^3]: [Prince, p. 227](zotero://open-pdf/library/items/BWT7FYX5?page=241&annotation=8DBPLMGU)
