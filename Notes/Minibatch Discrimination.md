---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Minibatch Discrimination[^1]
> A [[Generative Adversarial Network|GAN]] technique in which feature statistics computed across a mini-batch of synthesized or real data are summarized and appended as an extra feature map (usually toward the end of the discriminator), so the discriminator judges batches by their variety as well as individual realism.

# Properties
- The discriminator can then signal the generator to include as much variation in its samples as exists in the data, which helps prevent [[Mode Collapse]].[^1]
- A common lightweight variant appends the average across the batch of per-feature standard deviations (minibatch standard deviation, Karras et al., 2018).

[^1]: [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=BNF8TWA5)
