---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Surface Area of a Graph)[^1]
> If $f_x$ and $f_y$ are continuous on $D$, the area of the surface $z = f(x, y)$, $(x, y) \in D$, is
> $$
> \begin{align}
> A(S) = \iint_D \sqrt{1 + f_x^2 + f_y^2}\,dA
> \end{align}
> $$

# Properties
- Derived by approximating the surface with tangent-plane patches of area $|\mathbf a \times \mathbf b| = \sqrt{1 + f_x^2 + f_y^2}\,\Delta A$, where $\mathbf a = (\Delta x, 0, f_x\Delta x)$ and $\mathbf b = (0, \Delta y, f_y\Delta y)$ ([[Cross Product]], [[Tangent Plane (Calculus)]]).
- Two-variable analogue of [[Arc Length]]; [[Surface Area of Revolution]] is a special case.
- A [[Double Riemann Integral]], often evaluated in polar coordinates.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=1059)
