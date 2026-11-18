---
tags:
  - mathematics
  - calculus
---

# Definition

> [!info] Definition 1 (Volume by Slicing)[^1]
> Let $S$ be a solid between $x = a$ and $x = b$ whose cross-section in the plane through $x$ perpendicular to the $x$-axis has area $A(x)$, with $A$ continuous. The volume of $S$ is
> $$
> \begin{align}
> V = \lim_{n \to \infty} \sum_{i=1}^n A(x_i^*)\,\Delta x = \int_a^b A(x)\,dx
> \end{align}
> $$

# Types
- Disk method (solid of revolution, region touching the axis): $A(x) = \pi r(x)^2$.
- Washer method (region separated from the axis): $A(x) = \pi\big(r_{\text{out}}(x)^2 - r_{\text{in}}(x)^2\big)$.
- Rotation about a horizontal or vertical line other than an axis: radii are measured as distances to that line.

# Properties
- Defined through [[Riemann Sum|Riemann sums]] of slab volumes ([[Definite Riemann Integral]]).
- Alternative for solids of revolution: [[Cylindrical Shells Method]].

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=471)
