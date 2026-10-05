---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Diffusion Equation[^1]
> The [[Second Order Partial Differential Equation]] for a concentration $u(\mathbf{x}, t)$ with constant diffusion rate $k > 0$:
> $$
> \begin{align}
> u_t = k \Delta u = k(u_{x_1 x_1} + \cdots + u_{x_n x_n}),
> \end{align}
> $$
> where $\Delta$ is the [[Laplacian Operator]]. With a variable diffusion rate $k(\mathbf{x})$ and an external source/sink $f$, the general (inhomogeneous) diffusion equation is[^2]
> $$
> \begin{align}
> u_t = \nabla \cdot (k \nabla u) + f(\mathbf{x}, t).
> \end{align}
> $$

# Types
- [[Heat Equation]]

# Properties
- Derived from conservation of mass plus Fick's law (flux $= -k \nabla u$, from high to low concentration): $\iiint_D u_t \, d\mathbf{x} = \iint_{\partial D} k (\mathbf{n} \cdot \nabla u) \, dS$ for every region $D$, then the divergence theorem and the arbitrariness of $D$.
- [[Parabolic Partial Differential Equation|Parabolic]].
- Needs one [[Initial Condition]] $u(\mathbf{x}, t_0) = \phi(\mathbf{x})$ (the initial concentration), since it is first order in time.
- Also describes heat conduction, Brownian motion, and diffusion models of population dynamics.
- Time-independent solutions satisfy the [[Laplace Equation]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=27&annotation=YGPGPWDI)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=28&annotation=BGSR7MAA)
