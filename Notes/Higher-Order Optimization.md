---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Higher-Order Optimization)[^1]
> An optimization setting in which the update function observes higher-order derivatives of the [[Cost Function]] beyond the gradient, such as the [[Hessian Matrix]], which describes how the loss landscape is locally curving.

# Properties
- More informative than [[First-Order Optimization]], but the Hessian is costly to compute exactly; many methods instead use approximations to the Hessian, or other properties related to loss curvature.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
