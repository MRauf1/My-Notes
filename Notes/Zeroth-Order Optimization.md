---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Zeroth-Order Optimization)[^1]
> An optimization setting in which the update function observes only the value of the [[Cost Function]] $J(\theta)$ at the current [[Operating Point]], not its derivatives. The only way to find $\theta$'s that minimize $J$ is to sample different values of $\theta$ and move toward those that give lower values.

# Properties
- Contrasts with [[First-Order Optimization]], which additionally observes the gradient of the cost, and [[Higher-Order Optimization]], which observes still higher-order derivatives.
- The [[Evolution Strategy]] approach to gradient-based learning is closely related, sampling perturbations of $\theta$ to estimate a useful update direction without an analytical gradient.
- Its gradient-estimate variance grows with the dimension of $\theta$, which is why [[Reverse-Mode Automatic Differentiation for High-Dimensional Gradients|reverse-mode automatic differentiation]] is preferred once $\theta$ has $10^4$–$10^7$ dimensions.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
