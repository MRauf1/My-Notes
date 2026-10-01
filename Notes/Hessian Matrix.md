---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Hessian Matrix)[^1]
> For a [[Cost Function]] $J(\theta)$, the matrix $H$ of its second-order partial derivatives with respect to the parameters, describing how the loss landscape is locally curving.

# Properties
- Explicitly, for $L[\boldsymbol{\phi}]$ with $\boldsymbol{\phi} = [\phi_0, \dots, \phi_N]^T$, $\mathbf{H}[\boldsymbol{\phi}]_{jk} = \frac{\partial^2 L}{\partial \phi_j \partial \phi_k}$.[^2]
- If $\mathbf{H}$ is [[Positive Definite Matrix|positive definite]] for all parameter values, the loss is [[Convex Function|convex]]: a smooth bowl with a single [[Global Minimum]] and no local minima or [[Saddle Point|saddle points]].
- At a stationary point, its eigenvalues classify the point as a minimum (all positive), a maximum (all negative), or a [[Saddle Point]] (mixed signs).
- Used by [[Newton's Method (Optimization)|Newton's method]].
- Used in [[Higher-Order Optimization]] methods, which exploit curvature information beyond the gradient used by [[First-Order Optimization]].
- Costly to compute exactly for high-dimensional parameter vectors, so many methods instead use approximations to the Hessian, or other properties related to loss curvature.

[^1]: [MIT Vision Book - Gradient Descent](https://visionbook.mit.edu/gradient_descent.html)
[^2]: [Prince, Ch. 6](zotero://select/library/items/T3V9WVXD)
