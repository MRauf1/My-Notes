---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (ReLU [[Function]])
> $$
> \begin{align}
> ReLU(z) = max(0, z)
> \end{align}
> $$

Rectified Linear Unit (ReLU) is an [[Activation Layer|activation function]] commonly used in [[Deep Neural Network|DNNs]].[^1]

> [!info] Definition 2 (ReLU Function [[Gradient]])
> $$
> \begin{align}
> \frac{\partial (ReLU(z))}{\partial z} = \begin{cases}0 & z < 0 \\ 1 & z \geq 0\end{cases}
> \end{align}
> $$

# Properties
- [[ReLU Function Geometric Properties]]
- [[ReLU Function Biological Plausability]]

## Pros
- [[ReLU Function Benefits]]

## Cons
- [[ReLU Function Downsides]]

[^1]: https://visionbook.mit.edu/neural_nets.html