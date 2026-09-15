---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Activation Maximization)[^1]
> A technique for visualizing what a neuron in a [[Deep Neural Network|neural net]] is sensitive to, by using [[Backpropagation|backpropagation]] to optimize the *input* data, rather than the parameters, to maximize that neuron's activation. Concretely, one descends the gradient, with respect to the input $\mathbf{x}_0$, of a cost $J(\mathbf{x}_0,\theta) = -x_l[i]$, the negative of the $i$-th neuron's activation on layer $l$, while holding the parameters $\theta$ fixed; the cost is negated so that minimizing it maximizes the activation.

# Properties
- Relies on parameters and data playing symmetric roles in a [[Computation Graph]]: just as descending the parameter gradient minimizes the loss, descending the data gradient here maximizes a chosen neuron's activation.
- Often combined with a **natural image prior**, so that the optimization finds an input that both strongly activates the neuron in question and looks like a natural photograph, rather than an unrecognizable pattern.
- A form of feature visualization, used to build intuition for what visual features a given neuron in a trained network detects.

[^1]: [MIT Vision Book - Backpropagation](https://visionbook.mit.edu/backpropagation.html)
