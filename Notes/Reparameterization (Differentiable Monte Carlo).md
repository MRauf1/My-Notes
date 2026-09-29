---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Reparameterization (Differentiable Monte Carlo)[^1]
> Choose a $\theta$-dependent [[Change of Variables|change of variables]] $x = T_\theta(y)$ from a fixed reference domain such that the discontinuities of $f(\cdot, \theta)$ are mapped to fixed locations in $y$. Then
> $$
> \begin{align}
> \nabla_\theta \int_{\Omega(\theta)} f(x, \theta)\,dx = \int_{\Omega_0} \nabla_\theta\Big[f\big(T_\theta(y), \theta\big)\,\big|\det J_{T_\theta}(y)\big|\Big]\,dy
> \end{align}
> $$
> where $J_{T_\theta}$ is the [[Jacobian Matrix]] of $T_\theta$.

Since the reparameterized integrand's discontinuities no longer move, the [[Reynolds Transport Theorem|boundary term]] vanishes and standard automatic differentiation of the interior integrand gives an unbiased gradient.

# Properties
- Avoids explicitly locating discontinuities, but requires a warp $T_\theta$ that tracks every moving boundary (in the continuum-mechanics sense, following material points, hence the "material" view); in practice the warp is often only approximated.
- The counterpart to [[Edge Sampling (Differentiable Monte Carlo)|edge sampling]] in [[Differentiable Monte Carlo]].

[^1]: Monte Carlo Methods — Q&A Overview
