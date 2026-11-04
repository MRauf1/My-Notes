---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Generative Model (Reinforcement Learning)[^1]
> A data-collection setting for a [[Markov Decision Process]] in which the learner can query any state-action pair $(s, a)$ and receive an independent sample $r \sim R(s, a)$, $s' \sim P(\cdot \mid s, a)$. Typically each $(s, a)$ is sampled a fixed number $n$ of times, giving datasets $D_{s,a}$ of size $n$.

# Properties
- Removes the exploration problem: data do not depend on the learner's policy, so the samples in each $D_{s,a}$ are i.i.d. and independent across pairs. This is what makes [[Hoeffding's Inequality]] directly applicable in the [[Certainty-Equivalence Sample Complexity]] analysis.
- The total number of samples is $n|\mathcal{S}||\mathcal{A}|$. [[Sparse Sampling]] uses a generative model lazily, querying only pairs reachable from the current state.
- Not to be confused with a [[Generative Model]] in machine learning (a model of a data distribution).

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), p. 2](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=2)
