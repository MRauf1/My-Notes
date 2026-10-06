---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] StyleGAN[^1][^2][^3]
> A [[Generative Adversarial Network|GAN]] that partitions the variation in a dataset into components controlled by separate subsets of [[Latent Variables|latent variables]], separating **style** from **noise** and controlling the output at different **scales**:
> - **Main branch**: starts from a learned constant $4 \times 4 \times 512$ tensor and passes through convolutional layers that progressively [[Upsampling (Deep Learning)|upsample]] to the final resolution.
> - **Noise**: independent Gaussian tensors $\mathbf{z}_1, \mathbf{z}_2, \dots$, of the same spatial size as the representation, scaled by learned per-channel factors $\psi_1, \psi_2, \dots$ and added after each convolution.
> - **Style**: a $1 \times 1 \times 512$ noise vector is mapped by a seven-layer fully connected network to an intermediate variable $\mathbf{w}$, which is linearly transformed into vectors $\mathbf{y}_1, \mathbf{y}_2, \dots$ (each $2 \times 512$) that set the per-channel mean and variance of the representation after noise addition, via [[Adaptive Instance Normalization]].

# Properties
- Latents injected closer to the output control finer-scale details: for faces, coarse layers control face shape and head pose, middle layers the shape and details of facial features, and fine layers hair and skin colour.[^1][^3]
- Style captures variation salient to humans; noise captures unimportant stochastic variation such as the exact placement of hairs, stubble, freckles, or skin pores.[^1]
- The mapping network decorrelates the style so that each dimension of $\mathbf{w}$ can represent an independent real-world factor ([[Generative Model Desiderata|disentangled latent space]]).[^4]
- Generalizes the standard GAN design in which a single $\mathbf{z}$ enters only at the input: latents can (i) be introduced at various points and (ii) modify the representation in different ways.[^2]
- The same style vector applied at several points lets a style contribute across scales; mixing styles from different $\mathbf{w}$ at different layers mixes attributes at the corresponding scales.[^5]
- Supports the [[Truncation Trick]] in $\mathbf{w}$-space and [[GAN Inversion]] for real-image editing.

[^1]: [Prince, p. 296](zotero://open-pdf/library/items/BWT7FYX5?page=310&annotation=QUNV9ZS4)
[^2]: [Prince, p. 296](zotero://open-pdf/library/items/BWT7FYX5?page=310&annotation=MIPBXXDM)
[^3]: [Prince, p. 296](zotero://open-pdf/library/items/BWT7FYX5?page=310&annotation=WHLIUI7I); [Prince, p. 296](zotero://open-pdf/library/items/BWT7FYX5?page=310&annotation=TNR96RPE)
[^4]: [Prince, p. 296](zotero://open-pdf/library/items/BWT7FYX5?page=310&annotation=Y8KPCTP7)
[^5]: [Prince, p. 298](zotero://open-pdf/library/items/BWT7FYX5?page=312&annotation=95SC89JB)
