---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Dynamic Programming)[^1]
> An algorithmic strategy of avoiding redundant computation by identifying that a computation shares intermediate terms with other computations, evaluating each shared term once, and reusing it wherever it is needed.

# Properties
- [[Backpropagation]] is an instance of this strategy: the gradients $\partial J/\partial\theta_1, \partial J/\partial\theta_2, \dots$ needed for every parameter share most of the same chain-rule terms (e.g. $\partial J/\partial\mathbf{x}_L$, $\partial\mathbf{x}_L/\partial\mathbf{x}_{L-1}$, and so on), so backpropagation computes each shared term once and reuses it, rather than recomputing every parameter's gradient from scratch.

[^1]: [MIT Vision Book - Backpropagation](https://visionbook.mit.edu/backpropagation.html)
