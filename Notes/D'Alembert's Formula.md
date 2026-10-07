---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] D'Alembert's Formula[^1][^2][^3]
> The 1D [[Wave Equation]] factors into two [[Transport Equation|transport operators]],
> $$
> \begin{align}
> u_{tt} - c^2 u_{xx} = \left(\frac{\partial}{\partial t} - c\frac{\partial}{\partial x}\right)\left(\frac{\partial}{\partial t} + c\frac{\partial}{\partial x}\right) u = 0,
> \end{align}
> $$
> so its general solution on $-\infty < x < \infty$ is
> $$
> \begin{align}
> u(x, t) = f(x + ct) + g(x - ct)
> \end{align}
> $$
> for arbitrary twice-differentiable $f, g$. The [[Initial Condition|initial-value problem]] $u(x, 0) = \phi(x)$, $u_t(x, 0) = \psi(x)$ has exactly one solution (d'Alembert, 1746):
> $$
> \begin{align}
> u(x, t) = \frac{1}{2}\left[\phi(x + ct) + \phi(x - ct)\right] + \frac{1}{2c}\int_{x - ct}^{x + ct} \psi(s)\, ds.
> \end{align}
> $$
> If $\phi \in C^2$ and $\psi \in C^1$, then $u \in C^2$ is a genuine solution.

**Interpretation: a 1D wave is two shapes sliding in opposite directions.** $g(x - ct)$ is a rigid profile of arbitrary shape moving right at speed $c$; $f(x + ct)$ is another moving left at speed $c$. Nothing else can happen: the wave equation does not deform shapes, it only transports them along the two families of [[Characteristic Curve|characteristic lines]] $x \pm ct = \text{const}$.[^2]
- An initial **position** $\phi$ splits into two copies of half the amplitude, one going each way at exactly speed $c$.
- An initial **velocity** $\psi$ produces a wave spreading out at speed $\le c$ in both directions: part of it can lag behind, but nothing outruns $c$ ([[Principle of Causality (Wave Equation)]]).[^4]

**In higher dimensions the wave moves in every direction.** For $u_{tt} = c^2 \Delta u$ in $\mathbb{R}^n$, the analogue of $g(x - ct)$ is a plane wave $F(\mathbf{k} \cdot \mathbf{x} - ct)$ for any unit vector $\mathbf{k}$, a planar profile travelling rigidly in direction $\mathbf{k}$ at speed $c$. The two directions $\pm$ of the line become the whole sphere of directions $\mathbf{k} \in S^{n-1}$, and a general solution is a superposition of plane waves over all directions. Equivalently, a point disturbance spreads as an expanding sphere (circle in 2D) of radius $ct$. Unlike 1D, the profile does not keep its shape: in 3D, radial solutions are $u = \frac{1}{r}\left[f(r + ct) + g(r - ct)\right]$, so the amplitude decays like $1/r$ as the energy spreads over a growing sphere. The $n$-D replacements for d'Alembert's formula are Kirchhoff's formula (3D, averages of the data over the sphere $|\mathbf{y} - \mathbf{x}| = ct$) and Poisson's formula (2D, averages over the disk $|\mathbf{y} - \mathbf{x}| \le ct$); see [[Huygens's Principle]].

# Properties
- Uniqueness and existence plus continuous dependence on $(\phi, \psi)$ make the problem a [[Well-Posed Problem]], both forward and backward in time.
- Obtained by solving the two first-order factors in turn, or by changing to characteristic coordinates $\xi = x + ct$, $\eta = x - ct$, in which the equation becomes $u_{\xi\eta} = 0$.
- $u(x, t)$ depends on $\phi$ only at the two points $x \pm ct$ and on $\psi$ only on $[x - ct, x + ct]$ ([[Domain of Dependence]]).
- Singularities (kinks, jumps) of $\phi$ are not smoothed out; they travel along the characteristics at speed $c$ ([[Wave and Diffusion Equation Comparison]]).
- Working on the whole line is justified physically by finite propagation speed: far from a boundary, the boundary's effect takes time to arrive, and until then the whole-line solution is valid.[^5]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=45&annotation=L3DTZCH6); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=46&annotation=M4946FM9)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=46&annotation=DKN9IJ9K)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=47&annotation=HZNBDQ8D); [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=48&annotation=2T8MJY69)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=51&annotation=BPYUW8YS)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=45&annotation=JGSNR9QP)
