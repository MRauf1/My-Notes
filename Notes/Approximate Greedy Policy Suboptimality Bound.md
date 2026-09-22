---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Approximate Greedy Policy Suboptimality Bound
> For any $f \in \mathbb{R}^{|\mathcal{S}\times\mathcal{A}|}$, the [[Greedy Policy]] $\pi_f$ satisfies
> $$
> \begin{align}
> \|V^\star - V^{\pi_f}\|_\infty \leq \frac{2\|f - Q^\star\|_\infty}{1-\gamma}
> \end{align}
> $$

# Properties
- Bounds the suboptimality (or loss) of acting greedily with respect to an approximate Q-value function $f$, rather than the true $Q^\star$.
- Applied to $f = Q^{\star,H}$ from [[Value Iteration]], together with its convergence rate, bounds the suboptimality of the resulting greedy policy.
