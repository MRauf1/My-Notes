---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] $H$-Step Truncated Value Function
> For a [[Markov Decision Process]] and stationary [[Policy]] $\pi$, the expected finite-horizon return over the first $H$ steps:
> $$
> \begin{align}
> V^{\pi,H}(s) = \mathbb{E}\left[\sum_{t=1}^{H} \gamma^{t-1} r_t \mid \pi, s_1 = s\right]
> \end{align}
> $$

# Properties
- $V^{\star,H}(s) := \max_\pi V^{\pi,H}(s)$ is within $\gamma^H R_{max}/(1-\gamma)$ of the true [[Value Function|value]] $V^\star(s)$, for every $s \in \mathcal{S}$: $V^\star(s) - \gamma^H R_{max}/(1-\gamma) \leq V^{\star,H}(s) \leq V^\star(s)$.
- The optimal $H$-step policy may need to be non-stationary, unlike the stationary [[Optimal Policy]] of the infinite-horizon setting.
- Provides an alternative (finite-horizon) derivation of the convergence rate of [[Value Iteration]].
