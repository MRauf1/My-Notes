---
tags:
  - computer_science
  - computer_vision
---

# Definition

> [!info] Definition 1 (ReLU [[Function]])
> $$
> \begin{align}
> ReLU(z) = max(0, z)
> \end{align}
> $$

Rectified Linear Unit (ReLU) is an [[Activation Layer|activation function]] commonly used in [[Deep Neural Network|DNNs]].[^1]

> [!info] Definition 2 (ReLU Function [[Gradient Vector]])
> $$
> \begin{align}
> \frac{\partial (ReLU(z))}{\partial z} = \begin{cases}0 & z < 0 \\ 1 & z \geq 0\end{cases}
> \end{align}
> $$

# Properties
- **Non-negative homogeneity**: $\mathrm{ReLU}[\alpha z] = \alpha\,\mathrm{ReLU}[z]$ for all $\alpha \in \mathbb{R}^+$.[^2]
- Networks built from it compute continuous piecewise linear functions whose regions are easy to characterize ([[Linear Regions of ReLU Network]]), which, together with its interpretability, makes it the most common activation.[^3]
- Its zero gradient for negative inputs causes the [[Dying ReLU Problem]].
- [[ReLU Function Geometric Properties]]
- [[ReLU Function Biological Plausability]]

## Pros
- [[ReLU Function Benefits]]

## Cons
- [[ReLU Function Downsides]]

# Variants
- [[Leaky ReLU]]
- [[Parametric ReLU]]
- [[Concatenated ReLU]]
- Smooth: [[Softplus Function]], [[Gaussian Error Linear Unit]], [[Swish Function]] (incl. SiLU), [[HardSwish Function]], [[Exponential Linear Unit]], [[Scaled Exponential Linear Unit]]

[^1]: https://visionbook.mit.edu/neural_nets.html
[^2]: [Prince, p. 39](zotero://open-pdf/library/items/BWT7FYX5?page=53&annotation=ERIGHJIL)
[^3]: [Prince, p. 35](zotero://open-pdf/library/items/BWT7FYX5?page=49&annotation=W2XKTGZD); [Prince, p. 38](zotero://open-pdf/library/items/BWT7FYX5?page=52&annotation=35695IHL)
