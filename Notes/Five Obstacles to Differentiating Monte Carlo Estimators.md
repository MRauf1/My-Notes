---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Five Obstacles to Differentiating Monte Carlo Estimators[^1]
> Computing $\partial F/\partial\theta$ for a Monte Carlo simulator $F$ is hard for five reasons:
> 1. You are differentiating an expectation, not a function — the [[Interchange of Differentiation and Expectation|interchange]] of $d/d\theta$ and $\mathbb{E}[\cdot]$ is not free.
> 2. The integrand is discontinuous in $\theta$ (visibility, interfaces, level sets).
> 3. The domain of integration moves with $\theta$, requiring the [[Reynolds Transport Theorem|Leibniz/Reynolds transport rule]] rather than the chain rule.
> 4. Memory: reverse-mode differentiation tapes the whole computation, but a random walk has unbounded length and millions are run at once.
> 5. Variance: the derivative integrand is not the original integrand — it has a different sign structure and support, so samplers tuned for the forward problem are wrong for the derivative.

# Properties
- Obstacles (1)–(3) concern differentiating the forward model itself; obstacles (4)–(5) concern doing so efficiently within a [[Monte Carlo Estimator|Monte Carlo estimator]]'s sampling and memory constraints.
- Obstacle (2) is concrete in light transport as the visibility term $V$ of the [[Geometric Term (Light Transport)|geometric term]]: the one factor of a path's contribution that is discontinuous rather than smooth in the vertex positions.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
