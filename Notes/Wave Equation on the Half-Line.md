---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Wave Equation on the Half-Line[^1][^2][^3]
> The Dirichlet problem
> $$
> \begin{align}
> v_{tt} - c^2 v_{xx} = 0 \ (0 < x < \infty), \quad v(x, 0) = \phi(x), \quad v_t(x, 0) = \psi(x), \quad v(0, t) = 0
> \end{align}
> $$
> has, for $t > 0$, the solution
> $$
> \begin{align}
> v(x, t) =
> \begin{cases}
> \dfrac{1}{2}\left[\phi(x + ct) + \phi(x - ct)\right] + \dfrac{1}{2c}\displaystyle\int_{x - ct}^{x + ct} \psi(y)\, dy, & x > ct, \[2ex]
> \dfrac{1}{2}\left[\phi(ct + x) - \phi(ct - x)\right] + \dfrac{1}{2c}\displaystyle\int_{ct - x}^{ct + x} \psi(y)\, dy, & 0 < x < ct.
> \end{cases}
> \end{align}
> $$

**Interpretation.** Derived by the [[Method of Reflection]] (odd extensions of $\phi, \psi$ plugged into [[D'Alembert's Formula]]). The characteristic $x = ct$ from the corner splits the quarter-plane in two. For $x > ct$ the boundary has not yet been felt and the solution is the whole-line one. For $0 < x < ct$, the backward characteristic $x - ct$ hits the wall: the left-moving wave is reflected at $x = 0$ with its sign flipped, so $\phi(x - ct)$ is replaced by $-\phi(ct - x)$ and the part of the $\psi$ integral over negative $y$ cancels against its mirror image.

**Inhomogeneous problem.**[^4] For $v_{tt} - c^2 v_{xx} = f(x, t)$ on $0 < x < \infty$ with $v(x, 0) = \phi$, $v_t(x, 0) = \psi$, $v(0, t) = h(t)$, the solution is the sum of four terms, one for each datum $\phi, \psi, f, h$:
- For $x > ct > 0$: the whole-line formula of the [[Inhomogeneous Wave Equation]], with the backward characteristic triangle as [[Domain of Dependence]].
- For $0 < x < ct$:
$$
\begin{align}
v(x, t) = (\phi \text{ term}) + (\psi \text{ term}) + h\!\left(t - \frac{x}{c}\right) + \frac{1}{2c} \iint_D f,
\end{align}
$$
where the $\phi, \psi$ terms are as above, $t - x/c$ is the time at which the backward characteristic through $(x, t)$ hits the wall (the reflection point), and $D$ is the quadrilateral with vertices $(x, t)$, $(0, t - x/c)$, $(ct - x, 0)$, $(x + ct, 0)$: the backward characteristic triangle with the part beyond the wall cut off by the characteristic leaving the reflection point.

# Properties
- The compatibility conditions $\phi(0) = h(0)$ and $\psi(0) = h'(0)$ are needed; otherwise a singularity propagates along the characteristic $x = ct$ emanating from the corner (singularities are not smoothed, see [[Wave and Diffusion Equation Comparison]]).[^4]
- Boundary data enter only through the retarded value $h(t - x/c)$: the wall's signal travels inward at speed $c$ ([[Principle of Causality (Wave Equation)]]).
- On a bounded interval, repeated reflections at both ends give [[Wave Equation on a Finite Interval]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=73&annotation=A9AICGQZ)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=74&annotation=NJ8DIFLQ)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=74&annotation=UVMYJDRL)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=90&annotation=MIIEKN33)
