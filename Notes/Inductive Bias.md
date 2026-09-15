---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Inductive Bias)[^1]
> The set of assumptions built into a learning algorithm's [[Hypothesis Space]] or optimization procedure that lead it to prefer some solutions over others, beyond what is strictly implied by the training data alone.

# Properties
- One of the reasons [[Deep Neural Network|deep nets]] work well: their architectures (e.g. convolutional weight-sharing, or attention) reflect real structure in the world, which biases the search toward learned solutions that capture true structure and so generalize, rather than toward arbitrary functions that merely fit the training data.
- [[The Bitter Lesson (Sutton)|Sutton's Bitter Lesson]] argues that hand-designed, human inductive biases tend to be outperformed over time by more general architectures paired with more data and compute, though inductive biases that reflect general mathematical structure of the world, such as invariances, may remain useful even as compute scales.

[^1]: [MIT Vision Book - Neural Networks](https://visionbook.mit.edu/neural_nets.html)
