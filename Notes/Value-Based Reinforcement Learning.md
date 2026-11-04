---
tags:
  - computer_science
  - reinforcement_learning
---

# Definition
> [!info] Value-Based Reinforcement Learning[^1]
> A family of reinforcement learning algorithms that model only the [[Action-Value Function|Q-value function]], not the transition and reward functions. Examples are Q-learning and Sarsa.

# Properties
- Tabular versions need only $O(|\mathcal{S}||\mathcal{A}|)$ space, versus $O(|\mathcal{S}|^2|\mathcal{A}|)$ for [[Model-Based Reinforcement Learning]].
- Can run **online**: the algorithm updates as more data are collected, rather than in a batch.
- Easy to combine with sophisticated generalization schemes such as deep neural networks, which has led to many empirical successes.
- Typically less sample-efficient than model-based methods. Techniques such as experience replay improve the sample efficiency of online algorithms, but blur the boundary between value-based and model-based methods.
- Batch (offline) example with function approximation: [[Fitted Q-Iteration]].
- Related: [[Temporal-Difference Learning]], [[Model-Free Agent]].

[^1]: [Jiang, Notes on Tabular Methods (CS 542 notes), pp. 1–2](https://nanjiang.cs.illinois.edu/files/cs542f22/note3.pdf#page=1)
