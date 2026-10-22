---
tags:
  - mathematics
  - partial_differential_equations
---

# Definition
> [!info] Laplace Equation in a Box[^1][^2]
> For the Dirichlet problem in $D = \{0 < x < a,\ 0 < y < b,\ 0 < z < c\}$ with $u(a, y, z) = g(y, z)$ and $u = 0$ on the other five faces, [[Separation of Variables]] $u = X(x)Y(y)Z(z)$ gives
> $$
> \begin{align}
> u(x, y, z) &= \sum_{m=1}^\infty \sum_{n=1}^\infty A_{mn} \sinh(\gamma_{mn} x)\, \sin\frac{m\pi y}{b}\, \sin\frac{n\pi z}{c}, \qquad \gamma_{mn} = \pi\sqrt{\frac{m^2}{b^2} + \frac{n^2}{c^2}}, \\
> A_{mn} &= \frac{4}{bc\,\sinh(\gamma_{mn} a)} \int_0^c \!\! \int_0^b g(y, z) \sin\frac{m\pi y}{b} \sin\frac{n\pi z}{c}\, dy\, dz .
> \end{align}
> $$
> For the cube $a = b = c = \pi$: $\gamma_{mn} = \sqrt{m^2+n^2}$ and $A_{mn} = \frac{4}{\pi^2\sinh(\sqrt{m^2+n^2}\,\pi)}\int_0^\pi\!\int_0^\pi g \sin my \sin nz\, dy\, dz$.

Matching the inhomogeneous face is a [[Double Fourier Sine Series]] of $g$ in $(y, z)$. Other boundary conditions and several inhomogeneous faces are handled as in the [[Laplace Equation in a Rectangle]], one face at a time.[^1]

# Properties
- The transverse eigenvalues add: $\gamma_{mn}^2 = (m\pi/b)^2 + (n\pi/c)^2$, the eigenvalue of $-\Delta$ on the face rectangle with Dirichlet conditions.[^3]
- As with a double integral, the order of summation of the double series needs care, though in most cases any order works.[^2]

[^1]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=175&annotation=WPBUVICQ)
[^2]: [Partial Differential Equations: An Introduction](zotero://open-pdf/library/items/NNYB7QVM?page=176&annotation=XXIMWAR6)
[^3]: Added from general knowledge.
