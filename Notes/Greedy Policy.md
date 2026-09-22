---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Greedy Policy
> For an [[Action-Value Function]]-shaped $f: \mathcal{S} \times \mathcal{A} \to \mathbb{R}$, the deterministic [[Policy]] $\pi_f$ obtained by choosing actions greedily with respect to $f$ (with arbitrary tie-breaking):
> $$
> \begin{align}
> \pi_f(s) = \arg\max_{a\in\mathcal{A}} f(s,a), \quad \forall s \in \mathcal{S}
> \end{align}
> $$

# Properties
- Applying this procedure to the optimal action-value function $Q^\star$ recovers the [[Optimal Policy]]: $\pi^\star = \pi_{Q^\star}$.
- The policy improvement step of [[Policy Iteration]] takes the greedy policy of the previous iterate's Q-value function: $\pi_k = \pi_{Q^{\pi_{k-1}}}$.
