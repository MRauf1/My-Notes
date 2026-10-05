---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Robin Boundary Condition[^1]
> A linear combination of the value and the [[Normal Derivative]] of $u$ is specified on the boundary:
> $$
> \begin{align}
> \frac{\partial u}{\partial n} + a u = g(\mathbf{x}, t), \qquad \mathbf{x} \in \partial D,
> \end{align}
> $$
> where $a(\mathbf{x}, t)$ is a given function. Homogeneous if $g \equiv 0$.

# Properties
- A type of [[Boundary Condition]].
- Models exchange with the exterior proportional to the difference of states: a string end attached to a spring obeying [[Hooke's Law]], or heat exchange with a reservoir by Newton's law of cooling, $\partial u/\partial n = -a(u - g)$, $a > 0$.[^2]
- Interpolates between the [[Neumann Boundary Condition]] ($a = 0$) and the [[Dirichlet Boundary Condition]] ($a \to \infty$).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=32&annotation=FYN9I4HD)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=34&annotation=SL6BMR9E)
