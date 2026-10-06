---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Auxiliary Classifier GAN (ACGAN)[^1]
> A [[Conditional GAN|conditional GAN]] whose discriminator receives only the real or synthesized image and must correctly predict its attribute. For a discrete attribute with $C$ categories, the discriminator has $C + 1$ outputs: the first passes through a [[Sigmoid Function|sigmoid]] to predict real vs. generated, and the remaining $C$ pass through a [[Softmax Function|softmax]] to predict the class probabilities.

# Properties
- Simplifies conditional generation, since the attribute need not be injected into the discriminator.[^1]
- The class head is trained with a [[Cross-Entropy Loss|cross-entropy loss]] on both real and generated images; trained this way, networks can synthesize multiple ImageNet classes.[^1]

[^1]: [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=7RW3MWUR); [Prince, p. 291](zotero://open-pdf/library/items/BWT7FYX5?page=305&annotation=LHG6HTMV)
