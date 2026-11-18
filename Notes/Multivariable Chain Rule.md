---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Chain Rule, Cases 1 and 2)[^1]
> If $z = f(x, y)$ is differentiable and $x = g(t)$, $y = h(t)$ are differentiable, then
> $$
> \begin{align}
> \frac{dz}{dt} = \frac{\partial z}{\partial x}\frac{dx}{dt} + \frac{\partial z}{\partial y}\frac{dy}{dt}
> \end{align}
> $$
> If $x = g(s, t)$ and $y = h(s, t)$, then $\frac{\partial z}{\partial s} = \frac{\partial z}{\partial x}\frac{\partial x}{\partial s} + \frac{\partial z}{\partial y}\frac{\partial y}{\partial s}$, and similarly for $t$.

> [!abstract] Theorem 2 (General Version)[^2]
> If $u$ is a differentiable function of $x_1, \dots, x_n$, and each $x_j$ is a differentiable function of $t_1, \dots, t_m$, then $\frac{\partial u}{\partial t_i} = \sum_{j=1}^{n} \frac{\partial u}{\partial x_j}\frac{\partial x_j}{\partial t_i}$. In matrix form, the [[Jacobian Matrix|Jacobians]] multiply.

# Properties
- Generalizes the [[Derivative Chain Rule]]; tree diagrams organize the terms.
- Implicit differentiation: if $F(x, y) = 0$ defines $y(x)$, then $\frac{dy}{dx} = -\frac{F_x}{F_y}$; if $F(x, y, z) = 0$ defines $z(x, y)$, then $\frac{\partial z}{\partial x} = -\frac{F_x}{F_z}$ ([[Implicit Differentiation]]).
- Second derivatives under a change of variables (e.g. the Laplacian in polar coordinates) need the chain rule applied twice together with the product rule.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=970)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=971)
