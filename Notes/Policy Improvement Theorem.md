---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Policy Improvement Theorem
> In [[Policy Iteration]], $V^{\pi_k}(s) \geq V^{\pi_{k-1}}(s)$ holds for all $k \geq 1$ and $s \in \mathcal{S}$, and the improvement is strictly positive in at least one state until $\pi^\star$ is found.

# Properties
- Follows from the [[Performance Difference Lemma]]: $V^{\pi_k}(s) - V^{\pi_{k-1}}(s)$ decomposes into a sum of nonnegative [[Advantage Function|advantage]] terms, nonnegative because $\pi_k$ is the [[Greedy Policy]] of $\pi_{k-1}$'s Q-value function.
