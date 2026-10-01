---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Global Minimum[^1]
> The point in parameter space with the lowest value of the loss function, $\boldsymbol{\phi}^* = \arg\min_{\boldsymbol{\phi}} L[\boldsymbol{\phi}]$; a [[Local Minimum|local minimum]] is a point where the gradient is zero and the loss increases in every direction, but which need not be the global minimum.

# Properties
- [[Gradient Descent]] from a random start has no guarantee of reaching the global minimum, and it is equally or more likely to terminate in a local minimum; there is no way of knowing whether a better solution exists elsewhere ([[Suboptimal Local Minimum]]).
- For low-dimensional models it can be found by exhaustive search or by restarting gradient descent from many positions and keeping the lowest loss; neither is practical with millions of parameters.
- A [[Convex Function|convex]] loss has a single global minimum and no other local minima or [[Saddle Point|saddle points]].

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
