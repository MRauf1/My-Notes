---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Zero-Density Bias (Importance Sampling)[^1]
> A [[Monte Carlo Estimator]] requires $f(x) \neq 0 \implies p(x) > 0$. Violating this does not make the estimator noisy — it makes it biased, silently, by exactly the integral of $f$ over the region never sampled.

Common causes:
- A sampler built from one factor of $f$, blind to a second factor that spikes elsewhere.
- A cap on the length of a random walk: everything past the cap has density zero.
- A sampler tuned for one integrand, reused on another whose support is larger — this is the cause that keeps recurring in practice, because the reuse is never announced.

# Properties
- Unlike [[Monte Carlo Estimator Variance|variance]], this bias does not shrink as $N \to \infty$ and does not show up as visible noise in a convergence plot.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
