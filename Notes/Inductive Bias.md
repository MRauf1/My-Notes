---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Inductive Bias)[^1]
> The set of assumptions built into a learning algorithm's [[Hypothesis Space]] or optimization procedure that lead it to prefer some solutions over others, beyond what is strictly implied by the training data alone.

# Properties
- In Prince's terms: the tendency of a model to prioritize one solution over another *between data points*. Once a model fits the training data almost perfectly, extra capacity can only change its behaviour between the training points, so the inductive bias determines generalization in the over-parameterized regime ([[Double Descent]]).[^2]
- One of the reasons [[Deep Neural Network|deep nets]] work well: their architectures (e.g. convolutional weight-sharing, or attention) reflect real structure in the world, which biases the search toward learned solutions that capture true structure and so generalize, rather than toward arbitrary functions that merely fit the training data.
- [[The Bitter Lesson (Sutton)|Sutton's Bitter Lesson]] argues that hand-designed, human inductive biases tend to be outperformed over time by more general architectures paired with more data and compute, though inductive biases that reflect general mathematical structure of the world, such as invariances, may remain useful even as compute scales; see [[Priors in Light of the Bitter Lesson]].

[^1]: [MIT Vision Book - Neural Networks](https://visionbook.mit.edu/neural_nets.html)
[^2]: [Prince, p. 129](zotero://open-pdf/library/items/BWT7FYX5?page=143&annotation=XN6MRP3D)
