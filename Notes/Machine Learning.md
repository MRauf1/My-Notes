---
tags:
  - computer_science
  - deep_learning
---

# Definition

[[Subset|Subset]] of [[Artificial Intelligence|artificial intelligence]] that learns to make decisions by fitting mathematical/statistical models to observed data.[^1]

These models represents the family of [[Function|functions]] that map the inputs to their respective outputs. When fitting a model to the training data, the algorithm searches through the family to come up with the most accurate function given the data.

Learning is a bit different from [[Optimization|optimization]] since learning studies how to generalize the optimization on the training data to the test data. Thus, optimization on training data acts as a proxy for optimization on the test data.

# Properties
- Characterized concisely as an algorithm that outputs algorithms: it searches, during a [[Training Phase]], for an algorithm that performs well on training data, then deploys that learned algorithm in a [[Testing Phase]] on new instances.[^2]
- [[Supervised Learning]] learns by matching observed input-output examples, whereas [[Unsupervised Learning]] and [[Reinforcement Learning]] instead optimize for desirable properties of the input-output mapping without being given explicit examples of it.
- Under this broad definition, biological [[Evolution]] itself qualifies as a learning algorithm, distinct from the [[Evolution Strategy]] optimization technique named after it.

# Types

- [[Supervised Learning|Supervised Learning]]
- [[Unsupervised Learning|Unsupervised Learning]]
- [[Reinforcement Learning|Reinforcement Learning]]

# Potential Problems

- [[Underfitting|Underfitting]]
- [[Overfitting|Overfitting]]

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=15)
[^2]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)