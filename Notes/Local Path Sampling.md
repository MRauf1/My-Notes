---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Local Path Sampling[^1]
> Every practical sampler builds a path one vertex at a time from one end, each vertex conditioned on the sub-path so far, so the path's density is a product of conditional densities, one per step.
> - Starting on a source and walking forward: particle tracing.
> - Starting on the sensor and walking backward: [[Path Tracing (Recursive Estimator)|path tracing]].
>
> A step arrives carrying a direction, draws a [[Free-Flight Distance Sampling|distance]] $\tau$ along it, and lands; the next direction $\omega$ is drawn on the way back out. What stops the step decides the measure it lands in:
> $$
> \begin{align}
> p_A(x_{n+1}) = p_\sigma(\omega)\,\mathcal{T}\,\frac{|\cos\theta_{n+1}|}{\tau^2} \quad \text{(surface: flight overshoots)}, \qquad p_V(x_{n+1}) = p_\sigma(\omega)\,\mathcal{T}\,\frac{\mu_t(x_{n+1})}{\tau^2} \quad \text{(volume: stops inside)}
> \end{align}
> $$

In the surface-only case, the flight always overshoots the medium, and $\mathcal{T} \equiv 1$.

# Properties
- Each vertex's density is used as the importance-sampling density $p$ in that step's [[Monte Carlo Estimator]] of the [[Generalized Path Integral (Surfaces and Volumes)|path integral]].
- Augmented at every vertex by [[Next-Event Estimation]], which connects directly to a source rather than only continuing the walk.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
