---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation in the Exterior of a Circle[^1][^2]
> The Dirichlet problem
> $$
> \begin{align}
> u_{xx} + u_{yy} = 0 \ \text{ for } x^2 + y^2 > a^2, \qquad u = h(\theta) \ \text{ for } x^2 + y^2 = a^2, \qquad u \text{ bounded as } x^2 + y^2 \to \infty
> \end{align}
> $$
> has the solution
> $$
> \begin{align}
> u(r, \theta) = (r^2 - a^2)\int_0^{2\pi}\frac{h(\phi)}{a^2 - 2ar\cos(\theta - \phi) + r^2}\,\frac{d\phi}{2\pi}, \qquad r > a .
> \end{align}
> $$

Here boundedness at infinity is the "boundary condition" at $r = \infty$: among the separated solutions of the [[Laplace Equation in a Disk]], it rejects $r^n$ ($n \ge 1$) and $\log r$, leaving $u = \tfrac12 A_0 + \sum_{n \ge 1} r^{-n}(A_n\cos n\theta + B_n\sin n\theta)$, whose sum is the exterior form of [[Poisson's Formula]].[^3]

# Properties
- Without the boundedness condition the solution is not unique (e.g. add $\log(r/a)$), so the [[Laplace Equation Dirichlet Problem Uniqueness|uniqueness]] argument for bounded domains needs this extra condition.[^3]
- Equivalent to the interior problem by the inversion $r \mapsto a^2/r$, which preserves harmonicity in 2D (Kelvin transform).[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=186&annotation=AIQLMDNW)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=187&annotation=BMNU3H3W)
[^3]: Added from general knowledge.
