---
tags:
  - computer_science
  - computer_vision
---

# Definition

When the [[Gradient Vector|gradient]] [[Magnitude|magnitudes]] are too small, which results in very slow convergence for [[Gradient Descent|gradient descent]].[^1]

# Properties
- In deep networks, poorly scaled weights $\boldsymbol{\Omega}$ make gradient magnitudes shrink uncontrollably during the backward pass of [[Backpropagation]], so updates become vanishingly small; prevented by [[Weight Initialization|variance-preserving initialization]] such as [[He Initialization]].[^2]
- When the gradient is zero almost everywhere, it is sometimes possible to substitute a [[Surrogate Loss Function]] with meaningful gradients, or to estimate a useful update direction by sampling perturbations, as in an [[Evolution Strategy]].

[^1]: https://visionbook.mit.edu/gradient_descent.html
[^2]: [Prince, Ch. 7](zotero://select/library/items/T3V9WVXD)
