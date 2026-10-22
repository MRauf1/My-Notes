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
- The inhomogeneous version $\Delta u = f$ is the [[Poisson Equation]].
- In one dimension $u_{xx} = 0$, whose solutions are linear functions; in two and three dimensions the interesting part is the geometry of the domain.[^2]

# Properties
- Describes the steady state ($u_t = u_{tt} = 0$) of the [[Wave Equation]], [[Diffusion Equation]], and [[Heat Equation]].
- [[Elliptic Partial Differential Equation|Elliptic]]; it is the canonical form of every elliptic equation up to lower-order terms.
- Has no time variable, so it is supplemented only by [[Boundary Condition|boundary conditions]], not [[Initial Condition|initial conditions]].
- Solved without a mesh by [[Walk on Spheres]].
- Solution set invariant under rigid motions ([[Laplacian Operator Rigid Motion Invariance]]).
- [[Maximum Principle (Laplace Equation)]], [[Laplace Equation Dirichlet Problem Uniqueness]], [[Mean Value Property (Harmonic Function)]], [[Harmonic Function Smoothness]].
- Rotation-invariant solutions: [[Radial Harmonic Function]].
- Special geometries by [[Separation of Variables]]: [[Laplace Equation in a Rectangle]], [[Laplace Equation in a Box]], [[Laplace Equation in a Disk]] ([[Poisson's Formula]]), [[Laplace Equation in a Wedge]], [[Laplace Equation in an Annulus]], [[Laplace Equation in the Exterior of a Circle]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=29&annotation=NHXUN49P); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=164&annotation=CH6QLZ9F)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=166&annotation=2ULRT7HJ)
