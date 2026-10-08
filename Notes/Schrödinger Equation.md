---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Schrödinger Equation[^1]
> The complex-valued wave function $u(\mathbf{x}, t)$ of a particle of mass $m$ in a potential $V(\mathbf{x})$ satisfies, on all of space $\mathbb{R}^3$,
> $$
> \begin{align}
> i\hbar \, u_t = -\frac{\hbar^2}{2m} \Delta u + V(\mathbf{x}) u, \qquad \iiint_{\mathbb{R}^3} |u|^2 \, d\mathbf{x} = 1,
> \end{align}
> $$
> where $\hbar$ is Planck's constant divided by $2\pi$ and $\Delta$ is the [[Laplacian Operator]]. For an electron (charge $-e$) about a nucleus of atomic number $Z$ at the origin (hydrogen: $Z = 1$), $V = -\dfrac{Z e^2}{r}$ in Gaussian units ($-\dfrac{Z e^2}{4\pi\varepsilon_0 r}$ in SI), $r = |\mathbf{x}|$.

# Properties
- Linear, homogeneous, first order in time and second order in space, with complex coefficient $i$.
- Needs one [[Initial Condition]] $u(\mathbf{x}, t_0) = \phi(\mathbf{x})$.
- Posed on all of space, so there is no boundary; the normalization $\int |u|^2 = 1$ replaces [[Boundary Condition|boundary conditions]] and makes $|u|^2$ a [[Probability Density Function]] of the particle's position.
- On an interval $u_t = i u_{xx}$ separates into $T = e^{-i\lambda t}$ times the same spatial [[Eigenfunction|eigenfunctions]] as diffusion, e.g. $u = \tfrac12 A_0 + \sum A_n e^{-i(n\pi/l)^2 t}\cos\frac{n\pi x}{l}$ with Neumann conditions ([[Separation of Variables]]).[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=29&annotation=QB56EPAP)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=104&annotation=XLES3PT5)
