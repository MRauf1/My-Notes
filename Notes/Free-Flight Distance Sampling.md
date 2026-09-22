---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Free-Flight Distance Sampling[^1]
> To draw a point $y = x - \tau\omega$ on a ray inside a medium, the free-flight distance $\tau$ has density
> $$
> \begin{align}
> p_\lambda(\tau) = \lambda(\tau)\exp\left(-\int_0^\tau \lambda(u)\,du\right), \qquad \lambda(\tau) = \mu_t(x-\tau\omega)
> \end{align}
> $$

Homogeneous medium ($\lambda$ constant): $p_\lambda$ is the exponential distribution, sampled by [[Inverse Transform Sampling|inversion]] as $\tau = -\log(1-\xi)/\lambda$.

Heterogeneous medium: no closed form. Two answers occupy different points of the bias/discretization tradeoff:

| | Ray marching | Delta tracking (Woodcock 1965) |
|---|---|---|
| Idea | discretize the CDF | fictitious collisions up to a majorant $\bar\lambda$ |
| Bias | biased, consistent as the step shrinks | unbiased, discretization-free |
| Gives $p_\lambda(\tau)$? | yes | no |

This is [[Bias and Consistency of an Estimator|biased-vs-consistent estimation]] once more: a nameable bias, against a density that cannot be written down.

# Properties
- Feeds [[Local Path Sampling]] in a volume, where a step's landing measure (area vs. volume) depends on whether the flight overshoots the medium or stops inside it.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
