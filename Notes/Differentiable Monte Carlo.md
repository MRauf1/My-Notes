---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Differentiable Monte Carlo[^1]
> Differentiable Monte Carlo estimates parameter gradients of Monte Carlo integrals,
> $$
> \begin{align}
> \nabla_\theta \int_{\Omega(\theta)} f(x, \theta)\,dx
> \end{align}
> $$
> where the integrand may be discontinuous in $x$ along boundaries that move with $\theta$, so that by the [[Reynolds Transport Theorem]] the gradient is an interior integral of $\partial_\theta f$ plus a boundary integral over the moving discontinuities.

# Types
- [[Reparameterization (Differentiable Monte Carlo)|Reparameterization]]: warp the coordinates so the discontinuities stop moving, turning the boundary term into an interior term that ordinary automatic differentiation can handle.
- [[Edge Sampling (Differentiable Monte Carlo)|Edge sampling]]: estimate the boundary term directly by placing samples on the moving discontinuities.

# Properties
- Naive automatic differentiation of a [[Monte Carlo Estimator]] computes only the interior term and is biased whenever discontinuities move with $\theta$.
- Faces the [[Five Obstacles to Differentiating Monte Carlo Estimators]].
- Its gradients are used as described in [[Three Uses of a Differentiable Simulator's Gradient]].

[^1]: Monte Carlo Methods — Q&A Overview
