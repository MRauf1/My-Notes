---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Bellman Equation (Policy Evaluation)[^1]
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
- For a [[Stochastic Policy]] $\pi: \mathcal{S} \to \Delta(\mathcal{A})$, writing $\pi(a \mid s)$ for the probability $\pi(s)$ assigns to $a$, substituting $Q^\pi$ into $V^\pi$ gives
  $$
  \begin{align}
  V^\pi(s) = \sum_{a \in \mathcal{A}} \pi(a \mid s) \Big[ R(s,a) + \gamma \sum_{s' \in \mathcal{S}} P(s' \mid s, a) \, V^\pi(s') \Big].
  \end{align}
  $$
  For a [[Deterministic Policy]], $\pi(\cdot \mid s)$ is a point mass at $\pi(s)$ and the outer sum collapses to $V^\pi(s) = R(s,\pi(s)) + \gamma \sum_{s'} P(s' \mid s, \pi(s)) \, V^\pi(s')$.
- The expectation defining $V^\pi(s)$ is a single expectation under the law of the [[Trajectory]] induced by $\pi$ and $P$ with $s_1 = s$ fixed (conditioning on $\pi$ selects the measure; $\pi$ is not a random variable). The equation follows by the [[Law of Total Expectation]], conditioning first on $a_1 \sim \pi(s)$ and then on $s_2 \sim P(s, a_1)$.
- Admits a matrix-vector form and a closed-form analytical solution when solving [[Policy Evaluation]].
- Equivalently, $Q^\pi$ is the fixed point of the [[Bellman Evaluation Operator]] $\mathcal{T}^\pi$: $Q^\pi = \mathcal{T}^\pi Q^\pi$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=2)
