---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Continuous Normalizing Flow[^1]
> A [[Normalizing Flow|normalizing flow]] defined by an [[Ordinary Differential Equation|ODE]] with a neural velocity field $\mathbf{v}_{\boldsymbol{\phi}}$:
> $$
> \begin{align}
> \frac{d\mathbf{z}(t)}{dt} = \mathbf{v}_{\boldsymbol{\phi}}(\mathbf{z}(t), t), \qquad \mathbf{z}(0) \sim Pr(\mathbf{z}) = \mathrm{Norm}[\mathbf{0}, \mathbf{I}], \qquad \mathbf{x} = \mathbf{z}(1)
> \end{align}
> $$
> The density along a trajectory obeys the **instantaneous change of variables** formula, so the log-likelihood is
> $$
> \begin{align}
> \frac{d \log p_t(\mathbf{z}(t))}{dt} = -\operatorname{trace}\left[\frac{\partial \mathbf{v}_{\boldsymbol{\phi}}}{\partial \mathbf{z}}(\mathbf{z}(t), t)\right] \quad\Longrightarrow\quad \log p_1(\mathbf{x}) = \log Pr(\mathbf{z}(0)) - \int_0^1 \operatorname{trace}\left[\frac{\partial \mathbf{v}_{\boldsymbol{\phi}}}{\partial \mathbf{z}}\right] dt
> \end{align}
> $$

# Properties
- **Free-form Jacobian**: only the [[Trace|trace]] of the velocity Jacobian is needed, not a determinant, so $\mathbf{v}_{\boldsymbol{\phi}}$ can be any network; no triangular or coupling structure is required. The trace is estimated without forming the Jacobian by [[Hutchinson's Trace Estimator]] with vector-Jacobian products (FFJORD).[^2]
- **Invertible by construction**: integrating the ODE backward from $t = 1$ to $t = 0$ inverts the map. If $\mathbf{v}_{\boldsymbol{\phi}}$ is [[Lipschitz Continuity|Lipschitz]] in $\mathbf{z}$, the flow map is a homeomorphism (a [[Diffeomorphism]] for smooth $\mathbf{v}$), since trajectories exist, are unique, and cannot cross.
- **Topology is preserved**: as a homeomorphism of $\mathbb{R}^D$, it cannot change the topology of the support; e.g. it cannot exactly map a Gaussian to a distribution with disconnected support. Augmenting the state with extra dimensions (augmented neural ODEs) relaxes this ([[Normalizing Flow Expressivity]]).[^3]
- **Training**: by [[Maximum Likelihood Learning|maximum likelihood]], each step requires an ODE solve and trace estimates, which is expensive; [[Flow Matching|flow matching]] instead trains $\mathbf{v}_{\boldsymbol{\phi}}$ by regression without simulating the ODE or evaluating densities.
- The [[Probability Flow ODE]] of a [[Diffusion Model|diffusion model]] is a continuous normalizing flow, which is why diffusion models admit exact likelihoods and deterministic encodings.
- Current large image generators trained by flow matching (e.g. rectified-flow transformers) are continuous normalizing flows, i.e. invertible maps from noise to data.[^4]

[^1]: Supplementary notes provided by the creator; Chen, Rubanova, Bettencourt & Duvenaud (2018) in `REFERENCES.md`.
[^2]: Grathwohl, Chen, Bettencourt, Sutskever & Duvenaud (2019) in `REFERENCES.md`.
[^3]: Dupont, Doucet & Teh (2019) in `REFERENCES.md`.
[^4]: Esser et al. (2024) in `REFERENCES.md`.
