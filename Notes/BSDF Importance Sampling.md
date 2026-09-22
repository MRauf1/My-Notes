---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] BSDF Importance Sampling[^1]
> Choices for the density $p(\omega_i)$ used to draw a direction at a [[Path Tracing (Recursive Estimator)|path-tracing]] vertex:
>
> | Choice | Density | Estimator picks up |
> |---|---|---|
> | Uniform on the hemisphere | $1/(2\pi)$ | $2\pi f_s \cos\theta_i$ |
> | Proportional to $\cos\theta_i$ | $\cos\theta_i/\pi$ | $\pi f_s$ |
> | Proportional to $f_s\cos\theta_i$ | — | a constant, if invertible |

The cosine-weighted case is sampled by inversion: $\mathbb{P}[\theta < \alpha] = \int_0^\alpha\int_0^{2\pi} \frac{\cos\theta}{\pi}\sin\theta\,d\phi\,d\theta = \sin^2\alpha$, so $\theta = \arcsin\sqrt{\xi}$ — or, skipping the trigonometry, $z = \sqrt{1-\xi}$ directly. As with any sampler, uniform in a parameterization is not uniform in the measure that matters: the $\sin\theta$ factor is the Jacobian of the [[Solid Angle Measure|solid-angle measure]] in spherical coordinates.

# Properties
- An application of [[Inverse Transform Sampling]] and of choosing $p$ close to the [[Optimal Importance Sampling Distribution]] for the [[Bidirectional Scattering Distribution Function|BSDF]]-weighted integrand.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
