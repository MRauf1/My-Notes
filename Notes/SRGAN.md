---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Super-Resolution GAN (SRGAN)[^1]
> A super-resolution model: a [[Convolutional Neural Network|convolutional network]] with [[Residual Connection|residual connections]] that ingests a low-resolution image and converts it to a high-resolution image via [[Upsampling (Deep Learning)|upsampling]] layers, trained with three losses:
> - a **content loss**, the squared difference between the output and the true high-resolution image;
> - a [[Perceptual Loss|VGG (perceptual) loss]], the squared difference between VGG activations of output and ground truth;
> - an [[Adversarial Loss|adversarial loss]] from a discriminator distinguishing real high-resolution images from upsampled ones.

# Properties
- The content loss enforces fidelity, the perceptual loss semantic similarity, and the adversarial loss realism.[^1]
- The adversarial term yields sharper, more realistic textures but not necessarily a lower pixel error than training on the content loss alone.[^1]

[^1]: [Prince, p. 293](zotero://open-pdf/library/items/BWT7FYX5?page=307&annotation=PFWVG6XU)
