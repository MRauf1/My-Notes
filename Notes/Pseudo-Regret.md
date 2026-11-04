---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Pseudo-Regret[^1]
> For a [[Multi-Armed Bandit]] with arm means $\mu_i$ and $\mu^\star = \max_i \mu_i$, the pseudo-regret of a learner after $T$ rounds is
> $$
> \begin{align}
> \mathrm{Regret}_T = \sum_{t=1}^T (\mu^\star - \mu_{i_t})
> \end{align}
> $$
> where $i_t$ is the arm chosen in round $t$.

# Properties
- "Pseudo" because it compares *means* $\mu_{i_t}$, not the realized rewards $r_t$. It is still random, through the learner's choices $i_t$.
- Every round counts, so the learner must both explore (to find the best arm) and exploit (to stop paying $\mu^\star - \mu_{i_t}$ on worse arms): the [[Exploration-Exploitation Tradeoff]].
- Contrasts with [[Simple Regret]], where only the final recommendation counts.

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=2)
