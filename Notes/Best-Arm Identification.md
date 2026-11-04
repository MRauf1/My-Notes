---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Best-Arm Identification[^1]
> For a [[Multi-Armed Bandit]], the objective of returning, after $T$ rounds, an arm $\hat{i} \in \arg\max_{i \in [K]} \mu_i$.

# Properties
- Related to minimizing [[Simple Regret]], but stricter: an arm within $\epsilon$ of $\mu^\star$ has small simple regret yet may not be the best arm.
- Results often require additional gap conditions, e.g. a lower bound on the gap between $\mu^\star$ and the best suboptimal mean. Without one, two arms can be arbitrarily close, and no fixed $T$ separates them reliably.
- Its sample complexity is lower bounded by the [[Best-Arm Identification Lower Bound]].

[^1]: [Jiang, Concentration Inequalities and Union Bound (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note2.pdf#page=2)
