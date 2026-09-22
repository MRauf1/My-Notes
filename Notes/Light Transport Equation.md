---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Light Transport Equation (Rendering Equation)[^1]
> $$
> \begin{align}
> L(x,\omega) = \underbrace{L_e(x,\omega)}_{\text{emitted}} + \int_{\mathbb{S}^2} L(y,-\omega_i)\,f_s(x,\omega_i\to\omega)\,|\cos\theta_i|\,d\sigma(\omega_i)
> \end{align}
> $$
> where $y = \mathrm{rayTrace}(x,\omega_i)$ is the first surface point seen from $x$ along $\omega_i$.

$L_e$ is the known emitted [[Radiance]]. $f_s$ is the known [[Bidirectional Scattering Distribution Function|scattering kernel (BSDF)]] at $x$. $L$ is the unknown, and it appears on both sides of the equation. $d\sigma$ is the [[Solid Angle Measure]] on $\mathbb{S}^2$; $L$ is a density against this measure, which is what "per unit solid angle" means.

# Types
- A special case of the general [[Radiative Transfer Equation]]: restricted to surfaces with no participating medium, so that radiance is piecewise-constant between discrete scattering events instead of changing continuously along the ray.

# Properties
- Solved by the recursive [[Path Tracing (Recursive Estimator)|Monte Carlo estimator]].
- Rewritten in [[Three-Point Form of the Light Transport Equation|three-point form]] by absorbing the direction-to-point change of measure into a [[Geometric Term (Light Transport)|geometric term]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
