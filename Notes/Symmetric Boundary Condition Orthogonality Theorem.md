---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!abstract] Theorem (Orthogonality of Eigenfunctions)[^1][^2]
> Let $X_1, X_2$ be [[Eigenfunction|eigenfunctions]] of $-X'' = \lambda X$ on $(a, b)$ under [[Symmetric Boundary Condition|symmetric boundary conditions]], with eigenvalues $\lambda_1 \neq \lambda_2$. Then they are orthogonal in the [[L2 Inner Product]]:
> $$
> \begin{align}
> (X_1, X_2) = \int_a^b X_1(x)\, \overline{X_2(x)}\, dx = 0.
> \end{align}
> $$
> Consequently, if a function is expanded as $\phi = \sum_n A_n X_n$, the coefficients are determined:[^3]
> $$
> \begin{align}
> A_m = \frac{(\phi, X_m)}{(X_m, X_m)}.
> \end{align}
> $$

By [[Green's Second Identity]], $(\lambda_1 - \lambda_2)(X_1, X_2) = \left(-X_1' X_2 + X_1 X_2'\right)\big|_a^b = 0$, since the boundary term vanishes for symmetric conditions. This explains the "wonderful coincidence" behind the orthogonality of sines, cosines, and the full trigonometric system: it is no accident but a consequence of the symmetry of $-d^2/dx^2$.[^4] The proof holds verbatim for complex-valued functions with hermitian conditions.[^5]

# Properties
- Infinite-dimensional analogue of the orthogonality of eigenvectors of a [[Self-Adjoint Linear Map]] ([[Spectral Theorem]]).
- Eigenfunctions sharing an eigenvalue need not be orthogonal (e.g. $\sin(n\pi x/l)$ and $\cos(n\pi x/l) + \sin(n\pi x/l)$ under [[Periodic Boundary Condition|periodic conditions]]), but they can be made orthogonal by the [[Gram-Schmidt Algorithm]].[^6]
- Says nothing about convergence of the expansion; that is settled by the [[Fourier Series L2 Convergence Theorem]] and its companions.[^6]
- Special cases: the coefficient formulas of the [[Fourier Sine Series]], [[Fourier Cosine Series]], and full [[Fourier Series]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=132&annotation=DQ67LX9Y)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=132&annotation=UJWR83NP)
[^3]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=132&annotation=MY7V4K98)
[^4]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=130&annotation=C326VLDR)
[^5]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=133&annotation=Z32Y62HQ)
[^6]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=132&annotation=HBL3UFLC)
