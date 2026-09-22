---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Dual Linear Program (Markov Decision Process)
> The dual of the [[Primal Linear Program (Markov Decision Process)|primal LP]]:
> $$
> \begin{align}
> \max_{d \in \mathbb{R}^{\mathcal{S}\times\mathcal{A}}, \, d \geq 0} \; & d^\top R \\
> \text{s.t.} \; & \left[\sum_{a\in\mathcal{A}} d(s,a)\right]_{s\in\mathcal{S}} = \gamma P^\top d + (1-\gamma) d_0
> \end{align}
> $$
> where $P$ is the matrix form of the [[Transition Function]] and $d_0$ the initial state distribution. The constraint is called the [[Bellman Flow Equations]].

# Properties
- The decision variable $d$ can be interpreted as the [[State-Action Occupancy|discounted state-action occupancy]] of a stationary (possibly stochastic) policy starting from $d_0$, so $d^\top R$ is that policy's expected return — hence the objective is maximized, unlike the primal.
- The feasible region is exactly the set of discounted state-action occupancies of all stationary policies.
- Given any feasible $d$, the inducing policy can be recovered as $\pi(a|s) = d(s,a) / \sum_{a'\in\mathcal{A}} d(s,a')$; applied to the optimal solution, this recovers $\pi^\star$.
