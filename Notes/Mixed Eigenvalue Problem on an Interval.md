---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Mixed Eigenvalue Problem on an Interval[^1]
> A **mixed** boundary condition is Dirichlet at one end and Neumann at the other. For $u(0, t) = u_x(l, t) = 0$ the [[Eigenfunction|eigenvalue problem]]
> $$
> \begin{align}
> -X'' = \lambda X, \qquad X(0) = X'(l) = 0
> \end{align}
> $$
> has the eigenvalues and eigenfunctions
> $$
> \begin{align}
> \lambda_n = \frac{\left(n + \tfrac12\right)^2 \pi^2}{l^2}, \qquad X_n(x) = \sin\frac{\left(n + \tfrac12\right)\pi x}{l}, \qquad n = 0, 1, 2, \dots
> \end{align}
> $$

The free end makes the interval act like a quarter-wavelength resonator: the lowest mode is a quarter sine wave, and only odd harmonics of the fundamental appear (as in a closed–open pipe).[^2]

# Properties
- All eigenvalues are positive: $\lambda\int|X|^2 = \int|X'|^2$ ([[Dirichlet Energy]]) and the Dirichlet end excludes constants.[^2]
- Interlaces the pure problems: $\lambda_n^{\text{Neumann}} < \lambda_n^{\text{mixed}} < \lambda_n^{\text{Dirichlet}}$, consistent with min–max monotonicity (each Dirichlet end raises the spectrum), indexing all three from $n = 0$.[^2]
- Equivalently, the Dirichlet problem on $(0, 2l)$ restricted to modes even about $x = l$ ([[Method of Reflection]]).[^2]
- Siblings: [[Dirichlet Eigenvalue Problem on an Interval]], [[Neumann Eigenvalue Problem on an Interval]], [[Robin Eigenvalue Problem on an Interval]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=103&annotation=AVGK6P9J)
[^2]: Added from general knowledge.
