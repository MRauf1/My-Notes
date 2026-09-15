---
tags:
  - computer_science
  - deep_learning
---

# Definition

[[Subset|Subset]] of [[Machine Learning|machine learning]] where agent living in some (not necessarily deterministic) system, acts (and these actions change the state of the system) in a way that maximizes its reward.[^1]

# Properties
- Rather than matching observed input-output examples as in [[Supervised Learning]], learns by optimizing for desirable properties, such as expected reward, of the input-output mapping.[^2]
- Explicitly measures the quality of the learned function's output with a [[Reward Function]], and searches for a function that maximizes reward.

# Difficulties

- [[Temporal Credit Assignment Problem|Temporal Credit Assignment Problem]]
- Exploitation vs. Exploration Tradeoff

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=25)
[^2]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)