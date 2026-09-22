---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Equation (Policy Evaluation)
> For a [[Markov Decision Process]] $M$ and [[Policy]] $\pi$, the [[Value Function]] $V^\pi$ and [[Action-Value Function]] $Q^\pi$ satisfy, for all $s \in \mathcal{S}, a \in \mathcal{A}$:
> $$
> \begin{align}
> V^\pi(s) &= Q^\pi(s, \pi(s)) \\
> Q^\pi(s, a) &= R(s,a) + \gamma \, \mathbb{E}_{s' \sim P(s,a)}[V^\pi(s')]
> \end{align}
> $$
> For a stochastic policy, $Q^\pi(s,\pi(s))$ is shorthand for $\mathbb{E}_{a \sim \pi(s)}[Q^\pi(s,a)]$.

# Properties
- Follows from the principles of dynamic programming: expresses the value of a state (or state-action pair) recursively in terms of the values of successor states.
- Admits a matrix-vector form and a closed-form analytical solution when solving [[Policy Evaluation]].
