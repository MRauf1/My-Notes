---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Transport Equation[^1]
> The [[First Order Partial Differential Equation]] for $u(x, t)$
> $$
> \begin{align}
> u_t + c u_x = 0,
> \end{align}
> $$
> with constant speed $c$. More generally, in $n$ dimensions with constant velocity $\mathbf{b} \in \mathbb{R}^n$,
> $$
> \begin{align}
> u_t + \mathbf{b} \cdot \nabla u = 0.
> \end{align}
> $$

Models a substance (e.g. a pollutant of concentration $u$) carried by a fluid flowing at constant velocity with negligible diffusion.

# Properties
- General solution $u(x, t) = f(x - ct)$ (resp. $f(\mathbf{x} - t\mathbf{b})$), found by the [[Geometric Method]] or the [[Coordinate Change Method]]: the profile is translated rigidly at speed $c$ without changing shape.
- Each particle moves along a [[Characteristic Curve|characteristic line]] $x - ct = \text{const}$ in the $xt$-plane.
- Linear, homogeneous, constant coefficients ([[Homogeneous Linear Partial Differential Equation]]).
- Adding diffusion gives the advection–diffusion equation; see [[Diffusion Equation]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=22&annotation=XFIQ734M)
