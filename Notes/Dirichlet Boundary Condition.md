---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Dirichlet Boundary Condition[^1]
> The value of $u$ itself is specified on the boundary:
> $$
> \begin{align}
> u(\mathbf{x}, t) = g(\mathbf{x}, t), \qquad \mathbf{x} \in \partial D.
> \end{align}
> $$
> Homogeneous if $g \equiv 0$.

# Properties
- A type of [[Boundary Condition]].
- Physically: the state is held fixed at the boundary (a string with clamped ends, a body in perfect thermal contact with a reservoir of temperature $g(t)$, a container whose escaping substance is immediately washed away so $u = 0$).[^2]
- Counterpart of the [[Neumann Boundary Condition]]; both are limits of the [[Robin Boundary Condition]].
- A homogeneous Dirichlet condition at a point is enforced by odd extension ([[Method of Reflection]]); an inhomogeneous one is reduced to it by the [[Boundary Condition Subtraction Device]].
- Its eigenvalue problem on an interval gives sines and the [[Fourier Sine Series]] ([[Dirichlet Eigenvalue Problem on an Interval]]).

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=32&annotation=FYN9I4HD)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=34&annotation=SL6BMR9E)
