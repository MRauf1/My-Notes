---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Pix2Pix[^1][^2]
> A paired image-to-image translation model $\hat{\mathbf{x}} = \mathbf{g}[\mathbf{c}, \boldsymbol{\theta}]$ that maps an image $\mathbf{c}$ to an image $\mathbf{x}$ of a different style using a [[U-Net]], trained with two losses:
> - a **content loss**, the [[L1 Norm|$\ell_1$ norm]] $\|\mathbf{x} - \mathbf{g}[\mathbf{c}, \boldsymbol{\theta}]\|_1$ between the ground-truth output and the prediction;
> - an **adversarial loss** from a discriminator $f[\mathbf{c}, \mathbf{x}, \boldsymbol{\phi}]$ that ingests before/after pairs and tries to distinguish real (input, ground truth) pairs from (input, synthesized) pairs.

# Properties
- Can be viewed as a [[Conditional GAN|conditional GAN]] whose generator is a U-Net conditioned on an image rather than a label.[^2]
- Not a generator in the conventional sense: the U-Net receives no noise. The original authors tried adding noise $\mathbf{z}$ alongside $\mathbf{c}$, but the network learned to ignore it.[^2]
- Division of labour: the content loss ensures the large-scale structure is correct, so the discriminator mainly needs to ensure plausible local texture, which motivates the [[PatchGAN]] discriminator.[^2]
- Requires ground-truth before/after pairs; [[CycleGAN]] removes this requirement.[^3]

[^1]: [Prince, p. 292](zotero://open-pdf/library/items/BWT7FYX5?page=306&annotation=D7D3ZKQR)
[^2]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=Q4RFIAZQ)
[^3]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=7IDRW3PG)
