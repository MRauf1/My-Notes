---
tags: computer_science, computer_vision
---

# Definition

> [!info] Definition 1 (Gradient)[^2]
> For a [[Real-Valued Function]] $f(\mathbf{x})$, the gradient is
> $$
> \begin{align}
> \nabla f(\mathbf{x}) = <\frac{\partial f}{\partial x_1} (\mathbf{x}), \dots, \frac{\partial f}{\partial x_n} (\mathbf{x})>
> \end{align}
> $$

Gradient vector is a [[Vector]] that points in the direction of greatest rate of change of $f$, provided that $f$ is a [[Real-Valued Function]]. The extension of gradient vector to [[Real Vector-Valued Function]] is [[Jacobian Matrix]].

It is [[Orthogonal Vector]] to the [[Level Curve]] $f(\mathbf{x}) = k$ that passes through [[Point]] $P$. In other words, it is [[Orthogonal Vector]] to the [[Tangent Vector]] of the [[Level Curve]] at [[Point]] $P$.

From the perspective of [[Optimization|optimization]], the gradient is the locally [[Loss Function|loss]]-minimizing direction in the parameter space.[^1]

[^1]: https://visionbook.mit.edu/gradient_descent.html
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=982)