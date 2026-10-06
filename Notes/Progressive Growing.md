---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Progressive Growing[^1]
> A [[Generative Adversarial Network|GAN]] training scheme that first trains a GAN to synthesize $4 \times 4$ images and then repeatedly adds layers to the generator (which [[Upsampling (Deep Learning)|upsample]] and further process the representation, e.g. to $8 \times 8$) and matching layers to the discriminator (so it can classify the higher-resolution images).

# Properties
- New higher-resolution layers "fade in" gradually: initially the higher-resolution output is an upsampled copy of the previous result passed through a [[Residual Connection|residual connection]], and the new layers progressively take over.[^1]
- Coarse structure is learned first at low resolution, which stabilizes training of high-resolution generators.

[^1]: [Prince, p. 287](zotero://open-pdf/library/items/BWT7FYX5?page=301&annotation=B5FXN2TF); [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=BNF8TWA5)
