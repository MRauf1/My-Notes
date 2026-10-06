---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Adversarial Loss[^1][^2]
> A loss term for a [[Supervised Learning|supervised]] network that penalizes its outputs whenever a discriminator, trained alongside it, can distinguish them from real examples of the output domain. The discriminator acts as a learned prior favouring realism.

# Properties
- Uses the discriminator idea of the [[Generative Adversarial Network|GAN]] outside random sample generation, for translating one data example into another.[^1]
- Needs no additional labelled data: the discriminator compares outputs with unpaired real examples of the output domain, unlike the paired discriminator of [[Pix2Pix]].[^2]
- Can be applied to the entire output or per patch ([[PatchGAN]]).[^2]
- Improves the realism of complex structured outputs, but does not necessarily improve the solution with respect to the original loss function.[^2]
- Used in [[SRGAN]] and [[CycleGAN]], typically combined with a content loss and/or a [[Perceptual Loss]].
- Distinct from [[Adversarial Training]], which perturbs inputs to improve robustness.

[^1]: [Prince, p. 291](zotero://open-pdf/library/items/BWT7FYX5?page=305&annotation=W9HV4LEK)
[^2]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=PFWVG6XU)
