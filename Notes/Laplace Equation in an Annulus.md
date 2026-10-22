---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation in an Annulus[^1][^2]
> The Dirichlet problem
> $$
> \begin{align}
> u_{xx} + u_{yy} = 0 \ \text{ in } a^2 < x^2 + y^2 < b^2, \qquad u = g(\theta) \ \text{ on } r = a, \qquad u = h(\theta) \ \text{ on } r = b
> \end{align}
> $$
> has the solution
> $$
> \begin{align}
> u(r, \theta) = \tfrac{1}{2}\big(C_0 + D_0\log r\big) + \sum_{n=1}^\infty \Big[\big(C_n r^n + D_n r^{-n}\big)\cos n\theta + \big(A_n r^n + B_n r^{-n}\big)\sin n\theta\Big],
> \end{align}
> $$
> with the coefficients determined by setting $r = a$ and $r = b$.

The separated solutions are those of the [[Laplace Equation in a Disk]], but $r^{-n}$ and $\log r$ are kept because they are finite in the annulus. Matching the [[Fourier Series]] of $g$ and $h$ gives, for each mode, two linear equations in two unknowns.

# Properties
- The $\log r$ term is the [[Radial Harmonic Function]]; it carries the net flux through the annulus.[^3]
- One of the domains bounded by concentric circles and rays on which polar [[Separation of Variables]] works.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=186&annotation=EQDJTJDM)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=186&annotation=UIQMPJDG)
[^3]: Added from general knowledge.
