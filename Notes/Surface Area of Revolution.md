---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Area of a Surface of Revolution)[^1]
> If $f \geq 0$ and $f'$ is continuous on $[a, b]$, the area of the surface obtained by rotating $y = f(x)$, $a \leq x \leq b$, about the $x$-axis is
> $$
> \begin{align}
> S = \int_a^b 2\pi f(x)\sqrt{1 + [f'(x)]^2}\,dx = \int 2\pi y\,ds
> \end{align}
> $$
> About the $y$-axis: $S = \int 2\pi x\,ds$, with $ds$ the [[Arc Length]] element.

# Properties
- Derived by approximating the surface with bands (frusta of cones) of area $2\pi r\,\ell$, where $r$ is the average radius and $\ell$ the slant length.
- Can be integrated in $x$ or in $y$, using $ds = \sqrt{1 + (dy/dx)^2}\,dx = \sqrt{1 + (dx/dy)^2}\,dy$.
- Special case of [[Surface Area]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=584)
