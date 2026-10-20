---
tags:
  - mathematics
  - real_analysis
---

# Definition
> [!abstract] Theorem 1 (Change of Variable)[^1]
> Suppose $\varphi$ is a strictly increasing [[Continuous Function]] that maps an interval $[A, B]$ onto $[a, b]$. Suppose $\alpha$ is monotonically increasing on $[a, b]$ and $f \in \mathscr{R}(\alpha)$ on $[a, b]$. Define $\beta$ and $g$ on $[A, B]$ by
> $$
> \begin{align}
> \beta(y) = \alpha(\varphi(y)), \qquad g(y) = f(\varphi(y))
> \end{align}
> $$
> Then $g \in \mathscr{R}(\beta)$ and
> $$
> \begin{align}
> \int_A^B g \, d\beta = \int_a^b f \, d\alpha
> \end{align}
> $$

> [!abstract] Corollary 2 (Substitution Rule for the [[Riemann Integral]])[^2]
> Take $\alpha(x) = x$, so $\beta = \varphi$, and assume $\varphi' \in \mathscr{R}$ on $[A, B]$. Then for $f \in \mathscr{R}$ on $[a, b]$,
> $$
> \begin{align}
> \int_a^b f(x) \, dx = \int_A^B f(\varphi(y)) \varphi'(y) \, dy
> \end{align}
> $$

The corollary follows by applying [[Riemann-Stieltjes Integral with Differentiable Integrator Theorem]] to the left side of Theorem 1. In the Stieltjes form, the Jacobian factor $\varphi'$ is hidden in the new integrator $\beta = \alpha \circ \varphi$.

# Properties
- Partitions of $[A, B]$ and $[a, b]$ correspond bijectively under $\varphi$, and the upper/lower sums coincide.
- Multivariable analogue: [[Change of Variables]] (with the Jacobian determinant).
- Related: [[u-Substitution]].

[^1]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=141&annotation=EW4QFFWN)
[^2]: [Principles of Mathematical Analysis](zotero://open-pdf/library/items/77RSE64H?page=142&annotation=X7FXULBN)
