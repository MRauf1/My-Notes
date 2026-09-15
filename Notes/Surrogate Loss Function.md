---
tags:
  - computer_science
  - computer_vision
---

# Definition

A [[Function|function]] with non-zero [[Gradient Vector|gradients]] that approximates some [[Loss Function|loss function]].[^1]

# Properties
- One of several ways to obtain a locally loss-minimizing update direction $\mathbf{v}$ when the true gradient of the [[Cost Function]] is zero almost everywhere or otherwise unhelpful; a common choice is a smoothed version of the true cost function.
- Contrasts with an [[Evolution Strategy]], which instead estimates $\mathbf{v}$ by sampling perturbations of the parameters rather than by approximating the cost function itself.

[^1]: https://visionbook.mit.edu/gradient_descent.html