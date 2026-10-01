---
tags:
  - computer_science
  - deep_learning
---

# Definition
> [!info] Newton's Method (Optimization)[^1]
> A [[Higher-Order Optimization|second-order]] method that accounts for the curvature of the loss using the inverse of the [[Hessian Matrix]] $\mathbf{H}$:
> $$
> \begin{align}
> \boldsymbol{\phi} \leftarrow \boldsymbol{\phi} - \mathbf{H}[\boldsymbol{\phi}]^{-1} \frac{\partial L}{\partial \boldsymbol{\phi}}
> \end{align}
> $$

# Properties
- Equivalent to applying the root-finding [[Newton's Method]] to the gradient $\partial L / \partial \boldsymbol{\phi} = \mathbf{0}$.
- Takes more cautious steps where the gradient changes quickly; eliminates the need for [[Line Search]] and avoids the oscillation of [[Gradient Descent]] in valleys.
- In its simplest form it moves toward the nearest extremum, which may be a maximum if closer to the top of a hill than the bottom of a valley.
- Computing the inverse Hessian is intractable for the millions of parameters of neural networks.

[^1]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
