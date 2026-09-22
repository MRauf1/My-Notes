---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Reverse-Mode Automatic Differentiation for High-Dimensional Gradients[^1]
> When a parameter $\theta$ has $10^4$–$10^7$ dimensions, reverse-mode automatic differentiation computes all of its partial derivatives for a small constant multiple of the cost of one forward evaluation, which is why it is preferred over alternatives whose cost or variance scales with the dimension of $\theta$:
> - [[Finite Difference Method|Finite differences]]: one forward solve per parameter; when each solve is itself a noisy Monte Carlo simulation, the difference quotient subtracts two noisy numbers and divides by a small step size.
> - [[Zeroth-Order Optimization|Zeroth-order]] / [[Evolution Strategy|evolution-strategy]] methods: need no adjoint, but gradient-estimate variance grows with dimension.
> - Grid or random search: infeasible once $\theta$ has more than a handful of dimensions.

# Properties
- Feeds the [[Three Uses of a Differentiable Simulator's Gradient|three downstream uses]] of a differentiable simulator's gradient.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
