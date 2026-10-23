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
> \sqrt{-2\log \xi_1}\,\cos(2\pi\xi_2) \quad \text{and} \quad \sqrt{-2\log \xi_1}\,\sin(2\pi\xi_2)
> \end{align}
> $$
> are independent samples from $\mathcal{N}(0,1)$.

# Properties
- Feeds [[Multivariate Normal Sampling (Cholesky Factorization)]], which draws a vector of independent standard normals componentwise before applying a Cholesky factor.
- An alternative to [[Inverse Transform Sampling]] for the normal distribution, whose CDF has no closed-form inverse.
- Usually outperformed in speed by the [[Ziggurat Algorithm]].
- Owen's formulation:[^2] for independent $U_1, U_2 \sim \mathcal{U}(0,1)$, $Z_1 = \sqrt{-2\log U_1}\cos(2\pi U_2)$ and $Z_2 = \sqrt{-2\log U_1}\sin(2\pi U_2)$ are independent $\mathcal{N}(0,1)$; one of the best-known [[Non-Uniform Random Variate Generation|transformation methods]] that consume several uniforms.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
[^2]: [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=15&annotation=STBJ76KS); [Owen, Monte Carlo Theory, Methods and Examples](zotero://open-pdf/library/items/7EZQYHPW?page=7&annotation=EFHT2V5D)
