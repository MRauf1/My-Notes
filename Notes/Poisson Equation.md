---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Poisson Equation[^1]
> The inhomogeneous version of the [[Laplace Equation]]:
> $$
> \begin{align}
> \Delta u = f,
> \end{align}
> $$
> where $\Delta$ is the [[Laplacian Operator]] and $f$ is a given function (the source term).

**Boundary value problem.**[^2] The basic problem is to solve the Poisson (or Laplace) equation in a domain $D$ with one condition on $\partial D$:
$$
\begin{align}
\Delta u = f \ \text{in } D, \qquad u = h \quad \text{or} \quad \frac{\partial u}{\partial n} = h \quad \text{or} \quad \frac{\partial u}{\partial n} + a u = h \ \text{on } \partial D,
\end{align}
$$
i.e. a [[Dirichlet Boundary Condition|Dirichlet]], [[Neumann Boundary Condition|Neumann]], or [[Robin Boundary Condition|Robin]] problem. In one dimension the only connected domain is an interval and the problem is an ODE; in two and three dimensions the interesting part is the geometry of $D$.

# Properties
- [[Elliptic Partial Differential Equation]]; time-independent (steady-state) version of the [[Inhomogeneous Diffusion Equation]].
- The Dirichlet problem has at most one solution ([[Laplace Equation Dirichlet Problem Uniqueness]]).
- In electrostatics $-\Delta V = \rho/\varepsilon_0$ relates the [[Electric Potential]] to the charge density; the potential of a point charge is a [[Radial Harmonic Function]].[^3]
- Solved without a mesh by [[Walk on Spheres]] with a source-term correction.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=164&annotation=RCUL6WIV)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=166&annotation=2ULRT7HJ)
[^3]: Added from general knowledge.
