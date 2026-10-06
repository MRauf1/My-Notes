---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Probability Flow ODE[^1]
> For a forward diffusion written as a stochastic differential equation
> $$
> \begin{align}
> d\mathbf{z} = \mathbf{f}(\mathbf{z}, t)\,dt + g(t)\,d\mathbf{w}
> \end{align}
> $$
> with marginals $q_t(\mathbf{z})$, the deterministic [[Ordinary Differential Equation|ordinary differential equation]]
> $$
> \begin{align}
> \frac{d\mathbf{z}}{dt} = \mathbf{f}(\mathbf{z}, t) - \frac{1}{2}g(t)^2\,\nabla_{\mathbf{z}}\log q_t(\mathbf{z})
> \end{align}
> $$
> has the same marginal distributions $q_t$ for every $t$ (Song et al., 2021). Integrating it backward from $\mathbf{z}_T \sim \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$, with the score $\nabla\log q_t$ supplied by a trained noise predictor, generates data.

# Properties
- **Reverse-time SDE**: the stochastic counterpart $d\mathbf{z} = \left[\mathbf{f}(\mathbf{z}, t) - g(t)^2\nabla\log q_t(\mathbf{z})\right]dt + g(t)\,d\bar{\mathbf{w}}$, run backward in time, also has marginals $q_t$ (Anderson, 1982); ancestral sampling of a [[Diffusion Model|diffusion model]] discretizes it.
- **DDPM as an SDE**: the [[Diffusion Forward Process]] is the discretization of the variance-preserving SDE $\mathbf{f} = -\frac{1}{2}\beta(t)\mathbf{z}$, $g = \sqrt{\beta(t)}$. The score is $\nabla\log q_t(\mathbf{z}) \approx -\mathbf{g}[\mathbf{z}, t]/\sqrt{1-\alpha_t}$ ([[Diffusion Model Loss Function]]).
- **Fast sampling**: off-the-shelf and specialized ODE solvers (higher-order, adaptive) can be applied; [[Denoising Diffusion Implicit Model|DDIM]] is one discretization. Karras et al. (2022) identified good time discretizations and sampler schedules, sharply reducing the required number of steps.[^1]
- **Exact likelihood**: the ODE defines an invertible map, i.e. a continuous [[Normalizing Flow|normalizing flow]], so the log-likelihood can be computed via the instantaneous change of variables $\frac{d\log q_t}{dt} = -\nabla\cdot\left(\frac{d\mathbf{z}}{dt}\right)$, with the divergence estimated by [[Hutchinson's Trace Estimator]].
- Gives a deterministic encoding of data to latents, enabling interpolation and inversion.

[^1]: [Prince, p. 371](zotero://open-pdf/library/items/BWT7FYX5?page=385&annotation=A2M52S2R)
