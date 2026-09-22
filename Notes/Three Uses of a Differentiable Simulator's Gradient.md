---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Three Uses of a Differentiable Simulator's Gradient[^1]
> A single gradient object, $\partial(\text{simulation})/\partial\theta$, feeds three distinct downstream uses:
> - Differentiating a forward model: $\partial(\text{simulation})/\partial\theta$
> - Descending an objective: $\nabla_\theta \mathcal{L}$, via [[Gradient Descent]] on the [[Inverse Problem (Analysis by Synthesis)|inverse problem]]
> - Sampling a distribution: $\nabla_x \log \pi(x)$, the score function of a target distribution $\pi$

The gradient of the log-density, $\nabla_x \log\pi(x)$, points toward higher-probability regions of $\pi$ without requiring $\pi$'s normalizing constant, which is often intractable. Markov-chain samplers built from it — e.g. Langevin-dynamics-style updates $x_{t+1} = x_t + \frac{\epsilon}{2}\nabla_x\log\pi(x_t) + \sqrt{\epsilon}\,\xi_t$ — use this gradient to steer proposals toward the high-density regions of $\pi \propto \exp(-\mathcal{L})$ far more efficiently than proposals that ignore it. This is precisely why minimizing $\mathcal{L}$ and sampling $\pi \propto \exp(-\mathcal{L})$ are two things done with the same gradient estimator.

# Properties
- Computed once via [[Reverse-Mode Automatic Differentiation for High-Dimensional Gradients|reverse-mode automatic differentiation]] and reused across all three uses.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
