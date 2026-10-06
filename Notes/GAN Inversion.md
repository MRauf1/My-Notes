---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] GAN Inversion (Resynthesis)[^1]
> Editing a real image $\mathbf{x}$ with a trained [[Generative Adversarial Network|GAN]] generator $\mathbf{g}[\mathbf{z}, \boldsymbol{\theta}]$ by (i) projecting it to latent space, $\hat{\mathbf{z}} \approx \mathbf{g}^{-1}[\mathbf{x}]$, (ii) manipulating the latent variable, and (iii) re-projecting it to image space with the generator.

# Properties
- Necessary because a GAN has no encoder: the generator maps only from [[Latent Variables|latent variables]] to data.
- Projection is typically done by optimization, $\hat{\mathbf{z}} = \operatorname{argmin}_{\mathbf{z}} \ell\left[\mathbf{g}[\mathbf{z}, \boldsymbol{\theta}], \mathbf{x}\right]$ with a pixel and/or [[Perceptual Loss|perceptual]] loss, by training an encoder, or by combining both.
- Editing is only meaningful with a well-behaved, disentangled latent space ([[Generative Model Desiderata]]), as in [[StyleGAN]].

[^1]: [Prince, p. 302](zotero://open-pdf/library/items/BWT7FYX5?page=316&annotation=44KUHMX9)
