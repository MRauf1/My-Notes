---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!abstract] Theorem (Real Eigenvalues)[^1]
> Under [[Symmetric Boundary Condition|symmetric (hermitian) boundary conditions]] with real constants, every eigenvalue $\lambda$ of $-X'' = \lambda X$ on $(a, b)$ is real. Furthermore, all the [[Eigenfunction|eigenfunctions]] can be chosen to be real valued.

If $-X'' = \lambda X$, then conjugating gives $-\bar X'' = \bar\lambda \bar X$ with $\bar X$ satisfying the same (real) conditions; [[Green's Second Identity]] gives $(\lambda - \bar\lambda)(X, X) = 0$, and $(X, X) > 0$ forces $\lambda = \bar\lambda$. Then $\operatorname{Re} X$ and $\operatorname{Im} X$ are themselves real eigenfunctions (or zero).[^2]

# Properties
- Analogue of the reality of eigenvalues of a [[Self-Adjoint Linear Map]] or Hermitian matrix.
- Rules out complex eigenvalues in the [[Dirichlet Eigenvalue Problem on an Interval|Dirichlet]], [[Neumann Eigenvalue Problem on an Interval|Neumann]], [[Robin Eigenvalue Problem on an Interval|Robin]], and periodic problems, so the temporal factors in [[Separation of Variables]] are pure exponentials or sinusoids.
- Companion of the [[Symmetric Boundary Condition Orthogonality Theorem]], which holds unchanged for complex functions.[^3]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=133&annotation=WPEIZNY8)
[^2]: Proof sketch added from general knowledge.
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=133&annotation=Z32Y62HQ)
