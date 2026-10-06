---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Truncation Trick[^1]
> Sampling only [[Latent Variables|latent variables]] $\mathbf{z}$ with high probability (close to the mean of the base distribution) when generating with a [[Generative Adversarial Network|GAN]], e.g. by resampling components of $\mathbf{z}$ whose magnitude exceeds a threshold.

# Properties
- Trades diversity for quality: reduces the variation of the samples but improves their fidelity.[^1]
- The threshold acts as a knob along the precision–recall trade-off ([[Manifold Precision and Recall]]).
- In [[StyleGAN]], truncation is applied in the intermediate latent space by shrinking $\mathbf{w}$ toward its mean, $\mathbf{w}' = \bar{\mathbf{w}} + \psi(\mathbf{w} - \bar{\mathbf{w}})$ with $\psi < 1$.

[^1]: [Prince, p. 289](zotero://open-pdf/library/items/BWT7FYX5?page=303&annotation=BNF8TWA5)
