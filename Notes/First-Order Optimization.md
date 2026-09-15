---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (First-Order Optimization)[^1]
> Also called **gradient-based optimization**, an optimization setting in which the update function takes as input the gradient of the [[Cost Function]] with respect to the parameters at the current [[Operating Point]], $\nabla_\theta J(\theta)$, revealing the direction of steepest descent.

# Properties
- Reveals substantially more information about how to minimize the cost than [[Zeroth-Order Optimization]], which observes only the cost's value.
- [[Gradient-Based Learning|Gradient-based learning algorithms]], such as [[Gradient Descent]], are first-order optimization methods.
- Contrasts with [[Higher-Order Optimization]], which additionally uses information about how the cost's gradient itself is changing, such as the [[Hessian Matrix]].

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
