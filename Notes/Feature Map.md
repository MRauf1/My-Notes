---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Feature Map[^1]
> The set of hidden variables produced by one of several convolutions computed in parallel within a [[Convolutional Layer|convolutional layer]]; also called a **channel**.

# Properties
- Multiple feature maps are needed because a single convolution would likely lose information: it averages nearby inputs, and a [[ReLU Function|ReLU]] clips results below zero.[^1]
- In general both the input and the hidden layers have multiple channels (e.g. an RGB image has three); a layer's hidden units are a 3D [[Tensor]] (height × width × channels) in 2D.[^2]
- Each output channel is a weighted sum over all input channels at the kernel's positions; [[1x1 Convolution|1×1 convolutions]] change the number of channels without spatial mixing.
- [[Spatial Dropout]] drops entire feature maps.

[^1]: [Prince, p. 165](zotero://open-pdf/library/items/BWT7FYX5?page=179&annotation=RR6LJUI2)
[^2]: [Prince, p. 167](zotero://open-pdf/library/items/BWT7FYX5?page=181&annotation=REWX9AMS); [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=IN8DPHQX)
