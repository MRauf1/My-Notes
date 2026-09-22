---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Value Function
> For a [[Markov Decision Process]] $M$ and [[Policy]] $\pi$, the function $V^\pi_M: \mathcal{S} \to \mathbb{R}$ given by
> $$
> \begin{align}
> V^\pi_M(s) = \mathbb{E}\left[\sum_{t=1}^{\infty} \gamma^{t-1} r_t \mid \pi, s_1 = s\right]
> \end{align}
> $$
> the expected [[Discounted Return]] obtained by following $\pi$ starting at state $s$.

# Properties
- Bounded in $[0, R_{max}/(1-\gamma)]$, since the underlying [[Discounted Return]] is bounded in this range.
- May differ for different choices of $s_1$, for a fixed policy $\pi$.
- Closely related to the [[Action-Value Function]] $Q^\pi_M(s,a)$, which additionally conditions on the first action taken.
- The dependence on $M$ is often left implicit when clear from context.
- Satisfies the [[Bellman Equation (Policy Evaluation)|Bellman equation]], and can be computed for finite $\mathcal{S}$ via [[Policy Evaluation]].
- The optimal value function $V^\star$ (see [[Optimal Policy]]) satisfies the [[Bellman Optimality Equation]].
