---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Measurement Equation[^1]
> A detector reports one number: a scalar integral of the [[Radiance]] field over the points and directions it is sensitive to,
> $$
> \begin{align}
> I = \int_\mathcal{M} \int_{\mathbb{S}^2} W_e(x,\omega)\, L(x,\omega)\, |\cos\theta|\, d\sigma(\omega)\, dA(x)
> \end{align}
> $$

$W_e$ is the known sensor response — which points and directions the detector is sensitive to, and how much; it is usually zero almost everywhere. An image is a few million such numbers, one per pixel; a tomographic dataset is a few thousand. Since $L$ is a field on a 4D domain that is rarely wanted directly, the practical task is not to solve for $L$ but to estimate $I$.

# Properties
- Rewritten in [[Three-Point Form of the Light Transport Equation|three-point form]] in terms of surface points alone.
- Estimated by the [[Path Integral (Light Transport)|path integral]] over [[Path Space]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
