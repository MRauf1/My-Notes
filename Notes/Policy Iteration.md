---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Policy Iteration
> An algorithm for [[Planning]] that starts from an arbitrary policy $\pi_0$ and repeats, for $k = 1, 2, \dots$:
> $$
> \begin{align}
> \pi_k = \pi_{Q^{\pi_{k-1}}}
> \end{align}
> $$
> i.e., computing the [[Action-Value Function|Q-value function]] of $\pi_{k-1}$ (policy evaluation, e.g. via the analytical form from [[Policy Evaluation]]), then taking its [[Greedy Policy|greedy policy]] as $\pi_k$ (policy improvement).

# Properties
- Terminates when $Q^{\pi_k} = Q^{\pi_{k-1}}$.
- Since only stationary deterministic policies are searched over, and a distinct policy is found every iteration, the algorithm is guaranteed to terminate in at most $|\mathcal{A}|^{|\mathcal{S}|}$ iterations.
- Guaranteed to improve monotonically until $\pi^\star$ is found (see [[Policy Improvement Theorem]]).
- Its worst-case iteration complexity is not fully understood, but it enjoys exponential convergence to an approximate solution (see [[Policy Iteration Exponential Convergence]]).
