---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Tangent Plane to a Graph)[^1]
> If $f$ has continuous [[Partial Derivative|partial derivatives]], the tangent plane to the surface $z = f(x, y)$ at $P(x_0, y_0, z_0)$ is
> $$
> \begin{align}
> z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)
> \end{align}
> $$

> [!abstract] Theorem 2 (Tangent Plane to a Level Surface)[^2]
> For the [[Level Set|level surface]] $F(x, y, z) = k$ with $\nabla F(x_0, y_0, z_0) \neq 0$, the tangent plane at $P$ is $\nabla F(P) \cdot (x - x_0, y - y_0, z - z_0) = 0$, and the normal line is $P + t\,\nabla F(P)$ ([[Gradient Vector]], [[Plane]]).

# Properties
- The linearization $L(x, y) = f(a, b) + f_x(a, b)(x - a) + f_y(a, b)(y - b)$ is the tangent plane viewed as a function ([[Linear Approximation]]). It approximates $f$ well when $f$ is differentiable, which holds when $f_x, f_y$ are continuous near $(a, b)$ ([[Partial Derivative Differentiable Theorem]]).
- Separate from the differential-geometry tangent plane $T_p(M)$ of a surface, which this calculus version motivates.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=960)
[^2]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=983)
