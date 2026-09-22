---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Bidirectional Scattering Distribution Function (BSDF)[^1]
> The scattering kernel $f_s(x, \omega_i \to \omega)$ at a surface point $x$: among all light arriving from direction $\omega_i$, the fraction that leaves toward direction $\omega$.

# Properties
- Known/given in the [[Light Transport Equation]], in contrast to the unknown radiance $L$.
- Its volumetric analogue is the phase function $f_p$ of the [[Radiative Transfer Equation]].
- Sampled by [[BSDF Importance Sampling]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
