---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Coordinate Change Method[^1]
> To solve the constant-coefficient [[First Order Partial Differential Equation]]
> $$
> \begin{align}
> a u_x + b u_y = 0, \qquad (a, b) \neq (0, 0),
> \end{align}
> $$
> change variables to $x' = ax + by$, $y' = bx - ay$. By the [[Derivative Chain Rule|chain rule]], $u_x = a u_{x'} + b u_{y'}$ and $u_y = b u_{x'} - a u_{y'}$, so
> $$
> \begin{align}
> a u_x + b u_y = (a^2 + b^2) u_{x'} = 0 \implies u_{x'} = 0.
> \end{align}
> $$
> Hence $u = f(y') = f(bx - ay)$ for an arbitrary function $f$ of one variable.

The new axis $x'$ points along the [[Characteristic Curve|characteristic lines]], so in these coordinates the PDE collapses to an [[Ordinary Differential Equation]] in $x'$.

# Properties
- Gives the same answer as the [[Geometric Method]].
- Generalizes to variable coefficients by choosing $y'$ to be constant along the [[Characteristic Curve|characteristic curves]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=19&annotation=848QGNIL)
