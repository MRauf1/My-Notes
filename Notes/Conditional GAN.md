---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Conditional GAN (cGAN)[^1][^2]
> A [[Generative Adversarial Network|GAN]] that passes a vector $\mathbf{c}$ of attributes to both the generator $\mathbf{g}[\mathbf{z}, \mathbf{c}, \boldsymbol{\theta}]$ and the discriminator $f[\mathbf{x}, \mathbf{c}, \boldsymbol{\phi}]$. The generator transforms $\mathbf{z}$ into a sample with attribute $\mathbf{c}$; the discriminator distinguishes (i) a generated sample paired with its target attribute from (ii) a real example paired with its real attribute.

# Types
- [[Auxiliary Classifier GAN]]: the discriminator predicts the attribute instead of receiving it.
- [[InfoGAN]]: the attributes are discovered automatically.
- [[Pix2Pix]]: conditioned on an image rather than a label.

# Properties
- Gives control over sample attributes (e.g. hair colour or age of faces), which an unconditional GAN lacks without training a separate GAN per attribute combination.[^1]
- **Injecting $\mathbf{c}$**: for the generator, append $\mathbf{c}$ to $\mathbf{z}$; for the discriminator, append it to the input if the data are 1D, or for images linearly transform it to a 2D map and append it as an extra channel to the input or to an intermediate hidden layer.[^2]

[^1]: [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=A274ZG6X)
[^2]: [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=ZRZ38SVW)
