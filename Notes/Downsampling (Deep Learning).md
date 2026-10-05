---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Downsampling (Deep Learning)[^1]
> Scaling down the spatial resolution of a hidden representation in a [[Convolutional Neural Network]], most commonly halving each spatial dimension of a 2D representation.

# Types
- **Subsampling**: keep every other position; a [[Stride (Convolution)|stride]]-two convolution applies this simultaneously with the convolution.[^2]
- [[Max Pooling]]
- [[Average Pooling]]

# Properties
- Applied separately to each channel, so the output has half the width and height but the same number of channels.[^3]
- Increases the [[Receptive Field]] of subsequent layers.[^1]
- Its counterpart, for when the output is also an image, is [[Upsampling (Deep Learning)]].

[^1]: [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=2BL7VV7Z); [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=GHDZ29PZ)
[^2]: [Prince, p. 172](zotero://open-pdf/library/items/BWT7FYX5?page=186&annotation=USAZEZPX)
[^3]: [Prince, p. 172](zotero://open-pdf/library/items/BWT7FYX5?page=186&annotation=YWT9TXL4)
