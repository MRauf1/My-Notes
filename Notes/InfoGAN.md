---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] InfoGAN[^1]
> A [[Generative Adversarial Network|GAN]] that discovers important attributes automatically: the generator receives random noise $\mathbf{z}$ together with random attribute variables $\mathbf{c}$, and the discriminator both predicts whether the image is real or synthesized and estimates $\mathbf{c}$ from it.

# Properties
- **Insight**: interpretable real-world characteristics should be the easiest to predict from the image, so they come to be represented by $\mathbf{c}$ ([[Generative Model Desiderata|disentangled latent space]]).[^1]
- Discrete attributes use a binary or multiclass [[Cross-Entropy Loss|cross-entropy loss]] and identify categories in the data; continuous attributes use a least squares loss ([[Mean Squared Error]]) and identify gradual modes of variation.[^1]
- Minimizing the attribute-prediction loss maximizes a variational lower bound on the [[Mutual Information]] $I(\mathbf{c}; \mathbf{g}[\mathbf{z}, \mathbf{c}])$ between the attributes and the generated sample (Chen et al., 2016).
- Contrasts with the [[Conditional GAN]] and [[Auxiliary Classifier GAN]], whose attributes are predetermined.

[^1]: [Prince, p. 291](zotero://open-pdf/library/items/BWT7FYX5?page=305&annotation=7DTDSMA9)
