---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Mean Value Property (Harmonic Function)[^1]
> Let $u$ be a [[Harmonic Function]] in a disk $D$, continuous on its closure. Then the value of $u$ at the center equals its average over the circumference:
> $$
> \begin{align}
> u(\mathbf{x}_0) = \frac{1}{2\pi a}\oint_{|\mathbf{x} - \mathbf{x}_0| = a} u \, ds .
> \end{align}
> $$

**General case.**[^2] If $\Delta u = 0$ in an open set containing the closed ball $\bar B(\mathbf{x}_0, a) \subset \mathbb{R}^n$, then $u(\mathbf{x}_0)$ equals the average of $u$ over the sphere $\partial B(\mathbf{x}_0, a)$ and also over the ball $B(\mathbf{x}_0, a)$. Conversely, a continuous function with the mean value property on all small spheres is harmonic.

# Properties
- Proof: set $r = 0$ in [[Poisson's Formula]], where the [[Poisson Kernel]] is identically $1$ (or note $u(0) = \tfrac12 A_0$ in the [[Laplace Equation in a Disk|series solution]]).[^1]
- Implies the strong [[Maximum Principle (Laplace Equation)]]: an interior maximum forces $u$ to equal the maximum on every small circle, hence on the connected domain.[^2]
- Basis of the [[Walk on Spheres]] Monte Carlo solver.
- Analogue of the [[Mean Value Theorem]] in spirit only: it is an averaging identity, not a derivative identity.[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=181&annotation=9CCS3ZDT)
[^2]: Added from general knowledge.
