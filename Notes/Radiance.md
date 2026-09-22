---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Radiance[^1]
> In a bounded region containing surfaces $\mathcal{M}$ where light travels in straight lines and changes direction only at scattering events (geometric optics), radiance $L(x,\omega)$ is the density of particle flow at point $x$ in direction $\omega$: power per unit area per unit solid angle.

$L$ is constant along a ray through empty space — this is what makes a ray $(x,\omega)$, rather than a point $x$, the natural primitive of light transport. This material assumes a steady state: sources are constant and the field has settled, so no time variable appears.

# Properties
- Governed by the [[Light Transport Equation]] on surfaces, and by the [[Radiative Transfer Equation]] in a scattering medium.
- Integrated against a sensor response to give the [[Measurement Equation|measured value]] that a detector reports.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
