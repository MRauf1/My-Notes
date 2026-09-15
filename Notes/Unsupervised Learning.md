---
tags:
  - computer_science
  - deep_learning
---

# Definition

[[Subset|Subset]] of [[Machine Learning|machine learning]] that learns without labeled data. The goal is to describe/understand structure within the data.[^1]

# Properties
- Rather than matching observed input-output examples as in [[Supervised Learning]], learns by optimizing for desirable properties of the input-output mapping.[^2]
- Given input data $\{\mathbf{x}^{(i)}\}_{i=1}^N$ without target outputs, the learner comes up with a model or representation of the input data with useful properties, as measured by an [[Objective Function]]; for example, the objective may reward compressing the data into a lower-dimensional format that still preserves all information about the inputs.

# Types
- [[Clustering]]

[^1]: [Understanding Deep Learning](zotero://open-pdf/library/items/RTSRBVL6?page=21)
[^2]: [MIT Vision Book - Introduction to Learning](https://visionbook.mit.edu/intro_to_learning.html)