---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition

Find a special direction ([[Curve]] in general) along which a [[Partial Differential Equation]] is an [[Ordinary Differential Equation]].

> [!info] Geometric Method[^1]
> The [[First Order Partial Differential Equation]]
> $$
> \begin{align}
> a(x, y) u_x + b(x, y) u_y = 0
> \end{align}
> $$
> states that the [[Directional Derivative]] of $u$ along $(a, b)$ is zero, so $u$ is constant along the [[Characteristic Curve|characteristic curves]], the solutions of the ODE
> $$
> \begin{align}
> \frac{dy}{dx} = \frac{b(x, y)}{a(x, y)}.
> \end{align}
> $$
> If these are the level sets $\xi(x, y) = C$, the general solution is $u = f(\xi(x, y))$ with $f$ an arbitrary function of one variable. For constant $a, b$: $u = f(bx - ay)$.

If the ODE can be solved, so can the PDE.

Equivalent to the [[Coordinate Change Method]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=21&annotation=WWKHCIM8)
