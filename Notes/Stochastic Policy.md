---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Stochastic Policy[^1]
> A [[Policy]] $\pi: \mathcal{S} \to \Delta(\mathcal{A})$ that maps each state to a distribution over actions, with $a_t \sim \pi(s_t)$.

# Properties
- Generalizes the [[Deterministic Policy]], which is the special case where $\pi(s)$ is a point mass for every $s \in \mathcal{S}$.
- Its value function satisfies the stochastic-policy form of the [[Bellman Equation (Policy Evaluation)|Bellman equation]], which averages over $a \sim \pi(s)$ as well as over $s' \sim P(s,a)$.

[^1]: [Jiang, MDP Preliminaries (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note1.pdf#page=2)
