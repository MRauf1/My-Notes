---
tags: computer_science, computer_vision
---

# Definition

If thinking of the input data $X_0$ as a data distribution, then [[Deep Neural Network]] transform the input data distribution into an output data distribution.

Each intermediate layer then, represents a certain [[Embedding]]/[[Representation]] of the data.

[[Loss Function]] then, can be thought of as penalizing the [[Divergence]] between the output distribution $\hat{Y}$ and the target [[Probability Distribution]] $Y$.[^1]

One can also think of it as disentangling the messy input data into a representation that can be cleanly separated.

[^1]: https://visionbook.mit.edu/neural_nets_as_distribution_transformers.html