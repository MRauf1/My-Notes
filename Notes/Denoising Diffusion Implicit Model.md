---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Denoising Diffusion Implicit Model (DDIM)[^1][^2]
> A [[Diffusion Model|diffusion model]] whose forward process is non-Markovian but has the same [[Diffusion Kernel|diffusion kernel]] $q(\mathbf{z}_t|\mathbf{x}) = \mathrm{Norm}_{\mathbf{z}_t}[\sqrt{\alpha_t}\,\mathbf{x}, (1-\alpha_t)\mathbf{I}]$, so it is trained with the same noise-prediction loss ([[Diffusion Model Loss Function]]) and can reuse a trained network $\mathbf{g}_t$. Song et al. (2021) define the family
> $$
> \begin{align}
> q_\sigma(\mathbf{z}_{t-1}|\mathbf{z}_t, \mathbf{x}) = \mathrm{Norm}_{\mathbf{z}_{t-1}}\left[\sqrt{\alpha_{t-1}}\,\mathbf{x} + \sqrt{1-\alpha_{t-1}-\sigma_t^2}\cdot\frac{\mathbf{z}_t - \sqrt{\alpha_t}\,\mathbf{x}}{\sqrt{1-\alpha_t}},\; \sigma_t^2\mathbf{I}\right]
> \end{align}
> $$
> where $\sigma_t^2 = \beta_t(1-\alpha_{t-1})/(1-\alpha_t)$ recovers the standard (DDPM) [[Conditional Diffusion Distribution|conditional diffusion distribution]] and $\sigma_t = 0$ gives DDIM. Sampling first estimates the clean data and noise, then re-noises deterministically:
> $$
> \begin{align}
> \hat{\mathbf{x}} = \frac{\mathbf{z}_t - \sqrt{1-\alpha_t}\,\mathbf{g}_t[\mathbf{z}_t, \boldsymbol{\phi}_t]}{\sqrt{\alpha_t}}, \qquad \mathbf{z}_{t-1} = \sqrt{\alpha_{t-1}}\,\hat{\mathbf{x}} + \sqrt{1-\alpha_{t-1}}\,\mathbf{g}_t[\mathbf{z}_t, \boldsymbol{\phi}_t]
> \end{align}
> $$

# Properties
- **Deterministic**: the forward process is stochastic only in the first step from $\mathbf{x}$ to $\mathbf{z}_1$; the reverse map from $\mathbf{z}_T$ to $\mathbf{x}$ is deterministic, so the latent $\mathbf{z}_T$ becomes a meaningful encoding (it can be inverted and interpolated).[^1]
- **Accelerated sampling**: the forward process can be defined on a sub-sequence of time steps, so the reverse process skips steps; good samples with about 50 steps instead of $\sim 1000$.[^1]
- **ODE view**: DDIM is a discretization (Euler-type) of the [[Probability Flow ODE]], whose low-curvature trajectories tolerate large steps and admit efficient numerical ODE solvers.[^2]
- Still slower than most single-pass generative models such as [[Generative Adversarial Network|GANs]] (as of Prince, 2023).[^1]

[^1]: [Prince, p. 364](zotero://open-pdf/library/items/BWT7FYX5?page=378&annotation=TIIGX58K); [Prince, p. 365](zotero://open-pdf/library/items/BWT7FYX5?page=379&annotation=D7TIBGCS)
[^2]: [Prince, p. 371](zotero://open-pdf/library/items/BWT7FYX5?page=385&annotation=9DW7EJJ4)
