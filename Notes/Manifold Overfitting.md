---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Manifold Overfitting[^1]
> The failure of [[Maximum Likelihood Estimation|maximum likelihood]] with full-dimensional densities on data supported on a lower-dimensional [[Manifold|manifold]]: the model learns the manifold $\mathcal{M}$ but not the distribution on it, since the likelihood can be made arbitrarily large by concentrating mass near $\mathcal{M}$, whatever distribution along $\mathcal{M}$ is used.

> [!abstract] Manifold Overfitting Theorem (informal)[^1]
> Let $P^*$ be supported on a $k$-dimensional embedded submanifold $\mathcal{M} \subset \mathbb{R}^D$ (analytic in the original statement), $k < D$, with a continuous positive density on $\mathcal{M}$. Then for *any* other distribution $P^\dagger$ on $\mathcal{M}$ with a continuous positive density on $\mathcal{M}$, there is a sequence of densities $p_t$ on $\mathbb{R}^D$ (with respect to $\lambda_D$) such that
> $$
> \begin{align}
> p_t\,d\lambda_D \xrightarrow{\text{weakly}} P^\dagger \qquad \text{and} \qquad p_t(\mathbf{x}) \to \infty \quad \forall\, \mathbf{x} \in \mathcal{M}
> \end{align}
> $$
> so the likelihood of data drawn from $P^*$ diverges. Infinite likelihood is attainable while converging to the wrong distribution: maximum likelihood identifies $\mathcal{M}$ but not $P^*$.

*Intuition.* Spreading mass in a tube of radius $\sigma$ around $\mathcal{M}$ gives density of order $\sigma^{-(D-k)}$ ([[Manifold Hypothesis]], Weyl's tube formula). This factor diverges as $\sigma \to 0$ regardless of how mass is distributed *along* $\mathcal{M}$, and it dominates the finite term that would reward getting the on-manifold distribution right.

# Properties
- A consequence of the data being [[Mutually Singular Measures|mutually singular]] with every full-dimensional model, so the forward [[Kullback-Leibler Divergence]] is infinite ([[Maximum Likelihood Loss Optimality and Failure Modes]]).
- Affects any model trained by likelihood with a full-dimensional density: [[Normalizing Flow|normalizing flows]], [[Variational Autoencoder|VAEs]] with vanishing decoder variance, and energy-based models.
- **Two-step fix**: first learn the manifold with a dimension-reducing map (e.g. an autoencoder with a $k$-dimensional latent), then fit a likelihood-based density model in the $k$-dimensional latent space, where the encoded data has a density; [[Latent Diffusion Model|latent diffusion]] follows the same pattern.
- Other remedies: noise perturbation ([[Dequantization]], [[Diffusion Model|diffusion]] noise levels), injective/manifold flows that model a density on a learned manifold, and objectives not based on density ratios ([[Wasserstein Distance]]).

[^1]: Loaiza-Ganem, Ross, Cresswell & Caterini (2022), *Diagnosing and Fixing Manifold Overfitting in Deep Generative Models* ([arXiv:2204.07172](https://arxiv.org/abs/2204.07172)); supplementary notes provided by the creator.
