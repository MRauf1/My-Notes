---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Gradient Clipping)[^1]
> A technique to combat [[Exploding Gradients]]: clamping the magnitude of the gradient used in a [[Gradient Descent|gradient descent]] update to some maximum value $m$, via
> $$
> \begin{align}
> \text{clip}(v, -m, m) = \max(\min(v, m), -m)
> \end{align}
> $$
> applied elementwise to the gradient vector.

# Properties
- Directly addresses the case where the gradient at the minimizer grows without bound, which otherwise causes gradient descent to fail to converge.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
