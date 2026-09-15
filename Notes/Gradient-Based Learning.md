---
tags:
  - computer_science
  - computer_vision
---

# Definition

A family of [[First-Order Optimization|first-order optimization]] [[Algorithm|algorithms]], which calculate the [[Gradient Vector|gradient]] and descend in the direction of the steepest descent.[^1]

# Properties
- Contrasts with [[Zeroth-Order Optimization]], which observes only the [[Cost Function|cost's]] value, and [[Higher-Order Optimization]], which additionally uses curvature information such as the [[Hessian Matrix]].
- Most gradient-based optimizers do not strictly require the true gradient; their update rules are compatible with any locally loss-minimizing direction $\mathbf{v}$, which can instead be obtained via a [[Surrogate Loss Function]] or an [[Evolution Strategy]] when the true gradient is zero almost everywhere or otherwise unhelpful.

# Optimizers
- [[Gradient Descent|Gradient Descent]]
- [[Gradient Descent with Momentum|Gradient Descent with Momentum]]
- [[Adam]]
- [[Evolution Strategy|Evolution Strategy]]

[^1]: https://visionbook.mit.edu/gradient_descent.html