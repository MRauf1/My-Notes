---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Planning
> The problem of computing the [[Optimal Policy]] $\pi^\star_M$ given the full specification of a [[Markov Decision Process]] $M = (\mathcal{S}, \mathcal{A}, P, R, \gamma)$.

# Properties
- Classical planning algorithms (e.g. [[Policy Iteration]], [[Value Iteration]], [[Linear Programming (Markov Decision Process)|linear programming]]) compute $Q^\star$, from which $\pi^\star$ follows as its [[Greedy Policy]].
- Of these, [[Value Iteration]] is arguably the most commonly used in practice: its simple, incremental update generalizes naturally to large or continuous state-action spaces via function approximation, and it underlies many modern sample-based RL algorithms (e.g. Q-learning, DQN). [[Policy Iteration]] is also widely used, particularly when the analytical [[Policy Evaluation]] step is cheap. [[Linear Programming (Markov Decision Process)|Linear programming]] is theoretically elegant (e.g. useful for analyzing offline RL and imitation learning via the dual's occupancy interpretation) but rarely used computationally, since its variable and constraint counts scale with $|\mathcal{S}|\times|\mathcal{A}|$.
