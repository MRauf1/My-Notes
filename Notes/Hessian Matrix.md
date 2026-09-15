---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Hessian Matrix)[^1]
> For a [[Cost Function]] $J(\theta)$, the matrix $H$ of its second-order partial derivatives with respect to the parameters, describing how the loss landscape is locally curving.

# Properties
- Used in [[Higher-Order Optimization]] methods, which exploit curvature information beyond the gradient used by [[First-Order Optimization]].
- Costly to compute exactly for high-dimensional parameter vectors, so many methods instead use approximations to the Hessian, or other properties related to loss curvature.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
