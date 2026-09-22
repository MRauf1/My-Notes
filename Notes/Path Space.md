---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Path Space[^1]
> A path is a tuple of vertices $\bar{x} = (x_0, \dots, x_N)$. Collecting the paths of each length and taking the union over lengths:
> $$
> \begin{align}
> \Omega_N := \mathcal{M}^{N+1}, \quad d\mu_N(\bar{x}) := \prod_{n=0}^N dA(x_n); \qquad \Omega := \bigcup_{N\geq 1}\Omega_N, \quad \mu(D) := \sum_{N\geq 1}\mu_N(D\cap\Omega_N)
> \end{align}
> $$

Paths of different lengths are simply measured separately — that is the whole content of the union, and it makes the abstract [[Walk Space Measure]] concrete.

# Properties
- Underlies the [[Path Integral (Light Transport)|path integral]] form of the [[Measurement Equation]].
- Generalized to include volume vertices by [[Generalized Path Integral (Surfaces and Volumes)]].

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
