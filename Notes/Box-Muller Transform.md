---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Box-Muller Transform[^1]
> Since inverting the standard normal CDF requires $\mathrm{erf}^{-1}$, the Box-Muller transform avoids it: from $\xi_1, \xi_2 \sim \mathcal{U}[0,1]$, both
> $$
> \begin{align}
> \sqrt{-\log \xi_1}\,\cos(2\pi\xi_2) \quad \text{and} \quad \sqrt{-\log \xi_1}\,\sin(2\pi\xi_2)
> \end{align}
> $$
> are independent samples from $\mathcal{N}(0,1)$.

# Properties
- Feeds [[Multivariate Normal Sampling (Cholesky Factorization)]], which draws a vector of independent standard normals componentwise before applying a Cholesky factor.
- An alternative to [[Inverse Transform Sampling]] for the normal distribution, whose CDF has no closed-form inverse.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
