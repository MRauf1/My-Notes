---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Second Order Linear Partial Differential Equation (Constant Coefficients)[^1]
> In $n$ variables $x_1, \dots, x_n$,
> $$
> \begin{align}
> \sum_{i,j=1}^n a_{ij} u_{x_i x_j} + \sum_{i=1}^n a_i u_{x_i} + a_0 u = 0,
> \end{align}
> $$
> with real constants $a_{ij}, a_i, a_0$. Since $u_{x_i x_j} = u_{x_j x_i}$, the coefficient matrix $A = (a_{ij})$ can be taken symmetric. In two variables,[^2]
> $$
> \begin{align}
> a_{11} u_{xx} + 2a_{12} u_{xy} + a_{22} u_{yy} + a_1 u_x + a_2 u_y + a_0 u = 0.
> \end{align}
> $$

The type is determined by the signs of the [[Eigenvalue|eigenvalues]] of $A$, mirroring the [[Conic Section|conic sections]]: $x^2 + y^2 = 1$ is an [[Ellipse]], $x^2 - y^2 = 1$ a [[Hyperbola]], and the [[Parabola]] lies in between.

# Types
- [[Elliptic Partial Differential Equation]]: all eigenvalues of $A$ of one sign (2D: $a_{12}^2 < a_{11} a_{22}$).
- [[Hyperbolic Partial Differential Equation]]: no zero eigenvalue, exactly one of opposite sign (2D: $a_{12}^2 > a_{11} a_{22}$).
- [[Parabolic Partial Differential Equation]]: exactly one zero eigenvalue, the rest of one sign (2D: $a_{12}^2 = a_{11} a_{22}$, $A \neq 0$).
- [[Ultrahyperbolic Partial Differential Equation]]: no zero eigenvalue, at least two positive and at least two negative (needs $n \geq 4$).

# Properties
- [[Canonical Form of Second Order Linear Partial Differential Equation]]: a linear change of variables reduces it to a diagonal coefficient matrix, so the [[Laplace Equation]], [[Wave Equation]], and [[Diffusion Equation]] are the prototypes of the elliptic, hyperbolic, and parabolic types.
- Only the second-order (principal) part determines the type.
- With variable coefficients $a_{ij}(\mathbf{x})$, the type is defined pointwise and may change between regions (elliptic in one region, hyperbolic in another).[^3]
- Special case of [[Second Order Partial Differential Equation]] and of [[Homogeneous Linear Partial Differential Equation]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=41&annotation=EGUYETDZ)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=40&annotation=YT4T6YJM)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=43&annotation=WYKFAFVX)
