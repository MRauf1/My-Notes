---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Discounted Return
> In a [[Markov Decision Process]], the discounted sum of rewards along a [[Trajectory]], $\sum_{t=1}^{\infty} \gamma^{t-1} r_t$, where $\gamma$ is the [[Discount Factor]]. The agent's goal is to choose a [[Policy]] $\pi$ maximizing its expectation, $\mathbb{E}\left[\sum_{t=1}^{\infty} \gamma^{t-1} r_t \mid \pi, s_1\right]$, called the value.

# Properties
- Since $r_t \in [0, R_{max}]$, the discounted return is bounded:
$$
\begin{align}
0 \leq \sum_{t=1}^{\infty} \gamma^{t-1} r_t \leq \sum_{t=1}^{\infty} \gamma^{t-1} R_{max} = \frac{R_{max}}{1-\gamma}
\end{align}
$$
along any actual trajectory, and so is its expectation of any form.
- The [[Value Function]] $V^\pi_M(s)$ is the expected discounted return conditioned on starting at state $s$ and following $\pi$; the [[Action-Value Function]] $Q^\pi_M(s,a)$ additionally conditions on the first action $a$.
