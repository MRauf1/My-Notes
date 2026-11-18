---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Area Between Curves)[^1]
> The area of the region bounded by $y = f(x)$, $y = g(x)$, $x = a$ and $x = b$, with $f, g$ continuous on $[a, b]$, is
> $$
> \begin{align}
> A = \int_a^b |f(x) - g(x)|\,dx
> \end{align}
> $$
> In particular $A = \int_a^b \big(f(x) - g(x)\big)\,dx$ when $f \geq g$ on $[a, b]$.

# Properties
- Derived as the limit of [[Riemann Sum|Riemann sums]] of approximating rectangles of height $f(x_i^*) - g(x_i^*)$ ([[Definite Riemann Integral]]); the case $g = 0$ is the [[Area of Region Under Curve]].
- For regions bounded by $x = f(y)$ and $x = g(y)$ (right minus left), integrate with respect to $y$: $A = \int_c^d \big(x_R(y) - x_L(y)\big)\,dy$.
- When the curves cross, split the interval at the intersection points (solve $f = g$) and take the larger minus the smaller on each piece.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=460)
