---
tags:
  - physics
  - introduction_to_physics
---

# Definition
> [!info] Lorentz Transformation[^1]
> $$
> \begin{align}
> x' &= \frac{x-ut}{\sqrt{1-u^2/c^2}}, & y' &= y, & z' &= z, & t' &= \frac{t - ux/c^2}{\sqrt{1-u^2/c^2}}
> \end{align}
> $$
> The coordinate transformation between two inertial frames in relative motion at speed $u$ along their common $x$-axis, under which Maxwell's equations of electromagnetism — and, by the postulate of [[Special Relativity]], all physical laws — retain exactly the same form.

# Properties
- Discovered by Lorentz as the transformation that leaves Maxwell's equations unchanged; Einstein, extending a suggestion of Poincaré, proposed that *all* physical laws, including Newtonian mechanics, must be rewritten (via [[Relativistic Momentum]]) to be invariant under it.
- Reduces to the ordinary Galilean transformation ($x'=x-ut,\ t'=t$) when $u \ll c$, recovering [[Galilean Relativity]] in that limit.
- Mixes the $x$ and $t$ coordinates into one another in the same way an ordinary rotation of spatial axes mixes $x$ and $y$; it can be thought of as a "rotation" between space and time.
- Implies the [[Relativity of Simultaneity]] (from the $ux/c^2$ term in the transformation of $t$) and [[Length Contraction]] (from the transformation of $x$).
- Leaves the [[Spacetime Interval]] $x^2+y^2+z^2-c^2t^2$ invariant, exactly as a rotation leaves the Euclidean distance to the origin invariant.

[^1]: [The Feynman Lectures on Physics, Vol. I, Ch. 15: The Special Theory of Relativity](https://www.feynmanlectures.caltech.edu/I_15.html)
