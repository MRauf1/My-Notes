---
tags:
  - computer_science
  - computer_vision
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

# Training
> [!info] Definition 2 (Perceptron Training Objective)
> Given data $\{\mathbf{x}^{(i)}, y^{(i)}\}_{i=1}^N$, training adjusts the weights $\mathbf{w}$ and bias $b$ to minimize a classification [[Loss Function|loss]] $\mathcal{L}$ that scores the number of misclassifications:
> $$
> \begin{align}
> \mathbf{w}^*, b^* = \underset{\mathbf{w},b}{\arg\min}\ \frac{1}{N}\sum_{i=1}^N \mathcal{L}(\mathbf{w}^T\mathbf{x}^{(i)} + b, y^{(i)})
> \end{align}
> $$

# Properties
- Geometrically, this optimization process corresponds to shifting and rotating the perceptron's [[Decision Boundary]] until it separates the two classes.

[^1]: https://visionbook.mit.edu/neural_nets.html