---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Stratified Sampling[^1]
> Split $\Omega$ into $M$ equal-measure strata and take one sample in each. The estimator's variance decomposes as
> $$
> \begin{align}
> \sigma^2 = \underbrace{\mathbb{E}_j[\sigma_j^2]}_{\text{within strata}} + \underbrace{\mathrm{Var}_j[\mu_j]}_{\text{between strata}}
> \end{align}
> $$
> where $\sigma_j^2$ and $\mu_j$ are the variance and mean within stratum $j$. Stratifying removes the between-strata term entirely.

# Properties
- Variance never increases relative to plain [[Monte Carlo Estimator|Monte Carlo]] sampling — a rare unconditional guarantee.
- Improves [[Monte Carlo Estimator Efficiency|efficiency]] whenever the between-strata term is non-negligible, i.e. when the integrand's mean varies across the domain.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
