---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (ReLU)
> $$
> \begin{align}
> ReLU(z) = max(0, z)
> \end{align}
> $$

Rectified Linear Unit (ReLU) is an [[Activation Layer|activation function]] commonly used in [[Deep Neural Network|DNNs]].[^1]

It produces nonzero [[Gradient|gradients]] for the positive half of the [[Domain|domain]], which is good for stable learning, but it produces zero gradients for the negative half of the domain, which can cause issues (in practice, it usually works out well).

[^1]: https://visionbook.mit.edu/neural_nets.html