---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Method of Reflection[^1][^2]
> To solve a linear PDE whose whole-line solution is known (e.g. the [[Diffusion Equation]] or [[Wave Equation]]) on a domain with a homogeneous boundary condition at a point (say $x = 0$), [[Extension of Function|extend]] the initial data to the whole line so that the boundary condition is automatically satisfied, solve the whole-line problem, and restrict back:
> - **[[Dirichlet Boundary Condition|Dirichlet]]** $u(0, t) = 0$: use the **odd extension** $\phi_{\text{odd}}(x) = \phi(x)$ for $x > 0$, $-\phi(-x)$ for $x < 0$ (and $0$ at $x = 0$).
> - **[[Neumann Boundary Condition|Neumann]]** $u_x(0, t) = 0$: use the **even extension** $\phi_{\text{even}}(x) = \phi(|x|)$.
>
> On a finite interval $(0, l)$, reflect about both ends: the extension is odd (or even) about $x = 0$ and about $x = l$, hence $2l$-periodic.

**Why it works.** The PDE is invariant under $x \mapsto -x$, and whole-line solutions inherit the [[Parity of Function|parity]] of their data by uniqueness. An odd solution vanishes at $x = 0$; an even solution has $u_x(0, t) = 0$. So the boundary condition is enforced by symmetry rather than imposed. This is the 1D version of the **method of images**: the boundary is replaced by a mirror-image source of opposite sign (Dirichlet) or the same sign (Neumann).

# Properties
- Gives the half-line Green's functions $S(x - y, t) \mp S(x + y, t)$ for diffusion ([[Diffusion Equation on the Half-Line]]).
- For waves, the reflected part of the solution is a wave bouncing off the boundary, with a sign flip under Dirichlet ([[Wave Equation on the Half-Line]], [[Wave Equation on a Finite Interval]]).
- Extends to inhomogeneous equations (reflect $f$ as well) and, combined with the [[Boundary Condition Subtraction Device]], to inhomogeneous boundary conditions.
- Requires the boundary to be a symmetry of the operator: works for half-lines, intervals, half-spaces, but not general curved boundaries.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=69&annotation=3R9NGU2J)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=73&annotation=A9AICGQZ)
