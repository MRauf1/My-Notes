---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Boundary Condition[^1]
> For a [[Partial Differential Equation]] valid in a domain $D$ with boundary $\partial D$, a boundary condition is an auxiliary condition prescribing $u$ and/or its derivatives on $\partial D$, required to hold for all $t$ and all $\mathbf{x} \in \partial D$. Written as an equation with given boundary datum $g(\mathbf{x}, t)$, it is homogeneous if $g \equiv 0$ and inhomogeneous otherwise.[^2]

Together with [[Initial Condition|initial conditions]], boundary conditions single out one solution among the many (arbitrary-function families of) solutions a PDE typically has, aiming at a [[Well-Posed Problem]].

# Types
- [[Dirichlet Boundary Condition]]: $u = g$.
- [[Neumann Boundary Condition]]: $\partial u / \partial n = g$.
- [[Robin Boundary Condition]]: $\partial u / \partial n + a u = g$.
- Mixed condition: Dirichlet on part of the boundary, Neumann on the rest ([[Mixed Eigenvalue Problem on an Interval]]).
- Radiation/absorbing condition (wave equation): $\dfrac{\partial u}{\partial n} + b \dfrac{\partial u}{\partial t} = 0$; energy is radiated to ($b > 0$) or absorbed from ($b < 0$) the exterior through the boundary.[^3]
- Conditions at infinity: when $D$ is unbounded, physics prescribes the behavior of $u$ as $|\mathbf{x}| \to \infty$.[^4]
- Jump (interface) conditions: when $D = D_1 \cup D_2$ consists of parts with different physical properties, conditions relate $u$ and its fluxes across the interface.[^4]

# Properties
- The domain may have no boundary (e.g. all of $\mathbb{R}^3$ for the [[Schrödinger Equation]]), in which case no boundary condition is imposed.
- Expressed with the [[Normal Derivative]] $\partial u/\partial n = \mathbf{n} \cdot \nabla u$, $\mathbf{n}$ the outward unit normal.
- Can couple several unknowns: the components of the electromagnetic field each satisfy the [[Wave Equation]] separately but are coupled through boundary conditions.
- Inhomogeneous boundary conditions can be made homogeneous by the [[Boundary Condition Subtraction Device]], at the cost of modified source and initial data.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=32&annotation=FYN9I4HD)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=33&annotation=75AFYIDW)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=36&annotation=S8RV9HC5)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=36&annotation=NK7YD3NH)
