---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Inhomogeneous Linear Partial Differential Equation[^1]
> A [[Partial Differential Equation]] of the form
> $$
> \begin{align}
> \mathcal{L}u = g,
> \end{align}
> $$
> where $\mathcal{L}$ is a [[Linear Partial Differential Operator]] and $g \neq 0$ is a given function of the [[Independent Variable|independent variables]] (the source or forcing term).

# Properties
- If $u_p$ solves $\mathcal{L}u = g$ and $u_h$ solves the [[Homogeneous Linear Partial Differential Equation]] $\mathcal{L}u = 0$, then $u_p + u_h$ solves $\mathcal{L}u = g$, since $\mathcal{L}(u_p + u_h) = g + 0$.[^2]
- Conversely, the difference of two solutions of $\mathcal{L}u = g$ solves $\mathcal{L}u = 0$. Hence the full solution set is the affine space $u_p + \ker \mathcal{L}$ (cf. [[Kernel Vector Subspace]]).
- Can be of any order.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=14&annotation=WFHSAPYJ)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=15&annotation=B4BVPKE6)
