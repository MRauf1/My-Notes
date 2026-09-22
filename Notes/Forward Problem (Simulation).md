---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Forward Problem (Simulation)[^1]
> Given parameters $\theta$ (scene geometry, materials, medium coefficients, domain shape), a forward Monte Carlo problem is to simulate
> $$
> \begin{align}
> y = F(\theta)
> \end{align}
> $$
> where $F$ is a stochastic simulator (light transport, particle transport, a random walk in a domain) and $y$ is its output (an image, a detector reading, a solution field).

$F$ has no closed-form expression. Instead, it is an expectation that can only be estimated: $F(\theta) = \mathbb{E}[\langle F(\theta) \rangle]$, where $\langle F(\theta) \rangle$ is a [[Monte Carlo Estimator]] of it.

# Properties
- Feeds the [[Inverse Problem (Analysis by Synthesis)]], which recovers $\theta$ by simulating forward repeatedly and adjusting $\theta$ until $F(\theta)$ matches a measurement.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
