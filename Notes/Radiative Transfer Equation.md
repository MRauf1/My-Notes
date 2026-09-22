---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Radiative Transfer Equation (RTE)[^1]
> $$
> \begin{align}
> \nabla_\omega L(x,\omega) = \underbrace{\mu_s(x)\int_{\mathbb{S}^2} L(x,\omega_i)\,f_p(x,\omega_i\to\omega)\,d\sigma(\omega_i)}_{\text{in-scattering}} - \mu_t(x)L(x,\omega) + \mu_a(x)L_e(x,\omega)
> \end{align}
> $$
> where $\nabla_\omega L$ is the directional derivative of [[Radiance]] $L$ along $\omega$ — zero in empty space.

| Coefficient | Meaning |
|---|---|
| $\mu_t = \mu_s + \mu_a$ | how often a particle interacts at all |
| $\mu_s, \mu_a$ | how those interactions split between scattering and absorption |
| $f_p$ | the phase function — the scattering kernel, in a volume |
| $\alpha := \mu_s/\mu_t \in [0,1]$ | single-scattering albedo |

A first-order integro-differential equation governing the interior of a scattering medium; radiance entering the boundary is the Dirichlet data.

# Types
- [[Light Transport Equation]] — the special case restricted to surfaces with no participating medium, where radiance is piecewise-constant between discrete scattering events rather than varying continuously along a ray.

# Properties
- Solved along a single ray by its [[Integral Form of the Radiative Transfer Equation|integral form]].
- $f_p$, the phase function, is the volumetric analogue of the [[Bidirectional Scattering Distribution Function|BSDF]] $f_s$.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
