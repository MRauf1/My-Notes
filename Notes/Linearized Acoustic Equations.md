---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Linearized Acoustic Equations[^1]
> Small disturbances of air with velocity $\mathbf{v}(\mathbf{x}, t)$ and density $\rho(\mathbf{x}, t)$ satisfy the linear system of four scalar equations
> $$
> \begin{align}
> \frac{\partial \mathbf{v}}{\partial t} + \frac{c_0^2}{\rho_0} \nabla \rho &= 0, \\
> \frac{\partial \rho}{\partial t} + \rho_0 \nabla \cdot \mathbf{v} &= 0,
> \end{align}
> $$
> where $\rho_0$ is the density and $c_0$ the speed of sound in still air. They are the linearization of the nonlinear equations of gas dynamics.

# Properties
- If the flow is irrotational ($\nabla \times \mathbf{v} = 0$, no sound "eddies"), then $\rho$ and each component of $\mathbf{v}$ satisfy the [[Wave Equation]] $\partial_t^2 \rho = c_0^2 \Delta \rho$, $\partial_t^2 \mathbf{v} = c_0^2 \Delta \mathbf{v}$.[^2]
- Irrotational $\mathbf{v}$ has a velocity potential $\psi$ with $\mathbf{v} = -\nabla \psi$ ([[Conservative Vector Field]]), which also satisfies the [[Wave Equation]].[^3]
- Boundary behavior: a rigid wall gives $\mathbf{v} \cdot \mathbf{n} = 0$, a homogeneous [[Neumann Boundary Condition]] on $\psi$; an open window gives the [[Dirichlet Boundary Condition]] $\rho = \rho_0$; a soft wall of acoustic impedance $Z$ gives the [[Robin Boundary Condition|Robin-type]] condition $\mathbf{v} \cdot \mathbf{n} = a(\rho - \rho_0)$ with $a \propto 1/Z$.[^4]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=35&annotation=EJTFKRI3)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=35&annotation=FCG3QCAC)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=35&annotation=JLCGZ3C3)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=35&annotation=EBDLQKHF)
