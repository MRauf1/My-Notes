---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Deep Convolutional GAN (DCGAN)[^1]
> A convolutional [[Generative Adversarial Network|GAN]] whose reliable training required:
> 1. [[Stride (Convolution)|Strided convolutions]] for [[Upsampling (Deep Learning)|upsampling]] and [[Downsampling (Deep Learning)|downsampling]] (instead of pooling);
> 2. [[Batch Normalization]] in both generator and discriminator, except in the generator's last layer and the discriminator's first layer;
> 3. [[Leaky ReLU]] activations in the discriminator;
> 4. the [[Adam]] optimizer with a lower momentum coefficient than usual ($\beta_1 = 0.5$).

# Properties
- Illustrates how fragile GAN training is: most deep learning models are relatively robust to such choices.[^1]
- Serves as the base architecture for [[Progressive Growing]].[^2]
- Freezing a DCGAN generator and repeatedly updating the discriminator shrinks the generator gradients, evidence for the vanishing-gradient problem of the original GAN loss.[^3]

[^1]: [Prince, p. 280](zotero://open-pdf/library/items/BWT7FYX5?page=294&annotation=KTE77RQX)
[^2]: [Prince, p. 287](zotero://open-pdf/library/items/BWT7FYX5?page=301&annotation=B5FXN2TF)
[^3]: [Prince, p. 283](zotero://open-pdf/library/items/BWT7FYX5?page=297&annotation=V9QJTZ5H)
