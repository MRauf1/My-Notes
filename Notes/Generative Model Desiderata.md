---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Generative Model Desiderata[^1]
> Desirable properties of a [[Generative Model|generative model]] based on [[Latent Variables|latent variables]] $\mathbf{z}$:
> - **Efficient sampling**: generating samples is computationally cheap and exploits the parallelism of modern hardware.
> - **High-quality sampling**: samples are indistinguishable from the real training data.
> - **Coverage**: samples represent the entire training distribution, not just a subset of it.
> - **Well-behaved latent space**: every $\mathbf{z}$ corresponds to a plausible data example $\mathbf{x}$, and smooth changes in $\mathbf{z}$ give smooth changes in $\mathbf{x}$.
> - **Disentangled latent space**: manipulating each dimension of $\mathbf{z}$ changes an interpretable property of the data.
> - **Efficient likelihood computation**: for a [[Probabilistic Generative Model|probabilistic model]], the probability of new examples can be computed efficiently and accurately.

![[Generative Model Properties Comparison.png]]

# Properties
- No existing family has all of these properties:[^2]
	- [[Generative Adversarial Network|GANs]]: efficient, high sample quality, well-behaved latent space, but poor coverage and no likelihood.
	- [[Variational Autoencoder|VAEs]]: efficient with a well-behaved latent space, but lower sample quality and no efficient (exact) likelihood.
	- [[Normalizing Flow|Normalizing flows]]: efficient, well-behaved latent space, and the only family with efficient exact likelihood, but lower sample quality.
	- [[Diffusion Model|Diffusion models]]: high sample quality, but slow sampling, a poorly behaved and entangled latent space, and no efficient likelihood.
- Quality and coverage are quantified by [[Test Likelihood]], [[Inception Score]], [[Fréchet Inception Distance]], and [[Manifold Precision and Recall]].

[^1]: [Prince, p. 270](zotero://open-pdf/library/items/BWT7FYX5?page=284&annotation=QZ2QFN6G); [Prince, p. 271](zotero://open-pdf/library/items/BWT7FYX5?page=285&annotation=EQDJ9Y5L)
[^2]: [Prince, p. 272](zotero://open-pdf/library/items/BWT7FYX5?page=286&annotation=HGG8MKC7)
