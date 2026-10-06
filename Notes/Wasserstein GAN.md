---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Wasserstein GAN (WGAN)[^1]
> A [[Generative Adversarial Network|GAN]] whose discriminator (*critic*) $f[\mathbf{x}, \boldsymbol{\phi}]$ estimates the dual form of the [[Wasserstein Distance]] between generated samples $\mathbf{x}_j^* = \mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}]$ and real examples $\mathbf{x}_i$, replacing the maximization over 1-Lipschitz functions with optimization of network parameters and the integrals with sample sums:
> $$
> \begin{align}
> L[\boldsymbol{\phi}] = \sum_j f[\mathbf{x}_j^*, \boldsymbol{\phi}] - \sum_i f[\mathbf{x}_i, \boldsymbol{\phi}] = \sum_j f[\mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}], \boldsymbol{\phi}] - \sum_i f[\mathbf{x}_i, \boldsymbol{\phi}]
> \end{align}
> $$
> subject to the critic having gradient norm at most one everywhere,
> $$
> \begin{align}
> \left\|\frac{\partial f[\mathbf{x}, \boldsymbol{\phi}]}{\partial \mathbf{x}}\right\| \leq 1
> \end{align}
> $$
> The critic minimizes $L[\boldsymbol{\phi}]$; the generator minimizes $-\sum_j f[\mathbf{g}[\mathbf{z}_j, \boldsymbol{\theta}], \boldsymbol{\phi}]$.

# Properties
- The critic output is an unbounded score with no [[Sigmoid Function|sigmoid]]; $-L[\boldsymbol{\phi}]$ estimates the Wasserstein distance (up to scale).
- Makes GAN training more stable: the Wasserstein distance gives useful gradients even when the generated and real distributions are disjoint, avoiding the vanishing gradients of the [[Jensen-Shannon Divergence]] objective.[^1][^2]
- **Enforcing the [[Lipschitz Continuity|Lipschitz]] constraint**:[^1]
	- **Weight clipping**: clip the critic weights to a small range (e.g. $\pm 0.01$); crude, it limits capacity and can make optimization difficult.
	- **WGAN-GP** (gradient penalty): add a regularization term that grows as the critic's gradient norm deviates from one, $\lambda\,\mathbb{E}_{\hat{\mathbf{x}}}\left[\left(\|\nabla_{\hat{\mathbf{x}}} f[\hat{\mathbf{x}}, \boldsymbol{\phi}]\| - 1\right)^2\right]$, evaluated at random interpolates $\hat{\mathbf{x}}$ between real and generated samples (Gulrajani et al., 2017).
	- Spectral normalization of the critic weights (Miyato et al., 2018) is a widely used alternative.
- Stability alone does not give high-quality images; [[Progressive Growing]], [[Minibatch Discrimination]], and the [[Truncation Trick]] are also used.[^2]

[^1]: [Prince, p. 286](zotero://open-pdf/library/items/BWT7FYX5?page=300&annotation=G2WPF6U8)
[^2]: [Prince, p. 287](zotero://open-pdf/library/items/BWT7FYX5?page=301&annotation=B5FXN2TF); [Prince, p. 284](zotero://open-pdf/library/items/BWT7FYX5?page=298&annotation=5I685ZVX)
