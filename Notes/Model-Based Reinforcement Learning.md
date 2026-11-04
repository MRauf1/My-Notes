---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Model-Based Reinforcement Learning[^1]
> A family of reinforcement learning algorithms that first estimate a [[Markov Decision Process]] model (transition function $\widehat{P}$ and, if needed, reward function $\widehat{R}$) from data, then perform [[Policy Evaluation|policy evaluation]] or optimization ([[Planning]]) in the estimated model.

# Types
- [[Certainty-Equivalence (Reinforcement Learning)]]

# Properties
- A tabular model has $O(|\mathcal{S}|^2|\mathcal{A}|)$ space complexity, and the algorithms are typically **batch**: invoked after all data are collected.
- Typically more sample-efficient than [[Value-Based Reinforcement Learning|value-based methods]], which store only a Q-value function. Its counterpart in agent design is the [[Model-Free Agent]].
- Value errors induced by model errors are controlled by the [[Simulation Lemma]].

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 1](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=1)
