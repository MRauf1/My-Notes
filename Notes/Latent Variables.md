---
tags:
  - computer_science
  - deep_learning
---

# Definition

One approach to represent high-dimensional variables is through a lower-dimensional, smaller representation (latent variables). The idea behind this is that the real-world data is often generated due to some structure (like images being formed through physical processes), and this structure adds constraints to the problem, which makes the representation lower-dimensional (latent variables).[^1]

Latent variables typically have a simpler probability distribution, and in generative tasks, can produce the desired output with the help of [[Decoder|decoders]].

Latent variables, while used primarily in [[Unsupervised Learning|unsupervised learning]], can also be used with [[Supervised Learning|supervised learning]] models. This results in multiple benefits:

1) Since latent variables are lower-dimensional, one will likely need less training samples.
2) Since latent variables correspond to plausible data, one can better enforce the model to produce more plausible examples through using latent variables
3) By adding randomness to the mapping between either the latent variables or the latent variable with the corresponding output, one can generate multiple images with the supervised constraint (like images following a certain caption).

# Properties
- A latent variable $\mathbf{z}$ can be viewed as a compressed version of a data example $\mathbf{x}$ capturing its essential qualities; the mapping between $\mathbf{x}$ and $\mathbf{z}$ may go either direction ([[Unsupervised Learning]], [[Generative Model]]).[^2]
- Desired latent-space properties for generative models (well-behaved, disentangled): [[Generative Model Desiderata]].
- In a [[Generative Adversarial Network|GAN]], latents are mapped to data by the generator; mapping a real image back to latent space is [[GAN Inversion]].
- A [[Latent Variable Model|latent variable model]] describes $Pr(\mathbf{x})$ as the marginal of a joint $Pr(\mathbf{x}, \mathbf{z})$; with a deep-network likelihood it is the [[Nonlinear Latent Variable Model]] learned by a [[Variational Autoencoder]].
- In a [[Normalizing Flow|normalizing flow]], the latent variables have the same dimension as the data and are related to it by an invertible network.

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=23)
[^2]: [Prince, p. 269](zotero://open-pdf/library/items/BWT7FYX5?page=283&annotation=R3VM8G8Y)
