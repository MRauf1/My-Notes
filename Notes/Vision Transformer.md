---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Vision Transformer (ViT)[^1]
> A [[Transformer Encoder|transformer encoder]] for images: the image is divided into $16 \times 16$ patches, each patch is mapped to an input embedding by a learned linear transformation, learned 1D [[Positional Encoding|positional encodings]] are added, and a <cls> token is prepended whose output embedding is mapped by a final layer and a [[Softmax Function|softmax]] to class probabilities.

# Properties
- **Obstacles to transformers for images**: (i) images have far more pixels than sentences have words, so the quadratic cost of [[Self-Attention|self-attention]] is a bottleneck (patching addresses this); (ii) [[Convolutional Neural Network|CNNs]] have a good [[Inductive Bias|inductive bias]] (translation [[Equivariant Function|equivariance]] and 2D structure) that a transformer must learn from data.[^2]
- **Training**: supervised pre-training on 303 million labelled images from 18,000 classes, then the final layer is replaced with one mapping to the target classes and the network is fine-tuned ([[Transfer Learning]]). It reached 11.45% top-1 error on ImageNet, but without large-scale pre-training it underperformed the best contemporary CNNs: the strong inductive bias of convolution is overcome only with extremely large amounts of data.[^3]
- Vision transformers now exceed CNNs on image classification and other tasks, partly because of the scale at which they can be built and the size of pre-training datasets (e.g. JFT, LAION).[^4]
- **Single scale**: unlike CNNs, ViT works at a single resolution with a [[Receptive Field|receptive field]] covering the whole image from the first layer. Multi-scale vision transformers (e.g. Swin) instead start with small high-resolution patches and few channels and gradually enlarge the receptive field, lower the spatial resolution, and increase the embedding dimension, like CNNs.[^5]

[^1]: [Prince, p. 229](zotero://open-pdf/library/items/BWT7FYX5?page=243&annotation=U8LSZ6J7); [Prince, p. 229](zotero://open-pdf/library/items/BWT7FYX5?page=243&annotation=HWCR3JUC)
[^2]: [Prince, p. 228](zotero://open-pdf/library/items/BWT7FYX5?page=242&annotation=SI95WGWC); [Prince, p. 229](zotero://open-pdf/library/items/BWT7FYX5?page=243&annotation=7T3VRMPJ)
[^3]: [Prince, p. 229](zotero://open-pdf/library/items/BWT7FYX5?page=243&annotation=HWCR3JUC); [Prince, p. 230](zotero://open-pdf/library/items/BWT7FYX5?page=244&annotation=2XR7VRS6); [Prince, p. 230](zotero://open-pdf/library/items/BWT7FYX5?page=244&annotation=8CLW5ECL)
[^4]: [Prince, p. 229](zotero://open-pdf/library/items/BWT7FYX5?page=243&annotation=WNTKUJHI); [Prince, p. 238](zotero://open-pdf/library/items/BWT7FYX5?page=252&annotation=AEG4IWZR)
[^5]: [Prince, p. 230](zotero://open-pdf/library/items/BWT7FYX5?page=244&annotation=29UDHGHN); [Prince, p. 232](zotero://open-pdf/library/items/BWT7FYX5?page=246&annotation=JTJE5C4R)
