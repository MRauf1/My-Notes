---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Stochastic Policy
> A [[Policy]] $\pi: \mathcal{S} \to \Delta(\mathcal{A})$ that maps each state to a distribution over actions, with $a_t \sim \pi(s_t)$.

# Properties
- Generalizes the [[Deterministic Policy]], which is the special case where $\pi(s)$ is a point mass for every $s \in \mathcal{S}$.
