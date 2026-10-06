---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Mode Dropping and Mode Collapse[^1]
> Failure modes of a [[Generative Adversarial Network|GAN]] generator $\mathbf{g}[\mathbf{z}, \boldsymbol{\theta}]$:
> - **Mode dropping**: the generated samples are plausible but represent only a subset of the data distribution.
> - **Mode collapse**: the extreme case in which the generator entirely or mostly ignores the [[Latent Variables|latent variables]] $\mathbf{z}$ and maps all samples to one or a few points.

# Properties
- Violates the coverage requirement of [[Generative Model Desiderata]]; detected by low recall in [[Manifold Precision and Recall]].
- **Putative cause**: the GAN loss with an optimal discriminator is the [[Jensen-Shannon Divergence]], whose coverage term does not depend on the generator, so the generator is not penalized for generating only a subset of examples accurately.[^2]
- Mitigated by [[Minibatch Discrimination]], which lets the discriminator compare the variation in a batch of samples against that of real data.[^3]
- Distinct from [[Model Collapse]], the degradation of models trained on their own generated outputs.

[^1]: [Prince, p. 281](zotero://open-pdf/library/items/BWT7FYX5?page=295&annotation=IXEZB85D)
[^2]: [Prince, p. 283](zotero://open-pdf/library/items/BWT7FYX5?page=297&annotation=ZD6YAEMZ)
[^3]: [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=BNF8TWA5)
