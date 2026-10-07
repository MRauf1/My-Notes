---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Heat Equation[^1]
> For the temperature $u(\mathbf{x}, t)$ of a body with specific heat $c$, density $\rho$, and thermal conductivity $\kappa$,
> $$
> \begin{align}
> c \rho \, u_t = \nabla \cdot (\kappa \nabla u).
> \end{align}
> $$
> If $c, \rho, \kappa$ are constant, it is the [[Diffusion Equation]] $u_t = k \Delta u$ with diffusivity $k = \kappa / (c\rho)$.

# Properties
- A special case of the [[Diffusion Equation]], with heat playing the role of the diffusing substance.
- Derived from conservation of heat energy plus Fourier's law (heat flux $= -\kappa \nabla u$) and the divergence theorem.
- [[Parabolic Partial Differential Equation|Parabolic]].
- Typical [[Boundary Condition|boundary conditions]]: perfect insulation is a homogeneous [[Neumann Boundary Condition]]; contact with a reservoir of temperature $g(t)$ is a [[Dirichlet Boundary Condition]]; Newton's law of cooling at the boundary is a [[Robin Boundary Condition]].
- Steady-state temperatures satisfy the [[Laplace Equation]].
- Inherits every property of the [[Diffusion Equation]]: a hot spot spreads as the Gaussian [[Diffusion Kernel (Partial Differential Equations)|diffusion kernel]] (the "heat kernel"); without internal sources the hottest and coldest points occur only initially or on the boundary ([[Maximum Principle (Diffusion Equation)]]); heat flow is irreversible ([[Diffusion Equation Well-Posedness]]); and heat propagates with infinite speed, unlike waves ([[Wave and Diffusion Equation Comparison]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=28&annotation=R38K4VFI)
