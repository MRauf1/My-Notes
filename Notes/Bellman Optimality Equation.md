---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Optimality Equation
> For a [[Markov Decision Process]], the [[Optimal Policy|optimal]] value functions $V^\star$ and $Q^\star$ satisfy, for all $s \in \mathcal{S}, a \in \mathcal{A}$:
> $$
> \begin{align}
> V^\star(s) &= \max_{a\in\mathcal{A}} Q^\star(s,a) \\
> Q^\star(s,a) &= R(s,a) + \gamma\,\mathbb{E}_{s'\sim P(s,a)}[V^\star(s')]
> \end{align}
> $$

# Properties
- Analogous to the [[Bellman Equation (Policy Evaluation)|Bellman equation for policy evaluation]], but with the expectation over actions taken by a fixed policy replaced by a maximization over actions.
- Can be written concisely as $Q^\star = \mathcal{T} Q^\star$ using the [[Bellman Optimality Operator]] $\mathcal{T}$, i.e. $Q^\star$ is the fixed point of $\mathcal{T}$.
