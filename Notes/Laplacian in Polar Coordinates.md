---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplacian in Polar Coordinates[^1][^2]
> In [[Polar Coordinate System|polar coordinates]] $x = r\cos\theta$, $y = r\sin\theta$, the two-dimensional [[Laplacian Operator]] is
> $$
> \begin{align}
> \Delta_2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} = \frac{\partial^2}{\partial r^2} + \frac{1}{r}\frac{\partial}{\partial r} + \frac{1}{r^2}\frac{\partial^2}{\partial \theta^2} = \frac{1}{r}\frac{\partial}{\partial r}\!\left(r\frac{\partial}{\partial r}\right) + \frac{1}{r^2}\frac{\partial^2}{\partial\theta^2}.
> \end{align}
> $$

The simple form is suggested by the [[Laplacian Operator Rigid Motion Invariance|rotational invariance]] of $\Delta$: rotations act on polar coordinates only by shifting $\theta$, so $\theta$ enters only through $\partial_\theta^2$.[^1]

# Properties
- Derived by the chain rule from [[Cartesian and Polar Coordinate System Change]].
- Functions independent of $\theta$ reduce $\Delta u = 0$ to the ODE $u_{rr} + u_r/r = 0$, giving $u = c_1 \log r + c_2$ ([[Radial Harmonic Function]]).
- Separating $u = R(r)\Theta(\theta)$ gives an Euler-type ODE in $r$ and a periodic eigenvalue problem in $\theta$: [[Laplace Equation in a Disk]], [[Laplace Equation in a Wedge]], [[Laplace Equation in an Annulus]], [[Laplace Equation in the Exterior of a Circle]].
- 3D counterpart: [[Laplacian in Spherical Coordinates]]. In [[Cylindrical Coordinate System|cylindrical coordinates]] add $\partial_z^2$.[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=168&annotation=MI5DM93G)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=169&annotation=IRZ27E66)
[^3]: Added from general knowledge.
