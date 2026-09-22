---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Action-Value Function (Q-Value Function)
> For a [[Markov Decision Process]] $M$ and [[Policy]] $\pi$, the function $Q^\pi_M: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$ given by
> $$
> \begin{align}
> Q^\pi_M(s, a) = \mathbb{E}\left[\sum_{t=1}^{\infty} \gamma^{t-1} r_t \mid \pi, s_1 = s, a_1 = a\right]
> \end{align}
> $$
> the expected [[Discounted Return]] obtained by starting at state $s$, taking action $a$, and following $\pi$ thereafter.

# Properties
- Bounded in $[0, R_{max}/(1-\gamma)]$, since the underlying [[Discounted Return]] is bounded in this range.
- Generalizes the [[Value Function]]: $V^\pi_M(s) = Q^\pi_M(s, \pi(s))$ for a [[Deterministic Policy]] (or the corresponding expectation over $a \sim \pi(s)$ for a [[Stochastic Policy]]).
- The dependence on $M$ is often left implicit when clear from context.
- Together with $V^\pi_M$, satisfies the [[Bellman Equation (Policy Evaluation)|Bellman equation]]: $Q^\pi_M(s,a) = R(s,a) + \gamma\,\mathbb{E}_{s' \sim P(s,a)}[V^\pi_M(s')]$.
