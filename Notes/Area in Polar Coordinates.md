---
tags:
  - mathematics
  - calculus
---

# Definition

> [!abstract] Theorem 1 (Area in Polar Coordinates)[^1]
> If $f$ is continuous and $f \geq 0$ on $[a, b]$ with $0 < b - a \leq 2\pi$, the area of the region bounded by $r = f(\theta)$ and the rays $\theta = a$, $\theta = b$ is
> $$
> \begin{align}
> A = \int_a^b \frac{1}{2}[f(\theta)]^2\,d\theta = \int_a^b \frac{1}{2} r^2\,d\theta
> \end{align}
> $$

# Properties
- Derived from [[Riemann Sum|Riemann sums]] of circular sectors of area $\frac{1}{2}r^2\Delta\theta$ in the [[Polar Coordinate System]].
- Area between $r = f(\theta) \geq g(\theta)$: $\frac{1}{2}\int_a^b (f^2 - g^2)\,d\theta$. Intersection points must be found carefully, since the pole and points with several representations may not appear as solutions of $f(\theta) = g(\theta)$.
- Loops of [[Rose Curve|roses]], [[Lemniscate|lemniscates]] and [[Limacon|limaçon]] inner loops are integrated between consecutive zeros of $r$.

[^1]: [Calculus: Early Transcendentals](zotero://open-pdf/library/items/EEFDQ9Y5?page=701)
