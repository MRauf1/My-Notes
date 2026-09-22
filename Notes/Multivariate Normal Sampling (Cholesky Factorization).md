---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Multivariate Normal Sampling (Cholesky Factorization)[^1]
> To sample $\mathcal{N}(\mu, \Sigma)$: factor $AA^\top = \Sigma$ via [[Cholesky Decomposition]], draw a vector $z$ of independent standard normals componentwise (e.g. via the [[Box-Muller Transform]]), and return $\mu + Az$.

# Properties
- Used for MALA/HMC proposals and every Gaussian primitive in Monte Carlo rendering.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
