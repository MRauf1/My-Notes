---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Optimal Policy
> A [[Policy]] $\pi^\star_M$ (or $\pi^\star$) that is stationary and deterministic, and simultaneously maximizes $V^\pi(s)$ for all $s \in \mathcal{S}$ and $Q^\pi(s,a)$ for all $s \in \mathcal{S}, a \in \mathcal{A}$. We write $V^\star := V^{\pi^\star}$ and $Q^\star := Q^{\pi^\star}$ as shorthand for the resulting optimal [[Value Function|value]] and [[Action-Value Function|action-value]] functions.

# Properties
- Such a policy always exists.
- $V^\star$ and $Q^\star$ satisfy the [[Bellman Optimality Equation]].
- Given $Q^\star$, $\pi^\star$ can be recovered as the [[Greedy Policy]] with respect to $Q^\star$: $\pi^\star = \pi_{Q^\star}$.
- For a [[Finite-Horizon Markov Decision Process]], the optimal policy is generally non-stationary, depending on both the state and the time step.
