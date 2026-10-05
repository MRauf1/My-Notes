---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Neumann Boundary Condition[^1]
> The [[Normal Derivative]] of $u$ is specified on the boundary:
> $$
> \begin{align}
> \frac{\partial u}{\partial n}(\mathbf{x}, t) = \mathbf{n} \cdot \nabla u = g(\mathbf{x}, t), \qquad \mathbf{x} \in \partial D.
> \end{align}
> $$
> Homogeneous if $g \equiv 0$.

# Properties
- A type of [[Boundary Condition]].
- Prescribes the flux through the boundary; the homogeneous condition $\partial u/\partial n = 0$ means no flux (a sealed container by Fick's law, a perfectly insulated body, a string end free to slide without resistance, a rigid wall in acoustics).[^2]
- Counterpart of the [[Dirichlet Boundary Condition]]; the $a = 0$ case of the [[Robin Boundary Condition]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=33&annotation=75AFYIDW)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=34&annotation=HISV8T4R)
