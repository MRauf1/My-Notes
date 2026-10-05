---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Convolutional Neural Network (CNN)[^1]
> A [[Deep Neural Network|network]] consisting predominantly of a sequence of [[Convolutional Layer|convolutional layers]], each of which is translation-[[Equivariant Function|equivariant]], typically interleaved with [[Downsampling (Deep Learning)|pooling/downsampling]] mechanisms that induce partial translation [[Invariant Function|invariance]].

Motivated by three properties of images:[^2]
1. They are high-dimensional, so [[Linear Layer|fully connected layers]] would need an enormous number of parameters.
2. Nearby pixels are statistically related, which fully connected layers have no built-in notion of.
3. Their interpretation is stable under geometric transformations, so a pattern should not need to be re-learned at every position.

# Properties
- The [[Receptive Field]] of hidden units grows with depth (and faster with stride or [[Downsampling (Deep Learning)|downsampling]]), so information from across the image is gradually integrated, from local to global.[^3]
- Has a superior [[Inductive Bias]] to a fully connected network on image data: it shares information across positions instead of learning each template at every position.[^4]
- When the output is also an image (e.g. per-pixel segmentation), representations are downsampled and then [[Upsampling (Deep Learning)|upsampled]] back to full resolution, and [[1x1 Convolution|1×1 convolutions]] adjust channel counts when combining branches.[^5]
- [[Dropout]] is less effective for convolutional layers, since neighbouring pixels are highly correlated and dropped information is passed on via adjacent positions; [[Spatial Dropout]] and [[Cutout]] address this.[^6]
- Used as the backbone of [[Object Detection]].
- Understanding what a CNN computes is attempted with [[Feature Visualization]] and [[Network Dissection]]; these give partial insight (earlier layers correlate with texture and color, later layers with object type), but fully understanding networks with millions of parameters is currently not possible ([[Interpretability (Machine Learning)]]).[^7]

[^1]: [Prince, p. 161](zotero://open-pdf/library/items/BWT7FYX5?page=175&annotation=TULQ84TG); [Prince, p. 163](zotero://open-pdf/library/items/BWT7FYX5?page=177&annotation=6LPDNNE6)
[^2]: [Prince, p. 161](zotero://open-pdf/library/items/BWT7FYX5?page=175&annotation=EW2MTDDW); [Prince, p. 161](zotero://open-pdf/library/items/BWT7FYX5?page=175&annotation=9CJJCDXJ); [Prince, p. 161](zotero://open-pdf/library/items/BWT7FYX5?page=175&annotation=BMIQHH9T)
[^3]: [Prince, p. 167](zotero://open-pdf/library/items/BWT7FYX5?page=181&annotation=LMGVCYWW); [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=2BL7VV7Z)
[^4]: [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=ZKKHF27M); [Prince, p. 170](zotero://open-pdf/library/items/BWT7FYX5?page=184&annotation=EE2MMBYY)
[^5]: [Prince, p. 171](zotero://open-pdf/library/items/BWT7FYX5?page=185&annotation=2BL7VV7Z)
[^6]: [Prince, p. 183](zotero://open-pdf/library/items/BWT7FYX5?page=197&annotation=V6VYB47L)
[^7]: [Prince, p. 184](zotero://open-pdf/library/items/BWT7FYX5?page=198&annotation=7WATMM6L)
