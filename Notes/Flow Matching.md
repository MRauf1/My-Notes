---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Flow Matching[^1]
> A simulation-free method for training a [[Continuous Normalizing Flow|continuous normalizing flow]] $d\mathbf{z}/dt = \mathbf{v}_{\boldsymbol{\phi}}(\mathbf{z}, t)$ by regressing its velocity field onto a target field $\mathbf{u}_t$ that generates a chosen probability path $p_t$ from noise $p_0 = \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$ to data $p_1 \approx p_{\text{data}}$:
> $$
> \begin{align}
> \mathcal{L}_{\text{FM}}(\boldsymbol{\phi}) = \mathbb{E}_{t \sim \mathcal{U}[0,1],\, \mathbf{x} \sim p_t}\left\|\mathbf{v}_{\boldsymbol{\phi}}(\mathbf{x}, t) - \mathbf{u}_t(\mathbf{x})\right\|^2
> \end{align}
> $$
> Since $\mathbf{u}_t$ is intractable, it is trained with the **conditional flow matching** loss. With the linear (rectified-flow) path $\mathbf{x}_t = (1 - t)\mathbf{x}_0 + t\,\mathbf{x}_1$, $\mathbf{x}_0 \sim \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$, $\mathbf{x}_1 \sim p_{\text{data}}$, the conditional velocity is $\mathbf{x}_1 - \mathbf{x}_0$ and
> $$
> \begin{align}
> \mathcal{L}_{\text{CFM}}(\boldsymbol{\phi}) = \mathbb{E}_{t,\, \mathbf{x}_0,\, \mathbf{x}_1}\left\|\mathbf{v}_{\boldsymbol{\phi}}(\mathbf{x}_t, t) - (\mathbf{x}_1 - \mathbf{x}_0)\right\|^2
> \end{align}
> $$

> [!abstract] Conditional Flow Matching Theorem[^1]
> $\nabla_{\boldsymbol{\phi}}\mathcal{L}_{\text{CFM}} = \nabla_{\boldsymbol{\phi}}\mathcal{L}_{\text{FM}}$. The two losses differ by a constant independent of $\boldsymbol{\phi}$, because the marginal field is the conditional expectation of the conditional field,
> $$
> \begin{align}
> \mathbf{u}_t(\mathbf{x}) = \mathbb{E}\left[\mathbf{x}_1 - \mathbf{x}_0 \mid \mathbf{x}_t = \mathbf{x}\right]
> \end{align}
> $$
> and the minimizer of a squared loss is the conditional mean. The field $\mathbf{u}_t$ generates $p_t$ in the sense of the continuity equation $\partial_t p_t + \nabla \cdot (p_t \mathbf{u}_t) = 0$.

Time runs from noise ($t = 0$) to data ($t = 1$), the reverse of the diffusion convention in [[Probability Flow ODE]].

# Properties
- **Simulation-free and likelihood-free**: training needs only samples $\mathbf{x}_0, \mathbf{x}_1$ and a regression loss; no ODE is solved and no density or Jacobian trace is evaluated, which avoids the costs and the degeneracies of [[Maximum Likelihood Loss Optimality and Failure Modes|maximum likelihood]] on near-singular data ([[Manifold Overfitting]]).
- **Generality**: other choices of path give other models; Gaussian paths recover the [[Probability Flow ODE]] of [[Diffusion Model|diffusion models]], and stochastic interpolants generalize the construction.[^2]
- **Rectified flow**: the linear path; re-training on the model's own (noise, sample) pairs ("reflow") straightens trajectories, so few integration steps are needed.[^3]
- **Sampling**: integrate the learned ODE from $\mathbf{x}_0 \sim \mathrm{Norm}[\mathbf{0}, \mathbf{I}]$ to $t = 1$; the result is an invertible map, so exact likelihoods remain available afterward via [[Continuous Normalizing Flow|instantaneous change of variables]].
- Used by state-of-the-art image generators (rectified-flow transformers), showing that invertible noise-to-data maps are expressive enough once trained by regression ([[Normalizing Flow Expressivity]]).[^4]

[^1]: Lipman, Chen, Ben-Hamu, Nickel & Le (2023) in `REFERENCES.md`; supplementary notes provided by the creator.
[^2]: Albergo & Vanden-Eijnden (2023) in `REFERENCES.md`.
[^3]: Liu, Gong & Liu (2023) in `REFERENCES.md`.
[^4]: Esser et al. (2024) in `REFERENCES.md`.
