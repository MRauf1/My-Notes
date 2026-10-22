---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Double Fourier Sine Series[^1]
> On the square $\{0 < y < \pi,\ 0 < z < \pi\}$, the expansion
> $$
> \begin{align}
> g(y, z) = \sum_{m=1}^\infty\sum_{n=1}^\infty B_{mn} \sin my \, \sin nz, \qquad B_{mn} = \frac{4}{\pi^2}\int_0^\pi\!\!\int_0^\pi g(y, z)\sin my\,\sin nz \, dy\, dz .
> \end{align}
> $$
> On a rectangle $(0, b)\times(0, c)$, use $\sin\frac{m\pi y}{b}\sin\frac{n\pi z}{c}$ and the factor $\frac{4}{bc}$.

The coefficients come from orthogonality: the products $\{\sin my \sin nz\}$ are mutually orthogonal on the square with normalizing constants $\int_0^\pi\!\int_0^\pi (\sin my \sin nz)^2\, dy\, dz = \pi^2/4$.[^1]

# Properties
- Tensor-product extension of the [[Fourier Sine Series]]; its theory is similar to that of the single series.[^1]
- The products are the Dirichlet eigenfunctions of $-\Delta$ on the rectangle, with eigenvalues $m^2 + n^2$ on the square ([[Separation of Variables]]).[^2]
- Order of summation must be handled with care, as for double integrals.[^1]
- Used in [[Laplace Equation in a Box]].

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=176&annotation=XXIMWAR6)
[^2]: Added from general knowledge.
