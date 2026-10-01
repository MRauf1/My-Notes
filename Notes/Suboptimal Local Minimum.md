---
tags:
  - computer_science
  - computer_vision
---

# Definition

For a [[Function|function]] with multiple [[Local Minimum|local minima]], [[Gradient Descent|gradient descent]] will converge to one of them based on the initialization. Thus, there is no guarantee that gradient descent converges to the [[Global Minimum|global minima]].[^1]

# Properties
- From a random start it is equally or more likely that gradient descent terminates in a local minimum than at the [[Global Minimum]], and there is no way of knowing whether a better solution exists. Exhaustive search or many random restarts are impractical with millions of parameters; [[Stochastic Gradient Descent]] can, in principle, escape local minima.[^2]

[^1]: https://visionbook.mit.edu/gradient_descent.html
[^2]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
