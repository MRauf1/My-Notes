---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Glow (Generative Flow)[^1]
> A [[Normalizing Flow|normalizing flow]] model for high-fidelity images. Each flow step consists of
> 1. **ActNorm**: a per-channel affine [[Elementwise Flow|elementwise]] layer (scale and bias), initialized from data so that activations have zero mean and unit variance;
> 2. **Invertible 1×1 convolution**: a learned channel permutation, i.e. a [[Linear Flow|linear flow]] on the channels at each position ([[1x1 Convolution]]), with $\log$-determinant $H \cdot W \cdot \log|\det \mathbf{W}|$, optionally [[LU Decomposition|LU]]-parameterized;
> 3. **Affine [[Coupling Flow|coupling layer]]** across channels.
>
> Flow steps are stacked within a [[Multi-Scale Flow|multi-scale]] architecture.

# Properties
- Trained on [[Dequantization|dequantized]] images by exact [[Maximum Likelihood Learning|maximum likelihood]].[^1]
- Its samples are good but below those of [[Generative Adversarial Network|GANs]] and [[Diffusion Model|diffusion models]].[^2]

[^1]: [Prince, p. 319](zotero://open-pdf/library/items/BWT7FYX5?page=333&annotation=WEGPQHRL); [Prince, p. 319](zotero://open-pdf/library/items/BWT7FYX5?page=333&annotation=TSQ29N5R)
[^2]: [Prince, p. 321](zotero://open-pdf/library/items/BWT7FYX5?page=335&annotation=T72FYWG2)
