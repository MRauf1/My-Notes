---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Periodic Boundary Condition[^1]
> On an interval $(-l, l)$, the periodic [[Boundary Condition]] is
> $$
> \begin{align}
> u(-l, t) = u(l, t), \qquad u_x(-l, t) = u_x(l, t).
> \end{align}
> $$
> More generally, on $(a, b)$: $u(a, t) = u(b, t)$ and $u_x(a, t) = u_x(b, t)$, modeling a closed ring of circumference $b - a$.[^2]

# Properties
- The eigenvalue problem $-X'' = \lambda X$ with periodic conditions on $(-l, l)$ has eigenvalues $\lambda_n = (n\pi/l)^2$, $n = 0, 1, 2, \dots$, with eigenfunctions $1$ and $\{\cos(n\pi x/l), \sin(n\pi x/l)\}$; each $\lambda_n$ with $n \geq 1$ has multiplicity two ([[Eigenfunction]]).[^3]
- The corresponding expansion is the full [[Fourier Series]], and the condition corresponds to the [[Periodic Extension]], just as Dirichlet corresponds to the [[Odd Extension]] and Neumann to the [[Even Extension]].[^1]
- A [[Symmetric Boundary Condition]], so eigenfunctions of distinct eigenvalues are orthogonal ([[Symmetric Boundary Condition Orthogonality Theorem]]); within a two-dimensional eigenspace, $\sin$ and $\cos$ happen to be orthogonal, but other choices need not be.[^4]
- Satisfies $f f'\big|_{-l}^{l} = 0$, so there are no negative eigenvalues ([[Symmetric Boundary Condition Nonnegative Eigenvalue Theorem]]).[^5]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=127&annotation=UVTNWTAG)
[^2]: Added from general knowledge.
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=119&annotation=6N9BMZWS)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=132&annotation=HBL3UFLC)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=134&annotation=88LI94RD)
