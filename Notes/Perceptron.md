---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (Perceptron)
> For input [[Vector|vector]] $\mathbf{x}$ and weight vector $\mathbf{w}$, the perceptron is
> $$
> \begin{align}
> z = f(\mathbf{x}) = \mathbf{w}^T \mathbf{x} + b \\
> g(z) = \begin{cases}
> 1 & z > 0 \\
> 0 & \text{otherwise}
> \end{cases} \\
> y = g(f(\mathbf{x}))
> \end{align}
> $$

Perceptron activates the neuron ($=1$) if the [[Weighted Sum|weighted sum]] of inputs is above the threshold of $0$, and otherwise, the neuron is not activated ($=0$).[^1]

Perceptron can solve a linearly separable [[Binary Classification]] problems.

[^1]: https://visionbook.mit.edu/neural_nets.html