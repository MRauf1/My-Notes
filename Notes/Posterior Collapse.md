---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Posterior Collapse[^1]
> A failure mode in training a [[Variational Autoencoder]] in which the encoder always predicts the prior, $q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta}) \approx Pr(\mathbf{z})$ for every $\mathbf{x}$, so the latent carries no information about the data and the KL term of the [[Evidence Lower Bound]] is zero.

It is typically associated with a decoder powerful enough to model the data without using $\mathbf{z}$ (e.g. an autoregressive one), so the cheapest way to raise the ELBO is to drive $D_{KL}[q(\mathbf{z}|\mathbf{x}, \boldsymbol{\theta}) \,\|\, Pr(\mathbf{z})]$ to zero.

# Properties
- Identified by Bowman et al. (2015); mitigated by KL annealing, i.e. gradually increasing the weight of the KL term during training.[^1]
- Several other remedies have been proposed (Razavi et al., 2019; Lucas et al., 2019), and it is part of the motivation for a discrete latent space (VQ-VAE, van den Oord et al., 2017).[^1]

[^1]: [Prince, p. 346](zotero://open-pdf/library/items/BWT7FYX5?page=360&annotation=39878WWA)
