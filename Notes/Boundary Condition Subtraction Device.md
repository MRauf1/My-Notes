---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Boundary Condition Subtraction Device[^1][^2][^3]
> To reduce a linear problem with an inhomogeneous [[Boundary Condition]] to one with a homogeneous boundary condition, subtract any simple function $H$ that satisfies the boundary condition, and solve for $V = v - H$, which satisfies the same PDE with a modified source and modified initial data.
>
> **Dirichlet, half-line.** For $v_t - k v_{xx} = f$, $v(0, t) = h(t)$, $v(x, 0) = \phi(x)$, let $V = v - h(t)$. Then
> $$
> \begin{align}
> V_t - k V_{xx} = f(x, t) - h'(t), \qquad V(0, t) = 0, \qquad V(x, 0) = \phi(x) - h(0).
> \end{align}
> $$
> **Neumann, half-line.** For $w_t - k w_{xx} = f$, $w_x(0, t) = h(t)$, $w(x, 0) = \phi(x)$, let $W = w - x h(t)$. Then
> $$
> \begin{align}
> W_t - k W_{xx} = f(x, t) - x h'(t), \qquad W_x(0, t) = 0, \qquad W(x, 0) = \phi(x) - x h(0).
> \end{align}
> $$

The new problem has a homogeneous boundary condition, so the [[Method of Reflection]] and [[Duhamel's Principle]] apply; recover $v = V + H$. The price is that boundary data are traded for interior source data ($-H_t + k H_{xx}$) and modified initial data ($-H(x, 0)$).

# Properties
- Works for any linear PDE, since the difference of solutions solves the problem with the differences of the data ([[Inhomogeneous Linear Partial Differential Equation]]).
- The choice of $H$ is free: it need only meet the boundary condition (e.g. a linear interpolant $H = h(t) + \frac{x}{l}[g(t) - h(t)]$ on an interval $(0, l)$ with $v(0) = h$, $v(l) = g$).
- The domain of $(x, t)$ is a quarter-plane with data on both edges; if $\phi(0) \neq h(0)$ the solution is discontinuous at the corner but continuous elsewhere (diffusion smooths the jump immediately for $t > 0$).[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=82&annotation=GV8D8JT5)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=82&annotation=GZN9RQNM)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=82&annotation=UPGKLY8Q)
