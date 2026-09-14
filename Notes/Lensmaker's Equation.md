---
tags:
  - computer_science
  - computer_vision
---

# Definition
> [!info] Definition (Lensmaker's Equation)[^1]
> Under the [[Paraxial Approximation]] and [[Thin Lens Approximation]], a spherical [[Lens]] surface of radius $R$ and index of refraction $n$ focuses light from a point at distance $a$ on one side of the lens to a point at distance $b$ on the other side according to
> $$
> \begin{align}
> \frac{1}{a} + \frac{1}{b} = \frac{1}{f}
> \end{align}
> $$
> where the lens's [[Focal Length (Lens)|focal length]] $f$ is
> $$
> \begin{align}
> f = \frac{R}{2(n-1)}
> \end{align}
> $$

# Properties
- Generalizes, for a lens with different radii of curvature $R_1$ and $R_2$ on its front and back surfaces, to $\dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1} + \dfrac{1}{R_2}\right)$.
- Also holds for light originating off the optical axis, not only for rays traveling along it.
- Shows that, under these approximations, a lens focuses light from every point on one plane onto a corresponding point on a second plane, both perpendicular to the optical axis.

[^1]: [MIT Vision Book - Lenses](https://visionbook.mit.edu/lenses.html)
