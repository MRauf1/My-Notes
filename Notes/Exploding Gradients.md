---
tags:
  - computer_science
  - computer_vision
---

# Definition

When the [[Gradient Vector|gradient]] [[Magnitude|magnitudes]] are too big, which results in divergence for [[Gradient Descent|gradient descent]].[^1]

One solution is [[Gradient Clipping]], which clips the gradients to some maximum value.

# Properties
- In deep networks, poorly scaled weights $\boldsymbol{\Omega}$ make gradient magnitudes grow uncontrollably during the backward pass of [[Backpropagation]], so updates become unstable; prevented by [[Weight Initialization|variance-preserving initialization]] such as [[He Initialization]].[^2]

[^1]: https://visionbook.mit.edu/gradient_descent.html
[^2]: [Prince, Ch. 7](zotero://select/library/items/T3V9WVXD)
