---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Ghost Batch Normalization (GhostNorm)[^1]
> A variant of [[Batch Normalization]] in which the [[Mean|mean]] and standard deviation statistics are computed from a subset (a "ghost batch") of the batch rather than the whole batch (Hoffer et al., 2017).

![[Normalization Schemes.png]]

# Properties
- BatchNorm has a [[Regularization|regularizing]] effect due to statistical fluctuations from the random composition of the batch ([[Noise Injection (Regularization)|noise injection]]). Computing statistics over a smaller ghost batch keeps this noise, so large batches can be used without losing the regularization of small batches.[^1]

[^1]: [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=73GXCPY6); [Prince, p. 205](zotero://open-pdf/library/items/BWT7FYX5?page=219&annotation=RSGRVJ2B); [Prince, p. 204](zotero://open-pdf/library/items/BWT7FYX5?page=218&annotation=WQAIWEGA)
