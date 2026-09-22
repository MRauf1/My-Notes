---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Path Integral (Light Transport)[^1]
> The [[Measurement Equation]] as a single integral over [[Path Space]]:
> $$
> \begin{align}
> I = \int_\Omega f(\bar{x})\,d\mu(\bar{x})
> \end{align}
> $$
> $$
> \begin{align}
> f(\bar{x}) = L_e(x_0\to x_1)\left(\prod_{n=1}^{N-1} f_s(x_{n-1}\to x_n\to x_{n+1})\right) W_e(x_{N-1}\to x_N)\prod_{n=1}^N G(x_{n-1}\leftrightarrow x_n)
> \end{align}
> $$

$f$ is the measurement contribution function: a product over what happens at each vertex (emission, scattering, sensor response) times what happens between consecutive vertices (the [[Geometric Term (Light Transport)|geometric term]]). Paths whose endpoints are not on a source and a sensor contribute nothing, since $L_e$ or $W_e$ is zero there; interior vertices may land anywhere, including on a source.

# Properties
- Estimated by a [[Monte Carlo Estimator]] built from a [[Path Space|path-space]] sampling strategy, e.g. [[Path Tracing (Recursive Estimator)|path tracing]], particle tracing, or [[Bidirectional Path Tracing]].
- Generalizes to [[Generalized Path Integral (Surfaces and Volumes)]] once vertices may also lie in a scattering medium.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
