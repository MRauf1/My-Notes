---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Diffusion Equation on the Half-Line[^1][^2][^3][^4]
> **Dirichlet problem.** $v_t - k v_{xx} = 0$ for $0 < x < \infty$, $0 < t < \infty$, with $v(x, 0) = \phi(x)$ and $v(0, t) = 0$, has the unique solution
> $$
> \begin{align}
> v(x, t) = \frac{1}{\sqrt{4\pi k t}} \int_0^\infty \left[e^{-(x - y)^2/4kt} - e^{-(x + y)^2/4kt}\right] \phi(y)\, dy.
> \end{align}
> $$
> **Neumann problem.** $w_t - k w_{xx} = 0$, $w(x, 0) = \phi(x)$, $w_x(0, t) = 0$, has the solution
> $$
> \begin{align}
> w(x, t) = \frac{1}{\sqrt{4\pi k t}} \int_0^\infty \left[e^{-(x - y)^2/4kt} + e^{-(x + y)^2/4kt}\right] \phi(y)\, dy.
> \end{align}
> $$

Physically, $v$ is the temperature in a very long rod with insulated sides and one end held in a reservoir at temperature zero; $w$ is the same rod with its end insulated.[^2]

**Derivation.** Apply the [[Method of Reflection]]: solve the whole-line problem with the odd (Dirichlet) or even (Neumann) extension of $\phi$ via the [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]], then split $\int_{-\infty}^0$ and substitute $y \mapsto -y$. The bracket is the half-line Green's function $S(x - y, t) \mp S(x + y, t)$: the source at $y$ plus a mirror source at $-y$ of opposite (Dirichlet) or equal (Neumann) strength.

# Properties
- Uniqueness follows from the energy/[[Maximum Principle (Diffusion Equation)|maximum principle]] arguments of [[Diffusion Equation Well-Posedness]].
- The PDE holds in the open quarter-plane; the boundary and initial conditions are imposed on its two edges.
- With a source $f(x, t)$, reflect $f$ in the same way and use [[Duhamel's Principle]] ([[Inhomogeneous Diffusion Equation]]); with a boundary source $v(0, t) = h(t)$ or $w_x(0, t) = h(t)$, first apply the [[Boundary Condition Subtraction Device]].
- If $\phi(0) \neq h(0)$ for the Dirichlet data $h$, the solution is discontinuous at the corner $(0, 0)$ only (a hot bar suddenly plunged into a cold bath).[^5]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=69&annotation=3R9NGU2J)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=69&annotation=RIPUIRIW)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=71&annotation=8ILG9GFG)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=71&annotation=3B962JD3); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=72&annotation=9U858KCX)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=82&annotation=UPGKLY8Q)
