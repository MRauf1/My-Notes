---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Wave Equation[^1]
> The [[Second Order Partial Differential Equation]] for $u(\mathbf{x}, t)$, $\mathbf{x} \in \mathbb{R}^n$,
> $$
> \begin{align}
> u_{tt} = c^2 \Delta u = c^2 (u_{x_1 x_1} + \cdots + u_{x_n x_n}),
> \end{align}
> $$
> where $\Delta$ is the [[Laplacian Operator]] and $c > 0$ is the wave speed. For a vibrating string or membrane of tension $T$ and density $\rho$, $c = \sqrt{T / \rho}$.

# Types
- One-dimensional ($u_{tt} = c^2 u_{xx}$): vibrating string.
- Two-dimensional ($u_{tt} = c^2(u_{xx} + u_{yy})$): vibrating drumhead.
- Three-dimensional ($u_{tt} = c^2(u_{xx} + u_{yy} + u_{zz})$): sound, light, simple 3D vibrations.
- [[Damped Wave Equation]] (resistance term $r u_t$)
- [[Klein-Gordon Equation]] (restoring term $k u$)
- [[Inhomogeneous Wave Equation]] (external force $f(\mathbf{x}, t)$)
- [[Linearized Acoustic Equations]] (sound reduces to the wave equation)

# Properties
- [[Hyperbolic Partial Differential Equation|Hyperbolic]]: coefficient matrix $\operatorname{diag}(1, -c^2, \dots, -c^2)$ in $(t, \mathbf{x})$.
- Needs two [[Initial Condition|initial conditions]], position $u(\mathbf{x}, t_0) = \phi(\mathbf{x})$ and velocity $u_t(\mathbf{x}, t_0) = \psi(\mathbf{x})$, since it is second order in time.
- Each component of the electric and magnetic fields in vacuum satisfies the 3D wave equation (with $c$ the speed of light); the components are coupled only through the [[Boundary Condition|boundary conditions]].
- Time-independent solutions satisfy the [[Laplace Equation]].
- Derived from Newton's second law: in 2D/3D, $\rho u_{tt} = \nabla \cdot (T \nabla u)$, which gives the above when $T$ is constant.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=24&annotation=JFPEHEK3)
