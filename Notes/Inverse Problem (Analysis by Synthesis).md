---
tags:
  - computer_science
  - monte_carlo_methods
---

# Definition
> [!info] Inverse Problem (Analysis by Synthesis)[^1]
> Given measurements $y^\star$, recover the parameters $\theta$ that produced them by minimizing
> $$
> \begin{align}
> \theta^\star = \arg\min_\theta \mathcal{L}(\theta), \qquad \mathcal{L}(\theta) = d\big(y^\star, F(\theta)\big) + R(\theta)
> \end{align}
> $$
> where $F$ is the [[Forward Problem (Simulation)|forward simulator]], $d$ is a data term comparing the simulation to the measurement, and $R(\theta)$ is a regularization term.

$R(\theta)$ penalizes undesirable solutions (e.g. to enforce smoothness) and helps make the otherwise ill-posed inverse problem well-posed. Under a Bayesian reading of $\mathcal{L}$ as a negative log-posterior, $R(\theta)$ plays the role of a negative log-prior, but $R$ need not correspond to any actual prior distribution in general — it can equally be a purely computational regularizer (e.g. an $\ell_2$ or total-variation penalty) chosen only to stabilize the optimization.

Analysis by synthesis: rather than inverting the physics of $F$ directly, $\theta$ is found by simulating forward repeatedly and adjusting $\theta$ until the simulation matches the measurement. This hinges entirely on one object: $\partial F/\partial\theta$, the derivative of a (Monte Carlo) simulator.

# Properties
- Solved by [[Gradient Descent]] on $\mathcal{L}(\theta)$, which is one of the [[Three Uses of a Differentiable Simulator's Gradient|three uses]] of the simulator's gradient.

[^1]: Differentiable Monte Carlo — Course Lecture Notes, University of Illinois (Fall 2026)
