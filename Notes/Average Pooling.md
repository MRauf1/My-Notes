---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Average Pooling[^1]
> A [[Downsampling (Deep Learning)|downsampling]] operation, also called **mean pooling**, that averages each block of input values (typically $2 \times 2$), separately for each channel.

# Properties
- Equivalent to a [[Stride (Convolution)|strided]] [[Convolutional Layer|convolution]] with a fixed uniform kernel applied per channel.[^2]
- Averaging over the entire spatial extent (global average pooling) yields a translation-[[Invariant Function|invariant]] per-channel summary.[^2]
- Contrast with [[Max Pooling]].

[^1]: [Prince, p. 172](zotero://open-pdf/library/items/BWT7FYX5?page=186&annotation=YWT9TXL4)
[^2]: Added from general knowledge.
