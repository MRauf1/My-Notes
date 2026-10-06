---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] PatchGAN[^1]
> A purely convolutional discriminator whose last-layer hidden units each classify the region within their [[Receptive Field|receptive field]] as real or synthesized; the per-patch responses are averaged to give the final output.

# Properties
- Judges local texture rather than global structure; used in [[Pix2Pix]], where a content loss already constrains the large-scale image structure.[^1]
- Being fully convolutional, it has fewer parameters and applies to images of arbitrary size.
- Realizes an [[Adversarial Loss]] at the patch level rather than over the whole output.[^2]

[^1]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=Q4RFIAZQ)
[^2]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=PFWVG6XU)
