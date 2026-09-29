---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Edge Sampling (Differentiable Monte Carlo)[^1]
> Estimate the boundary term of the [[Reynolds Transport Theorem]] by Monte Carlo sampling points $x$ directly on the moving discontinuity curves $\Gamma(\theta)$ of the integrand (e.g. silhouette edges in rendering):
> $$
> \begin{align}
> \int_{\Gamma(\theta)} \Delta f(x)\,\big(v(x)\cdot n(x)\big)\,ds \approx \frac{1}{N}\sum_{i=1}^N \frac{\Delta f(x_i)\,\big(v(x_i)\cdot n(x_i)\big)}{p_\Gamma(x_i)}, \qquad x_i \sim p_\Gamma
> \end{align}
> $$
> where $\Delta f$ is the jump of $f$ across $\Gamma$, $v$ the boundary's velocity with respect to $\theta$, $n$ its unit normal, and $p_\Gamma$ a density on $\Gamma$. The interior term is estimated separately by ordinary automatic differentiation.

# Properties
- Captures the discontinuity contribution that naive automatic differentiation misses entirely.
- Requires explicitly finding and sampling the discontinuities, which is costly in complex scenes; generalized to light transport as path-space boundary integrals.
- The counterpart to [[Reparameterization (Differentiable Monte Carlo)|reparameterization]] in [[Differentiable Monte Carlo]].

[^1]: Monte Carlo Methods — Q&A Overview
