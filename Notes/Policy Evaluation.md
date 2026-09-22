---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Policy Evaluation
> The problem of computing the [[Value Function]] $V^\pi$ of a fixed [[Policy]] $\pi$ in a [[Markov Decision Process]] $M = (\mathcal{S}, \mathcal{A}, P, R, \gamma)$.

# Properties
- Since $\mathcal{S}$ is finite, fixing an order of states lets $V^\pi$ be treated as a vector in $\mathbb{R}^{|\mathcal{S}|}$, admitting a matrix-vector form of the [[Bellman Equation (Policy Evaluation)|Bellman equation]]:
$$
\begin{align}
V^\pi = R^\pi + \gamma P^\pi V^\pi
\end{align}
$$
using the policy's [[Transition Matrix (Markov Decision Process)|transition matrix]] $P^\pi$ and reward vector $R^\pi$.
- $(I_{|\mathcal{S}|} - \gamma P^\pi)$ is always invertible, giving $V^\pi$ a closed-form analytical solution:
$$
\begin{align}
V^\pi = (I_{|\mathcal{S}|} - \gamma P^\pi)^{-1} R^\pi
\end{align}
$$
- When the reward function depends only on the current state ($R(s,a) = R(s)$), $R^\pi$ is independent of $\pi$, and the value of a policy is linear in rewards, with the rows of $(I_{|\mathcal{S}|} - \gamma P^\pi)^{-1}$ giving the linear coefficients — the [[Discounted State Occupancy|discounted state occupancy]].
- The policy evaluation step of [[Policy Iteration]] computes $Q^\pi$ this way before taking the [[Greedy Policy]] for the next iteration.
