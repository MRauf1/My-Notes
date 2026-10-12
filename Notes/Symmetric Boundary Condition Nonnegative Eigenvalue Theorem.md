---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!abstract] Theorem (No Negative Eigenvalues)[^1]
> Assume [[Symmetric Boundary Condition|symmetric boundary conditions]] on $(a, b)$. If
> $$
> \begin{align}
> f(x) f'(x) \Big|_{x=a}^{x=b} \leq 0
> \end{align}
> $$
> for all real-valued functions $f$ satisfying the boundary conditions, then $-X'' = \lambda X$ has no negative eigenvalue.

# Properties
- The hypothesis holds for [[Dirichlet Boundary Condition|Dirichlet]], [[Neumann Boundary Condition|Neumann]], and [[Periodic Boundary Condition|periodic]] conditions, so these have no negative eigenvalues; it fails for certain [[Robin Boundary Condition|Robin]] conditions, which can have negative eigenvalues ([[Robin Eigenvalue Problem on an Interval]]).[^1]
- The sign of the eigenvalues is controlled by the [[Dirichlet Energy]] $\int_a^b |X'|^2$ together with the boundary term, the analogue of a positive semidefinite matrix having nonnegative eigenvalues.[^2]
- Consequence for evolution problems: no exponentially growing modes in [[Separation of Variables]], so diffusion solutions stay bounded.

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=134&annotation=88LI94RD)
[^2]: Added from general knowledge.
