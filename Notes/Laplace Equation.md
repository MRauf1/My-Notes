---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation[^1]
> $$
> \begin{align}
> \Delta u = u_{x_1 x_1} + \cdots + u_{x_n x_n} = 0,
> \end{align}
> $$
> where $\Delta$ is the [[Laplacian Operator]]. Its solutions are called [[Harmonic Function|harmonic functions]].

# Types
- The inhomogeneous version $\Delta u = f$ is the Poisson equation.

# Properties
- Describes the steady state ($u_t = u_{tt} = 0$) of the [[Wave Equation]], [[Diffusion Equation]], and [[Heat Equation]].
- [[Elliptic Partial Differential Equation|Elliptic]]; it is the canonical form of every elliptic equation up to lower-order terms.
- Has no time variable, so it is supplemented only by [[Boundary Condition|boundary conditions]], not [[Initial Condition|initial conditions]].
- Solved without a mesh by [[Walk on Spheres]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=29&annotation=NHXUN49P)
