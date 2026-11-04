---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Simple Regret[^1]
> For a [[Multi-Armed Bandit]], if $\hat{i}$ is the arm the learner picks after $T$ rounds of interaction, its simple regret is
> $$
> \begin{align}
> \mu^\star - \mu_{\hat{i}}.
> \end{align}
> $$

# Properties
- Poses the **pure exploration** challenge: only the final guess matters, and the rewards collected during the $T$ rounds do not, unlike [[Pseudo-Regret]].
- It is zero exactly when $\hat{i}$ is an optimal arm, so success at [[Best-Arm Identification]] implies zero simple regret. Conversely, simple regret below the gap between the best and second-best means implies that $\hat{i}$ is optimal.
- Bounded for uniform sampling by the [[Uniform Sampling Simple Regret Bound]].

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=2)
