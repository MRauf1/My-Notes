---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Ancestral Sampling[^1]
> Drawing a sample from a joint distribution that factorizes along a directed acyclic graph,
> $$
> \begin{align}
> Pr(\mathbf{v}_1, \dots, \mathbf{v}_K) = \prod_{k=1}^K Pr(\mathbf{v}_k | \mathrm{pa}(\mathbf{v}_k))
> \end{align}
> $$
> by visiting the variables in topological order and drawing each $\mathbf{v}_k^*$ from its conditional given the already-drawn values of its parents $\mathrm{pa}(\mathbf{v}_k)$. Discarding the unwanted variables leaves a sample from the marginal of the rest.

For a [[Latent Variable Model|latent variable model]] $Pr(\mathbf{x}, \mathbf{z}) = Pr(\mathbf{x}|\mathbf{z})Pr(\mathbf{z})$ this is two steps: draw $\mathbf{z}^* \sim Pr(\mathbf{z})$, then $\mathbf{x}^* \sim Pr(\mathbf{x}|\mathbf{z}^*)$. Keeping only $\mathbf{x}^*$ gives a sample from the marginal $Pr(\mathbf{x})$ without ever evaluating it.

# Properties
- Exact and non-iterative, unlike [[Markov Chain Monte Carlo]]; it only requires that each conditional be easy to sample.
- Used to generate from the [[Nonlinear Latent Variable Model]] and hence a [[Variational Autoencoder]]: $\mathbf{z}^* \sim \mathrm{Norm}_{\mathbf{z}}[\mathbf{0}, \mathbf{I}]$, then $\mathbf{x}^* \sim \mathrm{Norm}_{\mathbf{x}}[\mathbf{f}[\mathbf{z}^*, \boldsymbol{\phi}], \sigma^2\mathbf{I}]$.
- Generates from a [[Diffusion Model|diffusion model]] by walking the learned reverse chain $\mathbf{z}_T \to \mathbf{z}_{T-1} \to \dots \to \mathbf{x}$, drawing each step from its Gaussian conditional.
- The two-stage view of sampling from a [[Mixture Distribution]] (pick a component, then draw from it) is ancestral sampling.

[^1]: [Prince, p. 329](zotero://open-pdf/library/items/BWT7FYX5?page=343&annotation=PERWBZVB)
