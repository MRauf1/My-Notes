---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Method of Lagrange Multipliers)[^1]
> To find the maximum and minimum values of $f(x, y, z)$ subject to $g(x, y, z) = k$, assuming these extreme values exist and $\nabla g \neq 0$ on the surface $g = k$:
> 1. Find all $x, y, z, \lambda$ with $\nabla f(x, y, z) = \lambda\,\nabla g(x, y, z)$ and $g(x, y, z) = k$.
> 2. Evaluate $f$ at all these points. The largest value is the maximum and the smallest is the minimum.

# Properties
- Geometric reason: at a constrained extremum, the [[Level Set]] of $f$ is tangent to the constraint surface, so the [[Gradient Vector|gradients]] are parallel.
- Two constraints $g = k$, $h = c$: solve $\nabla f = \lambda\nabla g + \mu\nabla h$.
- Existence of the extremes comes from the [[Extreme Value Theorem]] when the constraint set is closed and bounded.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=1004)
