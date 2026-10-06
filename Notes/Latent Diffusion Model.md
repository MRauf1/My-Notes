---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Latent Diffusion Model[^1]
> A [[Diffusion Model|diffusion model]] run in the latent space of a pre-trained conventional autoencoder rather than on the data: an encoder maps $\mathbf{x}$ to a smaller latent $\mathbf{h}$, the diffusion model is trained and sampled on $\mathbf{h}$, and the autoencoder's decoder maps generated latents back to data (Rombach et al., 2022; "Stable Diffusion").

# Properties
- Reduces the dimensionality the diffusion process works on, making training and sampling much cheaper; the autoencoder handles perceptual detail.[^1]
- Allows other data types (text, graphs, etc.) to be modeled by diffusion once they are embedded in a continuous latent space.[^1]
- Conditioning (e.g. text) is typically injected through cross-attention in the [[U-Net]], combined with [[Classifier-Free Guidance]].
- Vahdat et al. (2021) take a similar approach, learning a [[Variational Autoencoder|VAE]] jointly with a score-based model in its latent space.[^1]

[^1]: [Prince, p. 371](zotero://open-pdf/library/items/BWT7FYX5?page=385&annotation=YS6DU3NW)
